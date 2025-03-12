/**************************************************************************
 *
 * Copyright 2011 LunarG, Inc.
 * Copyright 2011 Jose Fonseca
 * All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 **************************************************************************/

#include <assert.h>
#include <stdlib.h>

#include <iostream>

#include <dlfcn.h>

#include "glproc.hpp"
#include "glws.hpp"
// #include "glws_xlib.hpp"
#include <screen/screen.h>

#include <EGL/eglext.h>


namespace glws {


static EGLDisplay eglDisplay = EGL_NO_DISPLAY;
static char const *eglExtensions = NULL;
static bool has_EGL_KHR_create_context = false;


static EGLenum
translateAPI(glfeatures::Profile profile)
{
    switch (profile.api) {
    case glfeatures::API_GL:
        return EGL_OPENGL_API;
    case glfeatures::API_GLES:
        return EGL_OPENGL_ES_API;
    default:
        assert(0);
        return EGL_NONE;
    }
}


/* Must be called before
 *
 * - eglCreateContext
 * - eglGetCurrentContext
 * - eglGetCurrentDisplay
 * - eglGetCurrentSurface
 * - eglMakeCurrent (when its ctx parameter is EGL_NO_CONTEXT ),
 * - eglWaitClient
 * - eglWaitNative
 */
static void
bindAPI(EGLenum api)
{
    if (eglBindAPI(api) != EGL_TRUE) {
        std::cerr << "error: eglBindAPI failed\n";
        exit(1);
    }
}


class EglVisual : public Visual
{
public:
    EGLConfig config;
    screen_context_t screen_ctx;

    EglVisual(Profile prof, screen_context_t ctx) :
        Visual(prof),
        config(0),
        screen_ctx(ctx)
    {}

    ~EglVisual() {
        screen_destroy_context(screen_ctx);
    }
};


class EglDrawable : public Drawable
{
public:
    screen_window_t window;
    EGLSurface surface;
    EGLenum api;

    EglDrawable(const Visual *vis, int w, int h,
                const glws::pbuffer_info *pbInfo) :
        Drawable(vis, w, h, pbInfo),
        api(EGL_OPENGL_ES_API)
    {
        std::cerr << "create drawable with size = " << w << ", " << h << "\n";

        createWindow(w, h);
    }

    void createWindow(int w, int h)
    {
        screen_create_window(&window, static_cast<const EglVisual*>(visual)->screen_ctx);

        eglWaitNative(EGL_CORE_NATIVE_ENGINE);

        int usage, format;
        int interval = 1;
        int size[2] = { w, h }; /* Size of window */
        int pos[2] = { 0, 0 };      /* Position of window */

        /* Indicate that OpenGL ES 2.x or 3.x will render to the buffer associated with this render target. */
        usage = SCREEN_USAGE_OPENGL_ES2 | SCREEN_USAGE_OPENGL_ES3;
        format = SCREEN_FORMAT_RGBA8888;    /* Indicate the pixel format to be used. */
        screen_set_window_property_iv(window, SCREEN_PROPERTY_USAGE, &usage);
        screen_set_window_property_iv(window, SCREEN_PROPERTY_FORMAT, &format);
        screen_set_window_property_iv(window, SCREEN_PROPERTY_SWAP_INTERVAL, &interval);
        screen_set_window_property_iv(window, SCREEN_PROPERTY_SIZE, size);
        screen_set_window_property_iv(window, SCREEN_PROPERTY_POSITION, pos);

        int nbuffers = 2;           /* Number of window buffers */
        screen_create_window_buffers(window, nbuffers);   

        EGLConfig config = static_cast<const EglVisual *>(visual)->config;
        surface = eglCreateWindowSurface(eglDisplay, config, (EGLNativeWindowType)window, NULL);
    }

    ~EglDrawable() {
        eglDestroySurface(eglDisplay, surface);
        eglWaitClient();
        screen_destroy_window(window);
        eglWaitNative(EGL_CORE_NATIVE_ENGINE);
    }

    void
    setDamageRegion(int *rects, int nrects) override {
        screen_discard_window_regions(window, nrects, rects);
    }

    void
    recreate(void) {
        std::cerr << "retrace: recreate\n";
        EGLContext currentContext = eglGetCurrentContext();
        EGLSurface currentDrawSurface = eglGetCurrentSurface(EGL_DRAW);
        EGLSurface currentReadSurface = eglGetCurrentSurface(EGL_READ);
        bool rebindDrawSurface = currentDrawSurface == surface;
        bool rebindReadSurface = currentReadSurface == surface;

        if (rebindDrawSurface || rebindReadSurface) {
            eglMakeCurrent(eglDisplay, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
        }

        // XXX: Defer destruction to prevent getting the same surface as before, which seems to cause Mesa to crash
        EGLSurface oldSurface = surface;

        EGLConfig config = static_cast<const EglVisual *>(visual)->config;
        surface = eglCreateWindowSurface(eglDisplay, config, (EGLNativeWindowType)window, NULL);
        if (surface == EGL_NO_SURFACE) {
            // XXX: But don't defer destruction if eglCreateWindowSurface fails, which is the case of SwiftShader
            eglDestroySurface(eglDisplay, oldSurface);
            oldSurface = EGL_NO_SURFACE;
            surface = eglCreateWindowSurface(eglDisplay, config, (EGLNativeWindowType)window, NULL);
        }
        assert(surface != EGL_NO_SURFACE);

        if (rebindDrawSurface || rebindReadSurface) {
            eglMakeCurrent(eglDisplay, surface, surface, currentContext);
        }

        if (oldSurface != EGL_NO_SURFACE) {
            eglDestroySurface(eglDisplay, oldSurface);
        }
    }

    void
    resize(int w, int h) override {
        std::cerr << "retrace: resize to " << w << "," << h << "\n";
        if (w == width && h == height) {
            std::cerr << "no need to resize\n";
            return;
        }

        eglWaitClient();

        Drawable::resize(w, h);

        /* full destroy and then re-create */
        eglDestroySurface(eglDisplay, surface);
        eglWaitClient();
        screen_destroy_window(window);
        eglWaitNative(EGL_CORE_NATIVE_ENGINE);
        createWindow(w, h);

        /*
         * Some implementations won't update the backbuffer unless we recreate
         * the EGL surface.
         */

        int eglWidth;
        int eglHeight;

        eglQuerySurface(eglDisplay, surface, EGL_WIDTH, &eglWidth);
        eglQuerySurface(eglDisplay, surface, EGL_HEIGHT, &eglHeight);

        if (eglWidth != width || eglHeight != height) {
            std::cerr << "surface not updated! try recreate\n";
            recreate();

            eglQuerySurface(eglDisplay, surface, EGL_WIDTH, &eglWidth);
            eglQuerySurface(eglDisplay, surface, EGL_HEIGHT, &eglHeight);
        }

        assert(eglWidth == width);
        assert(eglHeight == height);
    }

    void show(void) override {
        if (visible) {
            return;
        }

        eglWaitClient();

        int visible = 1;
        screen_set_window_property_iv(window, SCREEN_PROPERTY_VISIBLE, &visible);

        eglWaitNative(EGL_CORE_NATIVE_ENGINE);

        Drawable::show();
    }

    void swapBuffers(void) override {
        bindAPI(api);
        eglSwapBuffers(eglDisplay, surface);
        // processKeys(window);
    }

    void swapBuffersWithDamage(int *rects, int nrects) override {
        if (!checkExtension("EGL_KHR_swap_buffers_with_damage", eglExtensions))
            return;

        bindAPI(api);
        eglSwapBuffersWithDamageEXT(eglDisplay, surface, rects, nrects);
        // processKeys(window);
    }
};


class EglContext : public Context
{
public:
    EGLContext context;

    EglContext(const Visual *vis, EGLContext ctx) :
        Context(vis),
        context(ctx)
    {}

    ~EglContext() {
        eglDestroyContext(eglDisplay, context);
    }
};

/**
 * Load the symbols from the specified shared object into global namespace, so
 * that they can be later found by dlsym(RTLD_NEXT, ...);
 */
static void
load(const char *filename)
{
    if (!dlopen(filename, RTLD_GLOBAL | RTLD_LAZY)) {
        std::cerr << "error: unable to open " << filename << "\n";
        exit(1);
    }
}

static void
loadEGLLib(const char *path)
{
    const char* eglLib = getenv("SDL_VIDEO_EGL_DRIVER");
    load(eglLib != NULL ? eglLib : path);
}

static void
loadGLLib(const char *path)
{
    const char* glLib = getenv("SDL_VIDEO_GL_DRIVER");
    load(glLib != NULL ? glLib : path);
}

bool
processEvents(void) {
    return true;
}

void
init(void) {
    loadEGLLib("libEGL.so.1");

    eglDisplay = eglGetDisplay(EGL_DEFAULT_DISPLAY);

    if (eglDisplay == EGL_NO_DISPLAY) {
        std::cerr << "error: unable to get EGL display\n";
        exit(1);
    }

    EGLint major, minor;
    if (!eglInitialize(eglDisplay, &major, &minor)) {
        std::cerr << "error: unable to initialize EGL display\n";
        exit(1);
    }

    eglExtensions = eglQueryString(eglDisplay, EGL_EXTENSIONS);
    has_EGL_KHR_create_context = checkExtension("EGL_KHR_create_context", eglExtensions);
}

void
cleanup(void) {
    if (eglDisplay != EGL_NO_DISPLAY) {
        eglTerminate(eglDisplay);
    }
}


Visual *
createVisual(bool doubleBuffer, unsigned samples, Profile profile) {
    EGLint api_bits;
    if (profile.api == glfeatures::API_GL) {
        api_bits = EGL_OPENGL_BIT;
        if (profile.core && !has_EGL_KHR_create_context) {
            return NULL;
        }
    } else if (profile.api == glfeatures::API_GLES) {
        switch (profile.major) {
        case 1:
            api_bits = EGL_OPENGL_ES_BIT;
            break;
        case 3:
            if (has_EGL_KHR_create_context) {
                api_bits = EGL_OPENGL_ES3_BIT;
                break;
            }
            /* fall-through */
        case 2:
            api_bits = EGL_OPENGL_ES2_BIT;
            break;
        default:
            return NULL;
        }
    } else {
        assert(0);
        return NULL;
    }

    Attributes<EGLint> attribs;
    attribs.add(EGL_SURFACE_TYPE, EGL_WINDOW_BIT);
    attribs.add(EGL_RED_SIZE, 8);
    attribs.add(EGL_GREEN_SIZE, 8);
    attribs.add(EGL_BLUE_SIZE, 8);
    attribs.add(EGL_ALPHA_SIZE, 8);
    attribs.add(EGL_DEPTH_SIZE, 24);
    attribs.add(EGL_STENCIL_SIZE, 8);
    attribs.add(EGL_RENDERABLE_TYPE, api_bits);
    attribs.end(EGL_NONE);

    EGLint num_configs = 0;
    if (!eglGetConfigs(eglDisplay, NULL, 0, &num_configs) ||
        num_configs <= 0) {
        return NULL;
    }

    std::vector<EGLConfig> configs(num_configs);
    if (!eglChooseConfig(eglDisplay, attribs, &configs[0], num_configs,  &num_configs) ||
        num_configs <= 0) {
        return NULL;
    }

    // We can't tell what other APIs the trace will use afterwards, therefore
    // try to pick a config which supports the widest set of APIs.
    int bestScore = -1;
    EGLConfig config = configs[0];
    for (EGLint i = 0; i < num_configs; ++i) {
        EGLint renderable_type = EGL_NONE;
        eglGetConfigAttrib(eglDisplay, configs[i], EGL_RENDERABLE_TYPE, &renderable_type);
        int score = 0;
        assert(renderable_type & api_bits);
        renderable_type &= ~api_bits;
        if (renderable_type & EGL_OPENGL_ES2_BIT) {
            score += 1 << 4;
        }
        if (renderable_type & EGL_OPENGL_ES3_BIT) {
            score += 1 << 3;
        }
        if (renderable_type & EGL_OPENGL_ES_BIT) {
            score += 1 << 2;
        }
        if (renderable_type & EGL_OPENGL_BIT) {
            score += 1 << 1;
        }
        if (score > bestScore) {
            config = configs[i];
            bestScore = score;
        }
    }
    assert(bestScore >= 0);

    screen_context_t screen_ctx;

    if (screen_create_context(&screen_ctx, SCREEN_APPLICATION_CONTEXT) == -1)
    {
        std::cerr << "error: screen_create_context failed!\n";
        exit(1);
    }
    
    EglVisual *visual = new EglVisual(profile, screen_ctx);
    visual->config = config;
    return visual;
}

Drawable *
createDrawable(const Visual *visual, int width, int height,
               const glws::pbuffer_info *pbInfo)
{
    return new EglDrawable(visual, width, height, pbInfo);
}

Context *
createContext(const Visual *_visual, Context *shareContext, bool debug)
{
    Profile profile = _visual->profile;
    const EglVisual *visual = static_cast<const EglVisual *>(_visual);
    EGLContext share_context = EGL_NO_CONTEXT;
    EGLContext context;
    Attributes<EGLint> attribs;

    if (shareContext) {
        share_context = static_cast<EglContext*>(shareContext)->context;
    }

    int contextFlags = 0;
    if (profile.api == glfeatures::API_GL) {
        loadGLLib("libGL.so.1");

        if (has_EGL_KHR_create_context) {
            attribs.add(EGL_CONTEXT_MAJOR_VERSION_KHR, profile.major);
            attribs.add(EGL_CONTEXT_MINOR_VERSION_KHR, profile.minor);
            int profileMask = profile.core ? EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT_KHR : EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT_KHR;
            attribs.add(EGL_CONTEXT_OPENGL_PROFILE_MASK_KHR, profileMask);
            if (profile.forwardCompatible) {
                contextFlags |= EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE_BIT_KHR;
            }
        } else if (profile.versionGreaterOrEqual(3, 2)) {
            std::cerr << "error: EGL_KHR_create_context not supported\n";
            return NULL;
        }
    } else if (profile.api == glfeatures::API_GLES) {
        if (profile.major >= 2) {
            loadGLLib("libGLESv2.so.2");
        } else {
            loadGLLib("libGLESv1_CM.so.1");
        }

        if (has_EGL_KHR_create_context) {
            attribs.add(EGL_CONTEXT_MAJOR_VERSION_KHR, profile.major);
            attribs.add(EGL_CONTEXT_MINOR_VERSION_KHR, profile.minor);
        } else {
            attribs.add(EGL_CONTEXT_CLIENT_VERSION, profile.major);
        }
    } else {
        assert(0);
        return NULL;
    }

    if (debug) {
        contextFlags |= EGL_CONTEXT_OPENGL_DEBUG_BIT_KHR;
    }
    if (contextFlags && has_EGL_KHR_create_context) {
        attribs.add(EGL_CONTEXT_FLAGS_KHR, contextFlags);
    }
    attribs.end(EGL_NONE);

    EGLenum api = translateAPI(profile);
    bindAPI(api);

    context = eglCreateContext(eglDisplay, visual->config, share_context, attribs);
    if (!context) {
        if (debug) {
            // XXX: Mesa has problems with EGL_CONTEXT_OPENGL_DEBUG_BIT_KHR
            // with OpenGL ES contexts, so retry without it
            return createContext(_visual, shareContext, false);
        }
        return NULL;
    }

    return new EglContext(visual, context);
}

bool
makeCurrentInternal(Drawable *drawable, Drawable *readable, Context *context)
{
    if (!drawable || !context) {
        return eglMakeCurrent(eglDisplay, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
    } else {
        EglDrawable *eglDrawable = static_cast<EglDrawable *>(drawable);
        EglDrawable *eglReadable = static_cast<EglDrawable *>(readable);
        EglContext *eglContext = static_cast<EglContext *>(context);
        EGLBoolean ok;

        EGLenum api = translateAPI(eglContext->profile);
        bindAPI(api);

        ok = eglMakeCurrent(eglDisplay, eglDrawable->surface,
                            eglReadable->surface, eglContext->context);

        if (ok) {
            eglDrawable->api = api;
            eglReadable->api = api;
        }

        return ok;
    }
}


bool
bindTexImage(Drawable *pBuffer, int iBuffer) {
    std::cerr << "error: EGL/QNX::wglBindTexImageARB not implemented.\n";
    assert(pBuffer->pbuffer);
    return true;
}

bool
releaseTexImage(Drawable *pBuffer, int iBuffer) {
    std::cerr << "error: EGL/QNX::wglReleaseTexImageARB not implemented.\n";
    assert(pBuffer->pbuffer);
    return true;
}

bool
setPbufferAttrib(Drawable *pBuffer, const int *attribList) {
    // nothing to do here.
    assert(pBuffer->pbuffer);
    return true;
}


} /* namespace glws */
