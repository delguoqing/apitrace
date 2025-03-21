##########################################################################
#
# Copyright 2011 Jose Fonseca
# Copyright 2008-2010 VMware, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/


"""GL API description.

Most of these were automatically generated from Khronos OpenGL spec files by
the specs/scripts/glspec.py script, and then manually edited to cover the
corner cases correctly.

"""


from .stdapi import *
from .gltypes import *
from . import glparams


def GlFunction(*args, **kwargs):
    kwargs.setdefault('call', 'APIENTRY')
    return Function(*args, **kwargs)


def InGlString(charType, length, argName):
    # Helper function to describe input strings, where string length can be
    # passed as argument.
    lengthExpr = '((%s) >= 0 ? (%s) : strlen(%s))' % (length, length, argName)
    return In(String(Const(charType), lengthExpr), argName)

def OutGlString(charType, lengthPtr, argName):
    # Helper function to describe output strings, where string length can be
    # returned as a pointer.
    lengthExpr = '((%s) ? *(%s) : strlen(%s))' % (lengthPtr, lengthPtr, argName)
    return Out(String(charType, lengthExpr), argName)


glapi = Module('GL')


glapi.addFunctions([
    # GL_VERSION_1_0
    GlFunction(Void, "glCullFace", [(GLenum, "mode")]),
    GlFunction(Void, "glFrontFace", [(GLenum, "mode")]),
    GlFunction(Void, "glHint", [(GLenum, "target"), (GLenum, "mode")]),
    GlFunction(Void, "glLineWidth", [(GLfloat, "width")]),
    GlFunction(Void, "glPointSize", [(GLfloat, "size")]),
    GlFunction(Void, "glPolygonMode", [(GLenum, "face"), (GLenum, "mode")]),
    GlFunction(Void, "glScissor", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glTexParameterf", [(GLenum, "target"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glTexParameterfv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexParameteri", [(GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glTexParameteriv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexImage1D", [(GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage1D_size(format, type, width)"), "pixels")]),
    GlFunction(Void, "glTexImage2D", [(GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage2D_size(format, type, width, height)"), "pixels")]),
    GlFunction(Void, "glDrawBuffer", [(GLenum, "mode")]),
    GlFunction(Void, "glClear", [(GLbitfield_attrib, "mask")]),
    GlFunction(Void, "glClearColor", [(GLfloat, "red"), (GLfloat, "green"), (GLfloat, "blue"), (GLfloat, "alpha")]),
    GlFunction(Void, "glClearStencil", [(GLint, "s")]),
    GlFunction(Void, "glClearDepth", [(GLdouble, "depth")]),
    GlFunction(Void, "glStencilMask", [(GLuint, "mask")]),
    GlFunction(Void, "glColorMask", [(GLboolean, "red"), (GLboolean, "green"), (GLboolean, "blue"), (GLboolean, "alpha")]),
    GlFunction(Void, "glDepthMask", [(GLboolean, "flag")]),
    GlFunction(Void, "glDisable", [(GLenum, "cap")]),
    GlFunction(Void, "glEnable", [(GLenum, "cap")]),
    GlFunction(Void, "glFinish", []),
    GlFunction(Void, "glFlush", []),
    GlFunction(Void, "glBlendFunc", [(GLenum, "sfactor"), (GLenum, "dfactor")]),
    GlFunction(Void, "glLogicOp", [(GLenum, "opcode")]),
    GlFunction(Void, "glStencilFunc", [(GLenum, "func"), (GLint, "ref"), (GLuint, "mask")]),
    GlFunction(Void, "glStencilOp", [(GLenum, "fail"), (GLenum, "zfail"), (GLenum, "zpass")]),
    GlFunction(Void, "glDepthFunc", [(GLenum, "func")]),
    GlFunction(Void, "glPixelStoref", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glPixelStorei", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glReadBuffer", [(GLenum, "mode")]),
    GlFunction(Void, "glReadPixels", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), Out(GLpointer, "pixels")]),
    GlFunction(Void, "glGetBooleanv", [(GLenum, "pname"), Out(Array(GLboolean, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetDoublev", [(GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLenum_error, "glGetError", [], sideeffects=False),
    GlFunction(Void, "glGetFloatv", [(GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetIntegerv", [(GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(String(Const(GLubyte)), "glGetString", [(GLenum, "name")], sideeffects=False),
    GlFunction(Void, "glGetTexImage", [(GLenum, "target"), (GLint, "level"), (GLenum, "format"), (GLenum, "type"), Out(GLpointer, "pixels")]),
    GlFunction(Void, "glGetTexParameterfv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexParameteriv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexLevelParameterfv", [(GLenum, "target"), (GLint, "level"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexLevelParameteriv", [(GLenum, "target"), (GLint, "level"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLboolean, "glIsEnabled", [(GLenum, "cap")], sideeffects=False),
    GlFunction(Void, "glDepthRange", [(GLdouble, "zNear"), (GLdouble, "zFar")]),
    GlFunction(Void, "glViewport", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),

    # GL_VERSION_1_0_DEPRECATED
    GlFunction(Void, "glNewList", [(GLlist, "list"), (GLenum, "mode")]),
    GlFunction(Void, "glEndList", []),
    GlFunction(Void, "glCallList", [(GLlist, "list")]),
    GlFunction(Void, "glCallLists", [(GLsizei, "n"), (GLenum, "type"), (Blob(Const(GLvoid), "_glCallLists_size(n, type)"), "lists")]),
    GlFunction(Void, "glDeleteLists", [(GLlist, "list"), (GLsizei, "range")]),
    GlFunction(Handle("list", GLuint, "range"), "glGenLists", [(GLsizei, "range")]),
    GlFunction(Void, "glListBase", [(GLlist, "base")]),
    GlFunction(Void, "glBegin", [(GLenum_mode, "mode")]),
    GlFunction(Void, "glBitmap", [(GLsizei, "width"), (GLsizei, "height"), (GLfloat, "xorig"), (GLfloat, "yorig"), (GLfloat, "xmove"), (GLfloat, "ymove"), (Blob(Const(GLubyte), "_glBitmap_size(width, height)"), "bitmap")]),
    GlFunction(Void, "glColor3b", [(GLbyte, "red"), (GLbyte, "green"), (GLbyte, "blue")]),
    GlFunction(Void, "glColor3bv", [(Array(Const(GLbyte), 3), "v")]),
    GlFunction(Void, "glColor3d", [(GLdouble, "red"), (GLdouble, "green"), (GLdouble, "blue")]),
    GlFunction(Void, "glColor3dv", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glColor3f", [(GLfloat, "red"), (GLfloat, "green"), (GLfloat, "blue")]),
    GlFunction(Void, "glColor3fv", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glColor3i", [(GLint, "red"), (GLint, "green"), (GLint, "blue")]),
    GlFunction(Void, "glColor3iv", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glColor3s", [(GLshort, "red"), (GLshort, "green"), (GLshort, "blue")]),
    GlFunction(Void, "glColor3sv", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glColor3ub", [(GLubyte, "red"), (GLubyte, "green"), (GLubyte, "blue")]),
    GlFunction(Void, "glColor3ubv", [(Array(Const(GLubyte), 3), "v")]),
    GlFunction(Void, "glColor3ui", [(GLuint, "red"), (GLuint, "green"), (GLuint, "blue")]),
    GlFunction(Void, "glColor3uiv", [(Array(Const(GLuint), 3), "v")]),
    GlFunction(Void, "glColor3us", [(GLushort, "red"), (GLushort, "green"), (GLushort, "blue")]),
    GlFunction(Void, "glColor3usv", [(Array(Const(GLushort), 3), "v")]),
    GlFunction(Void, "glColor4b", [(GLbyte, "red"), (GLbyte, "green"), (GLbyte, "blue"), (GLbyte, "alpha")]),
    GlFunction(Void, "glColor4bv", [(Array(Const(GLbyte), 4), "v")]),
    GlFunction(Void, "glColor4d", [(GLdouble, "red"), (GLdouble, "green"), (GLdouble, "blue"), (GLdouble, "alpha")]),
    GlFunction(Void, "glColor4dv", [(Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glColor4f", [(GLfloat, "red"), (GLfloat, "green"), (GLfloat, "blue"), (GLfloat, "alpha")]),
    GlFunction(Void, "glColor4fv", [(Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glColor4i", [(GLint, "red"), (GLint, "green"), (GLint, "blue"), (GLint, "alpha")]),
    GlFunction(Void, "glColor4iv", [(Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glColor4s", [(GLshort, "red"), (GLshort, "green"), (GLshort, "blue"), (GLshort, "alpha")]),
    GlFunction(Void, "glColor4sv", [(Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glColor4ub", [(GLubyte, "red"), (GLubyte, "green"), (GLubyte, "blue"), (GLubyte, "alpha")]),
    GlFunction(Void, "glColor4ubv", [(Array(Const(GLubyte), 4), "v")]),
    GlFunction(Void, "glColor4ui", [(GLuint, "red"), (GLuint, "green"), (GLuint, "blue"), (GLuint, "alpha")]),
    GlFunction(Void, "glColor4uiv", [(Array(Const(GLuint), 4), "v")]),
    GlFunction(Void, "glColor4us", [(GLushort, "red"), (GLushort, "green"), (GLushort, "blue"), (GLushort, "alpha")]),
    GlFunction(Void, "glColor4usv", [(Array(Const(GLushort), 4), "v")]),
    GlFunction(Void, "glEdgeFlag", [(GLboolean, "flag")]),
    GlFunction(Void, "glEdgeFlagv", [(Pointer(Const(GLboolean)), "flag")]),
    GlFunction(Void, "glEnd", []),
    GlFunction(Void, "glIndexd", [(GLdouble, "c")]),
    GlFunction(Void, "glIndexdv", [(Pointer(Const(GLdouble)), "c")]),
    GlFunction(Void, "glIndexf", [(GLfloat, "c")]),
    GlFunction(Void, "glIndexfv", [(Pointer(Const(GLfloat)), "c")]),
    GlFunction(Void, "glIndexi", [(GLint, "c")]),
    GlFunction(Void, "glIndexiv", [(Pointer(Const(GLint)), "c")]),
    GlFunction(Void, "glIndexs", [(GLshort, "c")]),
    GlFunction(Void, "glIndexsv", [(Pointer(Const(GLshort)), "c")]),
    GlFunction(Void, "glNormal3b", [(GLbyte, "nx"), (GLbyte, "ny"), (GLbyte, "nz")]),
    GlFunction(Void, "glNormal3bv", [(Array(Const(GLbyte), 3), "v")]),
    GlFunction(Void, "glNormal3d", [(GLdouble, "nx"), (GLdouble, "ny"), (GLdouble, "nz")]),
    GlFunction(Void, "glNormal3dv", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glNormal3f", [(GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz")]),
    GlFunction(Void, "glNormal3fv", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glNormal3i", [(GLint, "nx"), (GLint, "ny"), (GLint, "nz")]),
    GlFunction(Void, "glNormal3iv", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glNormal3s", [(GLshort, "nx"), (GLshort, "ny"), (GLshort, "nz")]),
    GlFunction(Void, "glNormal3sv", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glRasterPos2d", [(GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glRasterPos2dv", [(Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glRasterPos2f", [(GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glRasterPos2fv", [(Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glRasterPos2i", [(GLint, "x"), (GLint, "y")]),
    GlFunction(Void, "glRasterPos2iv", [(Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glRasterPos2s", [(GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glRasterPos2sv", [(Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glRasterPos3d", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glRasterPos3dv", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glRasterPos3f", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glRasterPos3fv", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glRasterPos3i", [(GLint, "x"), (GLint, "y"), (GLint, "z")]),
    GlFunction(Void, "glRasterPos3iv", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glRasterPos3s", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glRasterPos3sv", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glRasterPos4d", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glRasterPos4dv", [(Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glRasterPos4f", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glRasterPos4fv", [(Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glRasterPos4i", [(GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glRasterPos4iv", [(Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glRasterPos4s", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z"), (GLshort, "w")]),
    GlFunction(Void, "glRasterPos4sv", [(Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glRectd", [(GLdouble, "x1"), (GLdouble, "y1"), (GLdouble, "x2"), (GLdouble, "y2")]),
    GlFunction(Void, "glRectdv", [(Array(Const(GLdouble), 2), "v1"), (Array(Const(GLdouble), 2), "v2")]),
    GlFunction(Void, "glRectf", [(GLfloat, "x1"), (GLfloat, "y1"), (GLfloat, "x2"), (GLfloat, "y2")]),
    GlFunction(Void, "glRectfv", [(Array(Const(GLfloat), 2), "v1"), (Array(Const(GLfloat), 2), "v2")]),
    GlFunction(Void, "glRecti", [(GLint, "x1"), (GLint, "y1"), (GLint, "x2"), (GLint, "y2")]),
    GlFunction(Void, "glRectiv", [(Array(Const(GLint), 2), "v1"), (Array(Const(GLint), 2), "v2")]),
    GlFunction(Void, "glRects", [(GLshort, "x1"), (GLshort, "y1"), (GLshort, "x2"), (GLshort, "y2")]),
    GlFunction(Void, "glRectsv", [(Array(Const(GLshort), 2), "v1"), (Array(Const(GLshort), 2), "v2")]),
    GlFunction(Void, "glTexCoord1d", [(GLdouble, "s")]),
    GlFunction(Void, "glTexCoord1dv", [(Pointer(Const(GLdouble)), "v")]),
    GlFunction(Void, "glTexCoord1f", [(GLfloat, "s")]),
    GlFunction(Void, "glTexCoord1fv", [(Pointer(Const(GLfloat)), "v")]),
    GlFunction(Void, "glTexCoord1i", [(GLint, "s")]),
    GlFunction(Void, "glTexCoord1iv", [(Pointer(Const(GLint)), "v")]),
    GlFunction(Void, "glTexCoord1s", [(GLshort, "s")]),
    GlFunction(Void, "glTexCoord1sv", [(Pointer(Const(GLshort)), "v")]),
    GlFunction(Void, "glTexCoord2d", [(GLdouble, "s"), (GLdouble, "t")]),
    GlFunction(Void, "glTexCoord2dv", [(Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glTexCoord2f", [(GLfloat, "s"), (GLfloat, "t")]),
    GlFunction(Void, "glTexCoord2fv", [(Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glTexCoord2i", [(GLint, "s"), (GLint, "t")]),
    GlFunction(Void, "glTexCoord2iv", [(Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glTexCoord2s", [(GLshort, "s"), (GLshort, "t")]),
    GlFunction(Void, "glTexCoord2sv", [(Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glTexCoord3d", [(GLdouble, "s"), (GLdouble, "t"), (GLdouble, "r")]),
    GlFunction(Void, "glTexCoord3dv", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glTexCoord3f", [(GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r")]),
    GlFunction(Void, "glTexCoord3fv", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glTexCoord3i", [(GLint, "s"), (GLint, "t"), (GLint, "r")]),
    GlFunction(Void, "glTexCoord3iv", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glTexCoord3s", [(GLshort, "s"), (GLshort, "t"), (GLshort, "r")]),
    GlFunction(Void, "glTexCoord3sv", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glTexCoord4d", [(GLdouble, "s"), (GLdouble, "t"), (GLdouble, "r"), (GLdouble, "q")]),
    GlFunction(Void, "glTexCoord4dv", [(Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glTexCoord4f", [(GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r"), (GLfloat, "q")]),
    GlFunction(Void, "glTexCoord4fv", [(Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glTexCoord4i", [(GLint, "s"), (GLint, "t"), (GLint, "r"), (GLint, "q")]),
    GlFunction(Void, "glTexCoord4iv", [(Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glTexCoord4s", [(GLshort, "s"), (GLshort, "t"), (GLshort, "r"), (GLshort, "q")]),
    GlFunction(Void, "glTexCoord4sv", [(Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glVertex2d", [(GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glVertex2dv", [(Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glVertex2f", [(GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glVertex2fv", [(Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glVertex2i", [(GLint, "x"), (GLint, "y")]),
    GlFunction(Void, "glVertex2iv", [(Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glVertex2s", [(GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glVertex2sv", [(Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glVertex3d", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glVertex3dv", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glVertex3f", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glVertex3fv", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glVertex3i", [(GLint, "x"), (GLint, "y"), (GLint, "z")]),
    GlFunction(Void, "glVertex3iv", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glVertex3s", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glVertex3sv", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glVertex4d", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glVertex4dv", [(Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glVertex4f", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glVertex4fv", [(Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glVertex4i", [(GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glVertex4iv", [(Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glVertex4s", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z"), (GLshort, "w")]),
    GlFunction(Void, "glVertex4sv", [(Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glClipPlane", [(GLenum, "plane"), (Array(Const(GLdouble), 4), "equation")]),
    GlFunction(Void, "glColorMaterial", [(GLenum, "face"), (GLenum, "mode")]),
    GlFunction(Void, "glFogf", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glFogfv", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glFogi", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glFogiv", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glLightf", [(GLenum, "light"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glLightfv", [(GLenum, "light"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glLighti", [(GLenum, "light"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glLightiv", [(GLenum, "light"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glLightModelf", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glLightModelfv", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glLightModeli", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glLightModeliv", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glLineStipple", [(GLint, "factor"), (GLushort, "pattern")]),
    GlFunction(Void, "glMaterialf", [(GLenum, "face"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glMaterialfv", [(GLenum, "face"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMateriali", [(GLenum, "face"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glMaterialiv", [(GLenum, "face"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glPolygonStipple", [(Array(Const(GLubyte), "_glPolygonStipple_size()"), "mask")]),
    GlFunction(Void, "glShadeModel", [(GLenum, "mode")]),
    GlFunction(Void, "glTexEnvf", [(GLenum, "target"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glTexEnvfv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexEnvi", [(GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glTexEnviv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexGend", [(GLenum, "coord"), (GLenum, "pname"), (GLdouble, "param")]),
    GlFunction(Void, "glTexGendv", [(GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLdouble), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexGenf", [(GLenum, "coord"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glTexGenfv", [(GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexGeni", [(GLenum, "coord"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glTexGeniv", [(GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glFeedbackBuffer", [(GLsizei, "size"), (GLenum, "type"), Out(Array(GLfloat, "size"), "buffer")]),
    GlFunction(Void, "glSelectBuffer", [(GLsizei, "size"), Out(Array(GLuint, "size"), "buffer")]),
    GlFunction(Alias("GLint", GLenum), "glRenderMode", [(GLenum, "mode")]),
    GlFunction(Void, "glInitNames", []),
    GlFunction(Void, "glLoadName", [(GLuint, "name")]),
    GlFunction(Void, "glPassThrough", [(GLfloat, "token")]),
    GlFunction(Void, "glPopName", []),
    GlFunction(Void, "glPushName", [(GLuint, "name")]),
    GlFunction(Void, "glClearAccum", [(GLfloat, "red"), (GLfloat, "green"), (GLfloat, "blue"), (GLfloat, "alpha")]),
    GlFunction(Void, "glClearIndex", [(GLfloat, "c")]),
    GlFunction(Void, "glIndexMask", [(GLuint, "mask")]),
    GlFunction(Void, "glAccum", [(GLenum, "op"), (GLfloat, "value")]),
    GlFunction(Void, "glPopAttrib", []),
    GlFunction(Void, "glPushAttrib", [(GLbitfield_attrib, "mask")]),
    GlFunction(Void, "glMap1d", [(GLenum, "target"), (GLdouble, "u1"), (GLdouble, "u2"), (GLint, "stride"), (GLint, "order"), (Array(Const(GLdouble), "_glMap1d_size(target, stride, order)"), "points")]),
    GlFunction(Void, "glMap1f", [(GLenum, "target"), (GLfloat, "u1"), (GLfloat, "u2"), (GLint, "stride"), (GLint, "order"), (Array(Const(GLfloat), "_glMap1f_size(target, stride, order)"), "points")]),
    GlFunction(Void, "glMap2d", [(GLenum, "target"), (GLdouble, "u1"), (GLdouble, "u2"), (GLint, "ustride"), (GLint, "uorder"), (GLdouble, "v1"), (GLdouble, "v2"), (GLint, "vstride"), (GLint, "vorder"), (Array(Const(GLdouble), "_glMap2d_size(target, ustride, uorder, vstride, vorder)"), "points")]),
    GlFunction(Void, "glMap2f", [(GLenum, "target"), (GLfloat, "u1"), (GLfloat, "u2"), (GLint, "ustride"), (GLint, "uorder"), (GLfloat, "v1"), (GLfloat, "v2"), (GLint, "vstride"), (GLint, "vorder"), (Array(Const(GLfloat), "_glMap2f_size(target, ustride, uorder, vstride, vorder)"), "points")]),
    GlFunction(Void, "glMapGrid1d", [(GLint, "un"), (GLdouble, "u1"), (GLdouble, "u2")]),
    GlFunction(Void, "glMapGrid1f", [(GLint, "un"), (GLfloat, "u1"), (GLfloat, "u2")]),
    GlFunction(Void, "glMapGrid2d", [(GLint, "un"), (GLdouble, "u1"), (GLdouble, "u2"), (GLint, "vn"), (GLdouble, "v1"), (GLdouble, "v2")]),
    GlFunction(Void, "glMapGrid2f", [(GLint, "un"), (GLfloat, "u1"), (GLfloat, "u2"), (GLint, "vn"), (GLfloat, "v1"), (GLfloat, "v2")]),
    GlFunction(Void, "glEvalCoord1d", [(GLdouble, "u")]),
    GlFunction(Void, "glEvalCoord1dv", [(Pointer(Const(GLdouble)), "u")]),
    GlFunction(Void, "glEvalCoord1f", [(GLfloat, "u")]),
    GlFunction(Void, "glEvalCoord1fv", [(Pointer(Const(GLfloat)), "u")]),
    GlFunction(Void, "glEvalCoord2d", [(GLdouble, "u"), (GLdouble, "v")]),
    GlFunction(Void, "glEvalCoord2dv", [(Array(Const(GLdouble), 2), "u")]),
    GlFunction(Void, "glEvalCoord2f", [(GLfloat, "u"), (GLfloat, "v")]),
    GlFunction(Void, "glEvalCoord2fv", [(Array(Const(GLfloat), 2), "u")]),
    GlFunction(Void, "glEvalMesh1", [(GLenum, "mode"), (GLint, "i1"), (GLint, "i2")]),
    GlFunction(Void, "glEvalPoint1", [(GLint, "i")]),
    GlFunction(Void, "glEvalMesh2", [(GLenum, "mode"), (GLint, "i1"), (GLint, "i2"), (GLint, "j1"), (GLint, "j2")]),
    GlFunction(Void, "glEvalPoint2", [(GLint, "i"), (GLint, "j")]),
    GlFunction(Void, "glAlphaFunc", [(GLenum, "func"), (GLfloat, "ref")]),
    GlFunction(Void, "glPixelZoom", [(GLfloat, "xfactor"), (GLfloat, "yfactor")]),
    GlFunction(Void, "glPixelTransferf", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glPixelTransferi", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glPixelMapfv", [(GLenum, "map"), (GLsizei, "mapsize"), (Array(Const(GLfloat), "mapsize"), "values")]),
    GlFunction(Void, "glPixelMapuiv", [(GLenum, "map"), (GLsizei, "mapsize"), (Array(Const(GLuint), "mapsize"), "values")]),
    GlFunction(Void, "glPixelMapusv", [(GLenum, "map"), (GLsizei, "mapsize"), (Array(Const(GLushort), "mapsize"), "values")]),
    GlFunction(Void, "glCopyPixels", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "type")]),
    GlFunction(Void, "glDrawPixels", [(GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glDrawPixels_size(format, type, width, height)"), "pixels")]),
    GlFunction(Void, "glGetClipPlane", [(GLenum, "plane"), Out(Array(GLdouble, 4), "equation")], sideeffects=False),
    GlFunction(Void, "glGetLightfv", [(GLenum, "light"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetLightiv", [(GLenum, "light"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMapdv", [(GLenum, "target"), (GLenum, "query"), Out(Pointer(GLdouble), "v")], sideeffects=False),
    GlFunction(Void, "glGetMapfv", [(GLenum, "target"), (GLenum, "query"), Out(Pointer(GLfloat), "v")], sideeffects=False),
    GlFunction(Void, "glGetMapiv", [(GLenum, "target"), (GLenum, "query"), Out(Pointer(GLint), "v")], sideeffects=False),
    GlFunction(Void, "glGetMaterialfv", [(GLenum, "face"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMaterialiv", [(GLenum, "face"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetPixelMapfv", [(GLenum, "map"), Out(Pointer(GLfloat), "values")]),
    GlFunction(Void, "glGetPixelMapuiv", [(GLenum, "map"), Out(Pointer(GLuint), "values")]),
    GlFunction(Void, "glGetPixelMapusv", [(GLenum, "map"), Out(Pointer(GLushort), "values")]),
    GlFunction(Void, "glGetPolygonStipple", [Out(OpaquePointer(GLubyte), "mask")]),
    GlFunction(Void, "glGetTexEnvfv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexEnviv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexGendv", [(GLenum, "coord"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexGenfv", [(GLenum, "coord"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexGeniv", [(GLenum, "coord"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLboolean, "glIsList", [(GLlist, "list")], sideeffects=False),
    GlFunction(Void, "glFrustum", [(GLdouble, "left"), (GLdouble, "right"), (GLdouble, "bottom"), (GLdouble, "top"), (GLdouble, "zNear"), (GLdouble, "zFar")]),
    GlFunction(Void, "glLoadIdentity", []),
    GlFunction(Void, "glLoadMatrixf", [(Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glLoadMatrixd", [(Array(Const(GLdouble), 16), "m")]),
    GlFunction(Void, "glMatrixMode", [(GLenum, "mode")]),
    GlFunction(Void, "glMultMatrixf", [(Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glMultMatrixd", [(Array(Const(GLdouble), 16), "m")]),
    GlFunction(Void, "glOrtho", [(GLdouble, "left"), (GLdouble, "right"), (GLdouble, "bottom"), (GLdouble, "top"), (GLdouble, "zNear"), (GLdouble, "zFar")]),
    GlFunction(Void, "glPopMatrix", []),
    GlFunction(Void, "glPushMatrix", []),
    GlFunction(Void, "glRotated", [(GLdouble, "angle"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glRotatef", [(GLfloat, "angle"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glScaled", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glScalef", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glTranslated", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glTranslatef", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),

    # GL_VERSION_1_1
    GlFunction(Void, "glDrawArrays", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count")]),
    GlFunction(Void, "glDrawElements", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices")]),
    GlFunction(Void, "glGetPointerv", [(GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),
    GlFunction(Void, "glPolygonOffset", [(GLfloat, "factor"), (GLfloat, "units")]),
    GlFunction(Void, "glCopyTexImage1D", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLint, "border")]),
    GlFunction(Void, "glCopyTexImage2D", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border")]),
    GlFunction(Void, "glCopyTexSubImage1D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glCopyTexSubImage2D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glTexSubImage1D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage1D_size(format, type, width)"), "pixels")]),
    GlFunction(Void, "glTexSubImage2D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage2D_size(format, type, width, height)"), "pixels")]),
    GlFunction(Void, "glBindTexture", [(GLenum, "target"), (GLtexture, "texture")]),
    GlFunction(Void, "glDeleteTextures", [(GLsizei, "n"), (Array(Const(GLtexture), "n"), "textures")]),
    GlFunction(Void, "glGenTextures", [(GLsizei, "n"), Out(Array(GLtexture, "n"), "textures")]),
    GlFunction(GLboolean, "glIsTexture", [(GLtexture, "texture")], sideeffects=False),

    # GL_VERSION_1_1_DEPRECATED
    GlFunction(Void, "glArrayElement", [(GLint, "i")]),
    GlFunction(Void, "glColorPointer", [(size_bgra, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glDisableClientState", [(GLenum, "array")]),
    GlFunction(Void, "glEdgeFlagPointer", [(GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glEnableClientState", [(GLenum, "array")]),
    GlFunction(Void, "glIndexPointer", [(GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glInterleavedArrays", [(GLenum, "format"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glNormalPointer", [(GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glTexCoordPointer", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glVertexPointer", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(GLboolean, "glAreTexturesResident", [(GLsizei, "n"), (Array(Const(GLtexture), "n"), "textures"), Out(Array(GLboolean, "n"), "residences")], sideeffects=False),
    GlFunction(Void, "glPrioritizeTextures", [(GLsizei, "n"), (Array(Const(GLtexture), "n"), "textures"), (Array(Const(GLclampf), "n"), "priorities")]),
    GlFunction(Void, "glIndexub", [(GLubyte, "c")]),
    GlFunction(Void, "glIndexubv", [(Pointer(Const(GLubyte)), "c")]),
    GlFunction(Void, "glPopClientAttrib", []),
    GlFunction(Void, "glPushClientAttrib", [(GLbitfield_client_attrib, "mask")]),

    # GL_VERSION_1_2
    GlFunction(Void, "glBlendColor", [(GLfloat, "red"), (GLfloat, "green"), (GLfloat, "blue"), (GLfloat, "alpha")]),
    GlFunction(Void, "glBlendEquation", [(GLenum, "mode")]),
    GlFunction(Void, "glDrawRangeElements", [(GLenum_mode, "mode"), (GLuint, "start"), (GLuint, "end"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices")]),
    GlFunction(Void, "glTexImage3D", [(GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glTexSubImage3D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glCopyTexSubImage3D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),

    # GL_VERSION_1_2_DEPRECATED
    GlFunction(Void, "glColorTable", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glColorTable_size(format, type, width)"), "table")]),
    GlFunction(Void, "glColorTableParameterfv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glColorTableParameteriv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glCopyColorTable", [(GLenum, "target"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glGetColorTable", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetColorTable_size(target, format, type)"), "table")], sideeffects=False),
    GlFunction(Void, "glGetColorTableParameterfv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetColorTableParameteriv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glColorSubTable", [(GLenum, "target"), (GLsizei, "start"), (GLsizei, "count"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glColorSubTable_size(format, type, count)"), "data")]),
    GlFunction(Void, "glCopyColorSubTable", [(GLenum, "target"), (GLsizei, "start"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glConvolutionFilter1D", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glConvolutionFilter1D_size(format, type, width)"), "image")]),
    GlFunction(Void, "glConvolutionFilter2D", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glConvolutionFilter2D_size(format, type, width, height)"), "image")]),
    GlFunction(Void, "glConvolutionParameterf", [(GLenum, "target"), (GLenum, "pname"), (GLfloat, "params")]),
    GlFunction(Void, "glConvolutionParameterfv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glConvolutionParameteri", [(GLenum, "target"), (GLenum, "pname"), (GLint, "params")]),
    GlFunction(Void, "glConvolutionParameteriv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glCopyConvolutionFilter1D", [(GLenum, "target"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glCopyConvolutionFilter2D", [(GLenum, "target"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glGetConvolutionFilter", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetConvolutionFilter_size(target, format, type)"), "image")]),
    GlFunction(Void, "glGetConvolutionParameterfv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetConvolutionParameteriv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetSeparableFilter", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetSeparableFilter_size(target, format, type)"), "row"), Out(OpaqueBlob(GLvoid, "_glGetSeparableFilter_size(target, format, type)"), "column"), Out(GLpointer, "span")]),
    GlFunction(Void, "glSeparableFilter2D", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glConvolutionFilter1D_size(format, type, width)"), "row"), (Blob(Const(GLvoid), "_glConvolutionFilter1D_size(format, type, height)"), "column")]),
    GlFunction(Void, "glGetHistogram", [(GLenum, "target"), (GLboolean, "reset"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetHistogram_size(target, format, type)"), "values")]),
    GlFunction(Void, "glGetHistogramParameterfv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetHistogramParameteriv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMinmax", [(GLenum, "target"), (GLboolean, "reset"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetMinmax_size(target, format, type)"), "values")]),
    GlFunction(Void, "glGetMinmaxParameterfv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMinmaxParameteriv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glHistogram", [(GLenum, "target"), (GLsizei, "width"), (GLenum, "internalformat"), (GLboolean, "sink")]),
    GlFunction(Void, "glMinmax", [(GLenum, "target"), (GLenum, "internalformat"), (GLboolean, "sink")]),
    GlFunction(Void, "glResetHistogram", [(GLenum, "target")]),
    GlFunction(Void, "glResetMinmax", [(GLenum, "target")]),

    # GL_VERSION_1_3
    GlFunction(Void, "glActiveTexture", [(GLenum, "texture")]),
    GlFunction(Void, "glSampleCoverage", [(GLfloat, "value"), (GLboolean, "invert")]),
    GlFunction(Void, "glCompressedTexImage3D", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, internalformat, width, height, depth, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexImage2D", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, internalformat, width, height, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexImage1D", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, internalformat, width, 0, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexSubImage3D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, format, width, height, depth, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexSubImage2D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, format, width, height, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexSubImage1D", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, format, width, 0, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glGetCompressedTexImage", [(GLenum, "target"), (GLint, "level"), Out(OpaqueBlob(GLvoid, "_glGetCompressedTexImage_size(target, level)"), "img")]),

    # GL_VERSION_1_3_DEPRECATED
    GlFunction(Void, "glClientActiveTexture", [(GLenum, "texture")]),
    GlFunction(Void, "glMultiTexCoord1d", [(GLenum, "target"), (GLdouble, "s")]),
    GlFunction(Void, "glMultiTexCoord1dv", [(GLenum, "target"), (Pointer(Const(GLdouble)), "v")]),
    GlFunction(Void, "glMultiTexCoord1f", [(GLenum, "target"), (GLfloat, "s")]),
    GlFunction(Void, "glMultiTexCoord1fv", [(GLenum, "target"), (Pointer(Const(GLfloat)), "v")]),
    GlFunction(Void, "glMultiTexCoord1i", [(GLenum, "target"), (GLint, "s")]),
    GlFunction(Void, "glMultiTexCoord1iv", [(GLenum, "target"), (Pointer(Const(GLint)), "v")]),
    GlFunction(Void, "glMultiTexCoord1s", [(GLenum, "target"), (GLshort, "s")]),
    GlFunction(Void, "glMultiTexCoord1sv", [(GLenum, "target"), (Pointer(Const(GLshort)), "v")]),
    GlFunction(Void, "glMultiTexCoord2d", [(GLenum, "target"), (GLdouble, "s"), (GLdouble, "t")]),
    GlFunction(Void, "glMultiTexCoord2dv", [(GLenum, "target"), (Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord2f", [(GLenum, "target"), (GLfloat, "s"), (GLfloat, "t")]),
    GlFunction(Void, "glMultiTexCoord2fv", [(GLenum, "target"), (Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord2i", [(GLenum, "target"), (GLint, "s"), (GLint, "t")]),
    GlFunction(Void, "glMultiTexCoord2iv", [(GLenum, "target"), (Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord2s", [(GLenum, "target"), (GLshort, "s"), (GLshort, "t")]),
    GlFunction(Void, "glMultiTexCoord2sv", [(GLenum, "target"), (Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord3d", [(GLenum, "target"), (GLdouble, "s"), (GLdouble, "t"), (GLdouble, "r")]),
    GlFunction(Void, "glMultiTexCoord3dv", [(GLenum, "target"), (Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord3f", [(GLenum, "target"), (GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r")]),
    GlFunction(Void, "glMultiTexCoord3fv", [(GLenum, "target"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord3i", [(GLenum, "target"), (GLint, "s"), (GLint, "t"), (GLint, "r")]),
    GlFunction(Void, "glMultiTexCoord3iv", [(GLenum, "target"), (Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord3s", [(GLenum, "target"), (GLshort, "s"), (GLshort, "t"), (GLshort, "r")]),
    GlFunction(Void, "glMultiTexCoord3sv", [(GLenum, "target"), (Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord4d", [(GLenum, "target"), (GLdouble, "s"), (GLdouble, "t"), (GLdouble, "r"), (GLdouble, "q")]),
    GlFunction(Void, "glMultiTexCoord4dv", [(GLenum, "target"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glMultiTexCoord4f", [(GLenum, "target"), (GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r"), (GLfloat, "q")]),
    GlFunction(Void, "glMultiTexCoord4fv", [(GLenum, "target"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glMultiTexCoord4i", [(GLenum, "target"), (GLint, "s"), (GLint, "t"), (GLint, "r"), (GLint, "q")]),
    GlFunction(Void, "glMultiTexCoord4iv", [(GLenum, "target"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glMultiTexCoord4s", [(GLenum, "target"), (GLshort, "s"), (GLshort, "t"), (GLshort, "r"), (GLshort, "q")]),
    GlFunction(Void, "glMultiTexCoord4sv", [(GLenum, "target"), (Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glLoadTransposeMatrixf", [(Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glLoadTransposeMatrixd", [(Array(Const(GLdouble), 16), "m")]),
    GlFunction(Void, "glMultTransposeMatrixf", [(Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glMultTransposeMatrixd", [(Array(Const(GLdouble), 16), "m")]),

    # GL_VERSION_1_4
    GlFunction(Void, "glBlendFuncSeparate", [(GLenum, "sfactorRGB"), (GLenum, "dfactorRGB"), (GLenum, "sfactorAlpha"), (GLenum, "dfactorAlpha")]),
    GlFunction(Void, "glMultiDrawArrays", [(GLenum_mode, "mode"), (Array(Const(GLint), "drawcount"), "first"), (Array(Const(GLsizei), "drawcount"), "count"), (GLsizei, "drawcount")]),
    GlFunction(Void, "glMultiDrawElements", [(GLenum_mode, "mode"), (Array(Const(GLsizei), "drawcount"), "count"), (GLenum, "type"), (Array(Const(GLindexBuffer("count[{i}]", "type")), "drawcount"), "indices"), (GLsizei, "drawcount")]),
    GlFunction(Void, "glPointParameterf", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glPointParameterfv", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glPointParameteri", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glPointParameteriv", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),

    # GL_VERSION_1_4_DEPRECATED
    GlFunction(Void, "glFogCoordf", [(GLfloat, "coord")]),
    GlFunction(Void, "glFogCoordfv", [(Pointer(Const(GLfloat)), "coord")]),
    GlFunction(Void, "glFogCoordd", [(GLdouble, "coord")]),
    GlFunction(Void, "glFogCoorddv", [(Pointer(Const(GLdouble)), "coord")]),
    GlFunction(Void, "glFogCoordPointer", [(GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glSecondaryColor3b", [(GLbyte, "red"), (GLbyte, "green"), (GLbyte, "blue")]),
    GlFunction(Void, "glSecondaryColor3bv", [(Array(Const(GLbyte), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3d", [(GLdouble, "red"), (GLdouble, "green"), (GLdouble, "blue")]),
    GlFunction(Void, "glSecondaryColor3dv", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3f", [(GLfloat, "red"), (GLfloat, "green"), (GLfloat, "blue")]),
    GlFunction(Void, "glSecondaryColor3fv", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3i", [(GLint, "red"), (GLint, "green"), (GLint, "blue")]),
    GlFunction(Void, "glSecondaryColor3iv", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3s", [(GLshort, "red"), (GLshort, "green"), (GLshort, "blue")]),
    GlFunction(Void, "glSecondaryColor3sv", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3ub", [(GLubyte, "red"), (GLubyte, "green"), (GLubyte, "blue")]),
    GlFunction(Void, "glSecondaryColor3ubv", [(Array(Const(GLubyte), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3ui", [(GLuint, "red"), (GLuint, "green"), (GLuint, "blue")]),
    GlFunction(Void, "glSecondaryColor3uiv", [(Array(Const(GLuint), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3us", [(GLushort, "red"), (GLushort, "green"), (GLushort, "blue")]),
    GlFunction(Void, "glSecondaryColor3usv", [(Array(Const(GLushort), 3), "v")]),
    GlFunction(Void, "glSecondaryColorPointer", [(size_bgra, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glWindowPos2d", [(GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glWindowPos2dv", [(Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glWindowPos2f", [(GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glWindowPos2fv", [(Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glWindowPos2i", [(GLint, "x"), (GLint, "y")]),
    GlFunction(Void, "glWindowPos2iv", [(Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glWindowPos2s", [(GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glWindowPos2sv", [(Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glWindowPos3d", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glWindowPos3dv", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glWindowPos3f", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glWindowPos3fv", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glWindowPos3i", [(GLint, "x"), (GLint, "y"), (GLint, "z")]),
    GlFunction(Void, "glWindowPos3iv", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glWindowPos3s", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glWindowPos3sv", [(Array(Const(GLshort), 3), "v")]),

    # GL_VERSION_1_5
    GlFunction(Void, "glGenQueries", [(GLsizei, "n"), Out(Array(GLquery, "n"), "ids")]),
    GlFunction(Void, "glDeleteQueries", [(GLsizei, "n"), (Array(Const(GLquery), "n"), "ids")]),
    GlFunction(GLboolean, "glIsQuery", [(GLquery, "id")], sideeffects=False),
    GlFunction(Void, "glBeginQuery", [(GLenum, "target"), (GLquery, "id")]),
    GlFunction(Void, "glEndQuery", [(GLenum, "target")]),
    GlFunction(Void, "glGetQueryiv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetQueryObjectiv", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjectuiv", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glBindBuffer", [(GLenum, "target"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glDeleteBuffers", [(GLsizei, "n"), (Array(Const(GLbuffer), "n"), "buffers")]),
    GlFunction(Void, "glGenBuffers", [(GLsizei, "n"), Out(Array(GLbuffer, "n"), "buffers")]),
    GlFunction(GLboolean, "glIsBuffer", [(GLbuffer, "buffer")], sideeffects=False),
    GlFunction(Void, "glBufferData", [(GLenum, "target"), (GLsizeiptr, "size"), (Blob(Const(GLvoid), "size"), "data"), (GLenum, "usage")]),
    GlFunction(Void, "glBufferSubData", [(GLenum, "target"), (GLintptr, "offset"), (GLsizeiptr, "size"), (Blob(Const(GLvoid), "size"), "data")]),
    GlFunction(Void, "glGetBufferSubData", [(GLenum, "target"), (GLintptr, "offset"), (GLsizeiptr, "size"), Out(OpaqueBlob(GLvoid, "size"), "data")], sideeffects=False),
    GlFunction(GLmap, "glMapBuffer", [(GLenum, "target"), (GLenum, "access")]),
    GlFunction(GLboolean, "glUnmapBuffer", [(GLenum, "target")]),
    GlFunction(Void, "glGetBufferParameteriv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetBufferPointerv", [(GLenum, "target"), (GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),

    # GL_VERSION_2_0
    GlFunction(Void, "glBlendEquationSeparate", [(GLenum, "modeRGB"), (GLenum, "modeAlpha")]),
    GlFunction(Void, "glDrawBuffers", [(GLsizei, "n"), (Array(Const(GLenum), "n"), "bufs")]),
    GlFunction(Void, "glStencilOpSeparate", [(GLenum, "face"), (GLenum, "sfail"), (GLenum, "dpfail"), (GLenum, "dppass")]),
    GlFunction(Void, "glStencilFuncSeparate", [(GLenum, "face"), (GLenum, "func"), (GLint, "ref"), (GLuint, "mask")]),
    GlFunction(Void, "glStencilMaskSeparate", [(GLenum, "face"), (GLuint, "mask")]),
    GlFunction(Void, "glAttachShader", [(GLprogram, "program"), (GLshader, "shader")]),
    GlFunction(Void, "glBindAttribLocation", [(GLprogram, "program"), (GLuint, "index"), (GLstringConst, "name")]),
    GlFunction(Void, "glCompileShader", [(GLshader, "shader")]),
    GlFunction(GLprogram, "glCreateProgram", []),
    GlFunction(GLshader, "glCreateShader", [(GLenum, "type")]),
    GlFunction(Void, "glDeleteProgram", [(GLprogram, "program")]),
    GlFunction(Void, "glDeleteShader", [(GLshader, "shader")]),
    GlFunction(Void, "glDetachShader", [(GLprogram, "program"), (GLshader, "shader")]),
    GlFunction(Void, "glDisableVertexAttribArray", [(GLuint, "index")]),
    GlFunction(Void, "glEnableVertexAttribArray", [(GLuint, "index")]),
    GlFunction(Void, "glGetActiveAttrib", [(GLprogram, "program"), (GLuint, "index"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLint), "size"), Out(Pointer(GLenum), "type"), OutGlString(GLchar, "length", "name")], sideeffects=False),
    GlFunction(Void, "glGetActiveUniform", [(GLprogram, "program"), (GLuint, "index"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLint), "size"), Out(Pointer(GLenum), "type"), OutGlString(GLchar, "length", "name")], sideeffects=False),
    GlFunction(Void, "glGetAttachedShaders", [(GLprogram, "program"), (GLsizei, "maxCount"), Out(Pointer(GLsizei), "count"), Out(Array(GLuint, "(count ? *count : maxCount)"), "obj")], sideeffects=False),
    GlFunction(GLint, "glGetAttribLocation", [(GLprogram, "program"), (GLstringConst, "name")]),
    GlFunction(Void, "glGetProgramiv", [(GLprogram, "program"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramInfoLog", [(GLprogram, "program"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "infoLog")], sideeffects=False),
    GlFunction(Void, "glGetShaderiv", [(GLshader, "shader"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetShaderInfoLog", [(GLshader, "shader"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "infoLog")], sideeffects=False),
    GlFunction(Void, "glGetShaderSource", [(GLshader, "shader"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "source")], sideeffects=False),
    GlFunction(GLlocation, "glGetUniformLocation", [(GLprogram, "program"), (GLstringConst, "name")]),
    GlFunction(Void, "glGetUniformfv", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaquePointer(GLfloat), "params")], sideeffects=False),
    GlFunction(Void, "glGetUniformiv", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaquePointer(GLint), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribdv", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribfv", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribiv", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribPointerv", [(GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLpointer), "pointer")], sideeffects=False),
    GlFunction(GLboolean, "glIsProgram", [(GLprogram, "program")], sideeffects=False),
    GlFunction(GLboolean, "glIsShader", [(GLshader, "shader")], sideeffects=False),
    GlFunction(Void, "glLinkProgram", [(GLprogram, "program")]),
    GlFunction(Void, "glShaderSource", [(GLshader, "shader"), (GLsizei, "count"), (Array(Const(String(Const(GLchar), "_glShaderSource_length(string, length, {i})")), "count"), "string"), (Array(Const(GLint), "count"), "length")]),
    GlFunction(Void, "glUseProgram", [(GLprogram, "program")]),
    GlFunction(Void, "glUniform1f", [(GLlocation, "location"), (GLfloat, "v0")]),
    GlFunction(Void, "glUniform2f", [(GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1")]),
    GlFunction(Void, "glUniform3f", [(GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1"), (GLfloat, "v2")]),
    GlFunction(Void, "glUniform4f", [(GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1"), (GLfloat, "v2"), (GLfloat, "v3")]),
    GlFunction(Void, "glUniform1i", [(GLlocation, "location"), (GLint, "v0")]),
    GlFunction(Void, "glUniform2i", [(GLlocation, "location"), (GLint, "v0"), (GLint, "v1")]),
    GlFunction(Void, "glUniform3i", [(GLlocation, "location"), (GLint, "v0"), (GLint, "v1"), (GLint, "v2")]),
    GlFunction(Void, "glUniform4i", [(GLlocation, "location"), (GLint, "v0"), (GLint, "v1"), (GLint, "v2"), (GLint, "v3")]),
    GlFunction(Void, "glUniform1fv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count"), "value")]),
    GlFunction(Void, "glUniform2fv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*2"), "value")]),
    GlFunction(Void, "glUniform3fv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*3"), "value")]),
    GlFunction(Void, "glUniform4fv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "value")]),
    GlFunction(Void, "glUniform1iv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count"), "value")]),
    GlFunction(Void, "glUniform2iv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*2"), "value")]),
    GlFunction(Void, "glUniform3iv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*3"), "value")]),
    GlFunction(Void, "glUniform4iv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "value")]),
    GlFunction(Void, "glUniformMatrix2fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*2"), "value")]),
    GlFunction(Void, "glUniformMatrix3fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*3"), "value")]),
    GlFunction(Void, "glUniformMatrix4fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*4"), "value")]),
    GlFunction(Void, "glValidateProgram", [(GLprogram, "program")]),
    GlFunction(Void, "glVertexAttrib1d", [(GLuint, "index"), (GLdouble, "x")]),
    GlFunction(Void, "glVertexAttrib1dv", [(GLuint, "index"), (Pointer(Const(GLdouble)), "v")]),
    GlFunction(Void, "glVertexAttrib1f", [(GLuint, "index"), (GLfloat, "x")]),
    GlFunction(Void, "glVertexAttrib1fv", [(GLuint, "index"), (Pointer(Const(GLfloat)), "v")]),
    GlFunction(Void, "glVertexAttrib1s", [(GLuint, "index"), (GLshort, "x")]),
    GlFunction(Void, "glVertexAttrib1sv", [(GLuint, "index"), (Pointer(Const(GLshort)), "v")]),
    GlFunction(Void, "glVertexAttrib2d", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glVertexAttrib2dv", [(GLuint, "index"), (Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glVertexAttrib2f", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glVertexAttrib2fv", [(GLuint, "index"), (Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glVertexAttrib2s", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glVertexAttrib2sv", [(GLuint, "index"), (Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glVertexAttrib3d", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glVertexAttrib3dv", [(GLuint, "index"), (Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glVertexAttrib3f", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glVertexAttrib3fv", [(GLuint, "index"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glVertexAttrib3s", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glVertexAttrib3sv", [(GLuint, "index"), (Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glVertexAttrib4Nbv", [(GLuint, "index"), (Array(Const(GLbyte), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4Niv", [(GLuint, "index"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4Nsv", [(GLuint, "index"), (Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4Nub", [(GLuint, "index"), (GLubyte, "x"), (GLubyte, "y"), (GLubyte, "z"), (GLubyte, "w")]),
    GlFunction(Void, "glVertexAttrib4Nubv", [(GLuint, "index"), (Array(Const(GLubyte), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4Nuiv", [(GLuint, "index"), (Array(Const(GLuint), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4Nusv", [(GLuint, "index"), (Array(Const(GLushort), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4bv", [(GLuint, "index"), (Array(Const(GLbyte), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4d", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glVertexAttrib4dv", [(GLuint, "index"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4f", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glVertexAttrib4fv", [(GLuint, "index"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4iv", [(GLuint, "index"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4s", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y"), (GLshort, "z"), (GLshort, "w")]),
    GlFunction(Void, "glVertexAttrib4sv", [(GLuint, "index"), (Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4ubv", [(GLuint, "index"), (Array(Const(GLubyte), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4uiv", [(GLuint, "index"), (Array(Const(GLuint), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4usv", [(GLuint, "index"), (Array(Const(GLushort), 4), "v")]),
    GlFunction(Void, "glVertexAttribPointer", [(GLuint, "index"), (size_bgra, "size"), (GLenum, "type"), (GLboolean, "normalized"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),

    # GL_VERSION_2_1
    GlFunction(Void, "glUniformMatrix2x3fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*3"), "value")]),
    GlFunction(Void, "glUniformMatrix3x2fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*2"), "value")]),
    GlFunction(Void, "glUniformMatrix2x4fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*4"), "value")]),
    GlFunction(Void, "glUniformMatrix4x2fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*2"), "value")]),
    GlFunction(Void, "glUniformMatrix3x4fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*4"), "value")]),
    GlFunction(Void, "glUniformMatrix4x3fv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*3"), "value")]),

    # GL_VERSION_3_0
    GlFunction(Void, "glColorMaski", [(GLuint, "index"), (GLboolean, "r"), (GLboolean, "g"), (GLboolean, "b"), (GLboolean, "a")]),
    GlFunction(Void, "glGetBooleani_v", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLboolean, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetIntegeri_v", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLint, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glEnablei", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(Void, "glDisablei", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(GLboolean, "glIsEnabledi", [(GLenum, "target"), (GLuint, "index")], sideeffects=False),
    GlFunction(Void, "glBeginTransformFeedback", [(GLenum_mode, "primitiveMode")]),
    GlFunction(Void, "glEndTransformFeedback", []),
    GlFunction(Void, "glBindBufferRange", [(GLenum, "target"), (GLuint, "index"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size")]),
    GlFunction(Void, "glBindBufferBase", [(GLenum, "target"), (GLuint, "index"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glTransformFeedbackVaryings", [(GLprogram, "program"), (GLsizei, "count"), (Array(Const(GLstringConst), "count"), "varyings"), (GLenum, "bufferMode")]),
    GlFunction(Void, "glGetTransformFeedbackVarying", [(GLprogram, "program"), (GLuint, "index"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLsizei), "size"), Out(Pointer(GLenum), "type"), OutGlString(GLchar, "length", "name")], sideeffects=False),
    GlFunction(Void, "glClampColor", [(GLenum, "target"), (GLenum, "clamp")]),
    GlFunction(Void, "glBeginConditionalRender", [(GLquery, "id"), (GLenum, "mode")]),
    GlFunction(Void, "glEndConditionalRender", []),
    GlFunction(Void, "glVertexAttribIPointer", [(GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glGetVertexAttribIiv", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribIuiv", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glVertexAttribI1i", [(GLuint, "index"), (GLint, "x")]),
    GlFunction(Void, "glVertexAttribI2i", [(GLuint, "index"), (GLint, "x"), (GLint, "y")]),
    GlFunction(Void, "glVertexAttribI3i", [(GLuint, "index"), (GLint, "x"), (GLint, "y"), (GLint, "z")]),
    GlFunction(Void, "glVertexAttribI4i", [(GLuint, "index"), (GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glVertexAttribI1ui", [(GLuint, "index"), (GLuint, "x")]),
    GlFunction(Void, "glVertexAttribI2ui", [(GLuint, "index"), (GLuint, "x"), (GLuint, "y")]),
    GlFunction(Void, "glVertexAttribI3ui", [(GLuint, "index"), (GLuint, "x"), (GLuint, "y"), (GLuint, "z")]),
    GlFunction(Void, "glVertexAttribI4ui", [(GLuint, "index"), (GLuint, "x"), (GLuint, "y"), (GLuint, "z"), (GLuint, "w")]),
    GlFunction(Void, "glVertexAttribI1iv", [(GLuint, "index"), (Pointer(Const(GLint)), "v")]),
    GlFunction(Void, "glVertexAttribI2iv", [(GLuint, "index"), (Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glVertexAttribI3iv", [(GLuint, "index"), (Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glVertexAttribI4iv", [(GLuint, "index"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glVertexAttribI1uiv", [(GLuint, "index"), (Pointer(Const(GLuint)), "v")]),
    GlFunction(Void, "glVertexAttribI2uiv", [(GLuint, "index"), (Array(Const(GLuint), 2), "v")]),
    GlFunction(Void, "glVertexAttribI3uiv", [(GLuint, "index"), (Array(Const(GLuint), 3), "v")]),
    GlFunction(Void, "glVertexAttribI4uiv", [(GLuint, "index"), (Array(Const(GLuint), 4), "v")]),
    GlFunction(Void, "glVertexAttribI4bv", [(GLuint, "index"), (Array(Const(GLbyte), 4), "v")]),
    GlFunction(Void, "glVertexAttribI4sv", [(GLuint, "index"), (Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glVertexAttribI4ubv", [(GLuint, "index"), (Array(Const(GLubyte), 4), "v")]),
    GlFunction(Void, "glVertexAttribI4usv", [(GLuint, "index"), (Array(Const(GLushort), 4), "v")]),
    GlFunction(Void, "glGetUniformuiv", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaqueArray(GLuint, "_glGetUniformuiv_size(program, location)"), "params")], sideeffects=False),
    GlFunction(Void, "glBindFragDataLocation", [(GLprogram, "program"), (GLuint, "color"), (GLstringConst, "name")]),
    GlFunction(GLint, "glGetFragDataLocation", [(GLprogram, "program"), (GLstringConst, "name")], sideeffects=False),
    GlFunction(Void, "glUniform1ui", [(GLlocation, "location"), (GLuint, "v0")]),
    GlFunction(Void, "glUniform2ui", [(GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1")]),
    GlFunction(Void, "glUniform3ui", [(GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1"), (GLuint, "v2")]),
    GlFunction(Void, "glUniform4ui", [(GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1"), (GLuint, "v2"), (GLuint, "v3")]),
    GlFunction(Void, "glUniform1uiv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "value")]),
    GlFunction(Void, "glUniform2uiv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*2"), "value")]),
    GlFunction(Void, "glUniform3uiv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*3"), "value")]),
    GlFunction(Void, "glUniform4uiv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*4"), "value")]),
    GlFunction(Void, "glTexParameterIiv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexParameterIuiv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLuint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetTexParameterIiv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexParameterIuiv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glClearBufferiv", [(GLenum, "buffer"), (GLint, "drawbuffer"), (Array(Const(GLint), "_glClearBuffer_size(buffer)"), "value")]),
    GlFunction(Void, "glClearBufferuiv", [(GLenum, "buffer"), (GLint, "drawbuffer"), (Array(Const(GLuint), "_glClearBuffer_size(buffer)"), "value")]),
    GlFunction(Void, "glClearBufferfv", [(GLenum, "buffer"), (GLint, "drawbuffer"), (Array(Const(GLfloat), "_glClearBuffer_size(buffer)"), "value")]),
    GlFunction(Void, "glClearBufferfi", [(GLenum, "buffer"), (GLint, "drawbuffer"), (GLfloat, "depth"), (GLint, "stencil")]),
    GlFunction(String(Const(GLubyte)), "glGetStringi", [(GLenum, "name"), (GLuint, "index")], sideeffects=False),

    # GL_VERSION_3_1
    GlFunction(Void, "glDrawArraysInstanced", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count"), (GLsizei, "instancecount")]),
    GlFunction(Void, "glDrawElementsInstanced", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount")]),
    GlFunction(Void, "glTexBuffer", [(GLenum, "target"), (GLenum, "internalformat"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glPrimitiveRestartIndex", [(GLuint, "index")]),

    # GL_VERSION_3_2
    GlFunction(Void, "glGetInteger64i_v", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLint64, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetBufferParameteri64v", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint64, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glFramebufferTexture", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level")]),

    # GL_VERSION_3_3
    GlFunction(Void, "glVertexAttribDivisor", [(GLuint, "index"), (GLuint, "divisor")]),

    # GL_VERSION_4_0
    GlFunction(Void, "glMinSampleShading", [(GLfloat, "value")]),
    GlFunction(Void, "glBlendEquationi", [(GLuint, "buf"), (GLenum, "mode")]),
    GlFunction(Void, "glBlendEquationSeparatei", [(GLuint, "buf"), (GLenum, "modeRGB"), (GLenum, "modeAlpha")]),
    GlFunction(Void, "glBlendFunci", [(GLuint, "buf"), (GLenum, "src"), (GLenum, "dst")]),
    GlFunction(Void, "glBlendFuncSeparatei", [(GLuint, "buf"), (GLenum, "srcRGB"), (GLenum, "dstRGB"), (GLenum, "srcAlpha"), (GLenum, "dstAlpha")]),

    # GL_VERSION_4_1

    # GL_VERSION_4_2

    # GL_VERSION_4_3

    # GL_VERSION_4_4

    # GL_VERSION_4_5
    GlFunction(Void, "glGetnCompressedTexImage", [(GLenum, "target"), (GLint, "lod"), (GLsizei, "bufSize"), Out(OpaqueBlob(Void, "bufSize"), "pixels")]),
    GlFunction(Void, "glGetnTexImage", [(GLenum, "target"), (GLint, "level"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(Void, "bufSize"), "pixels")]),
    GlFunction(Void, "glGetnUniformdv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLdouble, "bufSize"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnMapdv", [(GLenum, "target"), (GLenum, "query"), (GLsizei, "bufSize"), Out(Array(GLdouble, "bufSize"), "v")], sideeffects=False),
    GlFunction(Void, "glGetnMapfv", [(GLenum, "target"), (GLenum, "query"), (GLsizei, "bufSize"), Out(Array(GLfloat, "bufSize"), "v")], sideeffects=False),
    GlFunction(Void, "glGetnMapiv", [(GLenum, "target"), (GLenum, "query"), (GLsizei, "bufSize"), Out(Array(GLint, "bufSize"), "v")], sideeffects=False),
    GlFunction(Void, "glGetnPixelMapfv", [(GLenum, "map"), (GLsizei, "bufSize"), Out(Array(GLfloat, "bufSize"), "values")]),
    GlFunction(Void, "glGetnPixelMapuiv", [(GLenum, "map"), (GLsizei, "bufSize"), Out(Array(GLuint, "bufSize"), "values")]),
    GlFunction(Void, "glGetnPixelMapusv", [(GLenum, "map"), (GLsizei, "bufSize"), Out(Array(GLushort, "bufSize"), "values")]),
    GlFunction(Void, "glGetnPolygonStipple", [(GLsizei, "bufSize"), Out(Array(GLubyte, "bufSize"), "pattern")]),
    GlFunction(Void, "glGetnColorTable", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(Void, "bufSize"), "table")], sideeffects=False),
    GlFunction(Void, "glGetnConvolutionFilter", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(Void, "bufSize"), "image")]),
    GlFunction(Void, "glGetnSeparableFilter", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "rowBufSize"), Out(OpaqueBlob(Void, "rowBufSize"), "row"), (GLsizei, "columnBufSize"), Out(OpaqueBlob(Void, "columnBufSize"), "column"), Out(GLpointer, "span")]),
    GlFunction(Void, "glGetnHistogram", [(GLenum, "target"), (GLboolean, "reset"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(Void, "bufSize"), "values")]),
    GlFunction(Void, "glGetnMinmax", [(GLenum, "target"), (GLboolean, "reset"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(Void, "bufSize"), "values")]),

    # GL_VERSION_4_6
    GlFunction(Void, "glSpecializeShader", [(GLshader, "shader"), (GLstringConst, "pEntryPoint"), (GLuint, "numSpecializationConstants"), (Array(Const(GLuint), "numSpecializationConstants"), "pConstantIndex"), (Array(Const(GLuint), "numSpecializationConstants"), "pConstantValue")]),
    GlFunction(Void, "glMultiDrawArraysIndirectCount", [(GLenum_mode, "mode"), (GLdrawArraysIndirectBuffer("maxdrawcount", "stride"), "indirect"), (GLintptr, "drawcount"), (GLsizei, "maxdrawcount"), (GLsizei, "stride")]),
    GlFunction(Void, "glMultiDrawElementsIndirectCount", [(GLenum_mode, "mode"), (GLenum, "type"), (GLdrawElementsIndirectBuffer("maxdrawcount", "stride"), "indirect"), (GLintptr, "drawcount"), (GLsizei, "maxdrawcount"), (GLsizei, "stride")]),

    # GL_VERSION_ES_CM_1_0
    GlFunction(Void, "glClipPlanef", [(GLenum, "plane"), (Array(Const(GLfloat), 4), "equation")]),
    GlFunction(Void, "glFrustumf", [(GLfloat, "left"), (GLfloat, "right"), (GLfloat, "bottom"), (GLfloat, "top"), (GLfloat, "zNear"), (GLfloat, "zFar")]),
    GlFunction(Void, "glGetClipPlanef", [(GLenum, "plane"), Out(Array(GLfloat, 4), "equation")], sideeffects=False),
    GlFunction(Void, "glOrthof", [(GLfloat, "left"), (GLfloat, "right"), (GLfloat, "bottom"), (GLfloat, "top"), (GLfloat, "zNear"), (GLfloat, "zFar")]),
    GlFunction(Void, "glAlphaFuncx", [(GLenum, "func"), (GLclampx, "ref")]),
    GlFunction(Void, "glClearColorx", [(GLclampx, "red"), (GLclampx, "green"), (GLclampx, "blue"), (GLclampx, "alpha")]),
    GlFunction(Void, "glClearDepthx", [(GLclampx, "depth")]),
    GlFunction(Void, "glClipPlanex", [(GLenum, "plane"), (Array(Const(GLfixed), 4), "equation")]),
    GlFunction(Void, "glColor4x", [(GLfixed, "red"), (GLfixed, "green"), (GLfixed, "blue"), (GLfixed, "alpha")]),
    GlFunction(Void, "glDepthRangex", [(GLclampx, "zNear"), (GLclampx, "zFar")]),
    GlFunction(Void, "glFogx", [(GLenum, "pname"), (GLfixed, "param")]),
    GlFunction(Void, "glFogxv", [(GLenum, "pname"), (Array(Const(GLfixed), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glFrustumx", [(GLfixed, "left"), (GLfixed, "right"), (GLfixed, "bottom"), (GLfixed, "top"), (GLfixed, "zNear"), (GLfixed, "zFar")]),
    GlFunction(Void, "glGetClipPlanex", [(GLenum, "plane"), Out(Array(GLfixed, 4), "equation")], sideeffects=False),
    GlFunction(Void, "glGetFixedv", [(GLenum, "pname"), Out(Array(GLfixed, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetLightxv", [(GLenum, "light"), (GLenum, "pname"), Out(Array(GLfixed, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMaterialxv", [(GLenum, "face"), (GLenum, "pname"), Out(Array(GLfixed, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexEnvxv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfixed, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexParameterxv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfixed, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glLightModelx", [(GLenum, "pname"), (GLfixed, "param")]),
    GlFunction(Void, "glLightModelxv", [(GLenum, "pname"), (Array(Const(GLfixed), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glLightx", [(GLenum, "light"), (GLenum, "pname"), (GLfixed, "param")]),
    GlFunction(Void, "glLightxv", [(GLenum, "light"), (GLenum, "pname"), (Array(Const(GLfixed), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glLineWidthx", [(GLfixed, "width")]),
    GlFunction(Void, "glLoadMatrixx", [(Array(Const(GLfixed), 16), "m")]),
    GlFunction(Void, "glMaterialx", [(GLenum, "face"), (GLenum, "pname"), (GLfixed, "param")]),
    GlFunction(Void, "glMaterialxv", [(GLenum, "face"), (GLenum, "pname"), (Array(Const(GLfixed), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultMatrixx", [(Array(Const(GLfixed), 16), "m")]),
    GlFunction(Void, "glMultiTexCoord4x", [(GLenum, "target"), (GLfixed, "s"), (GLfixed, "t"), (GLfixed, "r"), (GLfixed, "q")]),
    GlFunction(Void, "glNormal3x", [(GLfixed, "nx"), (GLfixed, "ny"), (GLfixed, "nz")]),
    GlFunction(Void, "glOrthox", [(GLfixed, "left"), (GLfixed, "right"), (GLfixed, "bottom"), (GLfixed, "top"), (GLfixed, "zNear"), (GLfixed, "zFar")]),
    GlFunction(Void, "glPointParameterx", [(GLenum, "pname"), (GLfixed, "param")]),
    GlFunction(Void, "glPointParameterxv", [(GLenum, "pname"), (Array(Const(GLfixed), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glPointSizex", [(GLfixed, "size")]),
    GlFunction(Void, "glPolygonOffsetx", [(GLfixed, "factor"), (GLfixed, "units")]),
    GlFunction(Void, "glRotatex", [(GLfixed, "angle"), (GLfixed, "x"), (GLfixed, "y"), (GLfixed, "z")]),
    GlFunction(Void, "glSampleCoveragex", [(GLclampx, "value"), (GLboolean, "invert")]),
    GlFunction(Void, "glScalex", [(GLfixed, "x"), (GLfixed, "y"), (GLfixed, "z")]),
    GlFunction(Void, "glTexEnvx", [(GLenum, "target"), (GLenum, "pname"), (GLfixed, "param")]),
    GlFunction(Void, "glTexEnvxv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfixed), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexParameterx", [(GLenum, "target"), (GLenum, "pname"), (GLfixed, "param")]),
    GlFunction(Void, "glTexParameterxv", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfixed), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTranslatex", [(GLfixed, "x"), (GLfixed, "y"), (GLfixed, "z")]),

    # GL_ES_VERSION_2_0

    # GL_ES_VERSION_3_0

    # GL_ES_VERSION_3_1

    # GL_ES_VERSION_3_2
    GlFunction(Void, "glBlendBarrier", []),
    GlFunction(Void, "glPrimitiveBoundingBox", [(GLfloat, "minX"), (GLfloat, "minY"), (GLfloat, "minZ"), (GLfloat, "minW"), (GLfloat, "maxX"), (GLfloat, "maxY"), (GLfloat, "maxZ"), (GLfloat, "maxW")]),
    
    # GL_3DFX_tbuffer
    GlFunction(Void, "glTbufferMask3DFX", [(GLuint, "mask")]),

    # GL_AMD_debug_output
    GlFunction(Void, "glDebugMessageEnableAMD", [(GLenum, "category"), (GLenum, "severity"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "ids"), (GLboolean, "enabled")], sideeffects=True),
    GlFunction(Void, "glDebugMessageInsertAMD", [(GLenum, "category"), (GLenum, "severity"), (GLuint, "id"), (GLsizei, "length"), InGlString(GLchar, "length", "buf")], sideeffects=True),
    GlFunction(Void, "glDebugMessageCallbackAMD", [(GLDEBUGPROCAMD, "callback"), (GLpointer, "userParam")], sideeffects=False),
    GlFunction(GLuint, "glGetDebugMessageLogAMD", [(GLuint, "count"), (GLsizei, "bufsize"), Out(Array(GLenum, "count"), "categories"), Out(Array(GLuint, "count"), "severities"), Out(Array(GLuint, "count"), "ids"), Out(Array(GLsizei, "count"), "lengths"), Out(String(GLchar, "_glGetDebugMessageLog_length(message, lengths, _result)"), "message")], sideeffects=False, fail=0),

    # GL_AMD_draw_buffers_blend
    GlFunction(Void, "glBlendFuncIndexedAMD", [(GLuint, "buf"), (GLenum, "src"), (GLenum, "dst")]),
    GlFunction(Void, "glBlendFuncSeparateIndexedAMD", [(GLuint, "buf"), (GLenum, "srcRGB"), (GLenum, "dstRGB"), (GLenum, "srcAlpha"), (GLenum, "dstAlpha")]),
    GlFunction(Void, "glBlendEquationIndexedAMD", [(GLuint, "buf"), (GLenum, "mode")]),
    GlFunction(Void, "glBlendEquationSeparateIndexedAMD", [(GLuint, "buf"), (GLenum, "modeRGB"), (GLenum, "modeAlpha")]),

    # GL_AMD_interleaved_elements
    GlFunction(Void, "glVertexAttribParameteriAMD", [(GLuint, "index"), (GLenum, "pname"), (GLint, "param")]),

    # GL_AMD_multi_draw_indirect
    GlFunction(Void, "glMultiDrawArraysIndirectAMD", [(GLenum_mode, "mode"), (GLpointerConst, "indirect"), (GLsizei, "drawcount"), (GLsizei, "stride")]),
    GlFunction(Void, "glMultiDrawElementsIndirectAMD", [(GLenum_mode, "mode"), (GLenum, "type"), (GLpointerConst, "indirect"), (GLsizei, "drawcount"), (GLsizei, "stride")]),

    # GL_AMD_name_gen_delete
    GlFunction(Void, "glGenNamesAMD", [(GLenum, "identifier"), (GLuint, "num"), Out(Array(GLuint, "num"), "names")]),
    GlFunction(Void, "glDeleteNamesAMD", [(GLenum, "identifier"), (GLuint, "num"), (Array(Const(GLuint), "num"), "names")]),
    GlFunction(GLboolean, "glIsNameAMD", [(GLenum, "identifier"), (GLuint, "name")], sideeffects=False),

    # GL_AMD_occlusion_query_event
    GlFunction(Void, "glQueryObjectParameteruiAMD", [(GLenum, "target"), (GLquery, "id"), (GLenum, "pname"), (GLuint, "param")]),

    # GL_AMD_performance_monitor
    GlFunction(Void, "glGetPerfMonitorGroupsAMD", [Out(Pointer(GLint), "numGroups"), (GLsizei, "groupsSize"), Out(Array(GLuint, "groupsSize"), "groups")], sideeffects=False),
    GlFunction(Void, "glGetPerfMonitorCountersAMD", [(GLuint, "group"), Out(Pointer(GLint), "numCounters"), Out(Pointer(GLint), "maxActiveCounters"), (GLsizei, "counterSize"), Out(Array(GLuint, "counterSize"), "counters")], sideeffects=False),
    GlFunction(Void, "glGetPerfMonitorGroupStringAMD", [(GLuint, "group"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "groupString")], sideeffects=False),
    GlFunction(Void, "glGetPerfMonitorCounterStringAMD", [(GLuint, "group"), (GLuint, "counter"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "counterString")], sideeffects=False),
    GlFunction(Void, "glGetPerfMonitorCounterInfoAMD", [(GLuint, "group"), (GLuint, "counter"), (GLenum, "pname"), Out(GLperfMonitorCounterInfoAMD, "data")], sideeffects=False),
    GlFunction(Void, "glGenPerfMonitorsAMD", [(GLsizei, "n"), Out(Array(GLuint, "n"), "monitors")]),
    GlFunction(Void, "glDeletePerfMonitorsAMD", [(GLsizei, "n"), (Array(GLuint, "n"), "monitors")]),
    GlFunction(Void, "glSelectPerfMonitorCountersAMD", [(GLuint, "monitor"), (GLboolean, "enable"), (GLuint, "group"), (GLint, "numCounters"), (Array(GLuint, "numCounters"), "counterList")]),
    GlFunction(Void, "glBeginPerfMonitorAMD", [(GLuint, "monitor")]),
    GlFunction(Void, "glEndPerfMonitorAMD", [(GLuint, "monitor")]),
    GlFunction(Void, "glGetPerfMonitorCounterDataAMD", [(GLuint, "monitor"), (GLenum, "pname"), (GLsizei, "dataSize"), Out(Array(GLuint, "dataSize"), "data"), Out(Pointer(GLint), "bytesWritten")], sideeffects=False),

    # GL_AMD_sample_positions
    GlFunction(Void, "glSetMultisamplefvAMD", [(GLenum, "pname"), (GLuint, "index"), (Array(Const(GLfloat), 2), "val")]),

    # GL_AMD_sparse_texture
    GlFunction(Void, "glTexStorageSparseAMD", [(GLenum, "target"), (GLenum, "internalFormat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLsizei, "layers"), (GLbitfield_texStorageSparse, "flags")]),
    GlFunction(Void, "glTextureStorageSparseAMD", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "internalFormat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLsizei, "layers"), (GLbitfield_texStorageSparse, "flags")]),

    # GL_AMD_stencil_operation_extended
    GlFunction(Void, "glStencilOpValueAMD", [(GLenum, "face"), (GLuint, "value")]),

    # GL_AMD_vertex_shader_tessellator
    GlFunction(Void, "glTessellationFactorAMD", [(GLfloat, "factor")]),
    GlFunction(Void, "glTessellationModeAMD", [(GLenum, "mode")]),

    # GL_ANGLE_framebuffer_blit
    GlFunction(Void, "glBlitFramebufferANGLE", [(GLint, "srcX0"), (GLint, "srcY0"), (GLint, "srcX1"), (GLint, "srcY1"), (GLint, "dstX0"), (GLint, "dstY0"), (GLint, "dstX1"), (GLint, "dstY1"), (GLbitfield_attrib, "mask"), (GLenum, "filter")]),

    # GL_ANGLE_framebuffer_multisample
    GlFunction(Void, "glRenderbufferStorageMultisampleANGLE", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),

    # GL_ANGLE_instanced_arrays
    GlFunction(Void, "glDrawArraysInstancedANGLE", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count"), (GLsizei, "instancecount")]),
    GlFunction(Void, "glDrawElementsInstancedANGLE", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount")]),
    GlFunction(Void, "glVertexAttribDivisorANGLE", [(GLuint, "index"), (GLuint, "divisor")]),

    # GL_ANGLE_timer_query
    GlFunction(Void, "glGenQueriesANGLE", [(GLsizei, "n"), Out(Array(GLquery, "n"), "ids")]),
    GlFunction(Void, "glDeleteQueriesANGLE", [(GLsizei, "n"), (Array(Const(GLquery), "n"), "ids")]),
    GlFunction(GLboolean, "glIsQueryANGLE", [(GLquery, "id")], sideeffects=False),
    GlFunction(Void, "glBeginQueryANGLE", [(GLenum, "target"), (GLquery, "id")]),
    GlFunction(Void, "glEndQueryANGLE", [(GLenum, "target")]),
    GlFunction(Void, "glQueryCounterANGLE", [(GLquery, "id"), (GLenum, "target")]),
    GlFunction(Void, "glGetQueryivANGLE", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetQueryObjectivANGLE", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjectuivANGLE", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjecti64vANGLE", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLint64, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjectui64vANGLE", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLuint64, "_gl_param_size(pname)"), "params")]),

    # GL_ANGLE_translated_shader_source
    GlFunction(Void, "glGetTranslatedShaderSourceANGLE", [(GLshader, "shader"), (GLsizei, "bufsize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "source")], sideeffects=False),

    # GL_APPLE_copy_texture_levels
    GlFunction(Void, "glCopyTextureLevelsAPPLE", [(GLtexture, "destinationTexture"), (GLtexture, "sourceTexture"), (GLint, "sourceBaseLevel"), (GLsizei, "sourceLevelCount")]),

    # GL_APPLE_element_array
    GlFunction(Void, "glElementPointerAPPLE", [(GLenum, "type"), (Blob(Const(GLvoid), "type"), "pointer")]),
    GlFunction(Void, "glDrawElementArrayAPPLE", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count")]),
    GlFunction(Void, "glDrawRangeElementArrayAPPLE", [(GLenum_mode, "mode"), (GLuint, "start"), (GLuint, "end"), (GLint, "first"), (GLsizei, "count")]),
    GlFunction(Void, "glMultiDrawElementArrayAPPLE", [(GLenum_mode, "mode"), (Array(Const(GLint), "drawcount"), "first"), (Array(Const(GLsizei), "drawcount"), "count"), (GLsizei, "drawcount")]),
    GlFunction(Void, "glMultiDrawRangeElementArrayAPPLE", [(GLenum_mode, "mode"), (GLuint, "start"), (GLuint, "end"), (Array(Const(GLint), "drawcount"), "first"), (Array(Const(GLsizei), "drawcount"), "count"), (GLsizei, "drawcount")]),

    # GL_APPLE_fence
    GlFunction(Void, "glGenFencesAPPLE", [(GLsizei, "n"), Out(Array(GLfence, "n"), "fences")]),
    GlFunction(Void, "glDeleteFencesAPPLE", [(GLsizei, "n"), (Array(Const(GLfence), "n"), "fences")]),
    GlFunction(Void, "glSetFenceAPPLE", [(GLfence, "fence")]),
    GlFunction(GLboolean, "glIsFenceAPPLE", [(GLfence, "fence")], sideeffects=False),
    GlFunction(GLboolean, "glTestFenceAPPLE", [(GLfence, "fence")]),
    GlFunction(Void, "glFinishFenceAPPLE", [(GLfence, "fence")]),
    GlFunction(GLboolean, "glTestObjectAPPLE", [(GLenum, "object"), (GLuint, "name")]), # XXX: name needs swizzling
    GlFunction(Void, "glFinishObjectAPPLE", [(GLenum, "object"), (GLint, "name")]), # XXX: name needs swizzling

    # GL_APPLE_flush_buffer_range
    GlFunction(Void, "glBufferParameteriAPPLE", [(GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glFlushMappedBufferRangeAPPLE", [(GLenum, "target"), (GLintptr, "offset"), (GLsizeiptr, "size")]),

    # GL_APPLE_flush_render
    GlFunction(Void, "glFlushRenderAPPLE", []),
    GlFunction(Void, "glFinishRenderAPPLE", []),
    GlFunction(Void, "glSwapAPPLE", []),

    # GL_APPLE_framebuffer_multisample
    GlFunction(Void, "glRenderbufferStorageMultisampleAPPLE", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glResolveMultisampleFramebufferAPPLE", []),

    # GL_APPLE_object_purgeable
    GlFunction(GLenum, "glObjectPurgeableAPPLE", [(GLenum, "objectType"), (GLuint, "name"), (GLenum, "option")]),
    GlFunction(GLenum, "glObjectUnpurgeableAPPLE", [(GLenum, "objectType"), (GLuint, "name"), (GLenum, "option")]),
    GlFunction(Void, "glGetObjectParameterivAPPLE", [(GLenum, "objectType"), (GLuint, "name"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_APPLE_vertex_point_size
    GlFunction(Void, "glPointSizePointerAPPLE", [(GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glVertexPointSizefAPPLE", [(GLfloat, "size")]),

    # GL_APPLE_sync
    GlFunction(GLsync, "glFenceSyncAPPLE", [(GLenum, "condition"), (GLbitfield, "flags")]),
    GlFunction(GLboolean, "glIsSyncAPPLE", [(GLsync, "sync")], sideeffects=False),
    GlFunction(Void, "glDeleteSyncAPPLE", [(GLsync, "sync")]),
    GlFunction(GLenum, "glClientWaitSyncAPPLE", [(GLsync, "sync"), (GLbitfield_sync_flush, "flags"), (GLuint64, "timeout")]),
    GlFunction(Void, "glWaitSyncAPPLE", [(GLsync, "sync"), (GLbitfield, "flags"), (GLuint64, "timeout")]),
    GlFunction(Void, "glGetInteger64vAPPLE", [(GLenum, "pname"), Out(Array(GLint64, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetSyncivAPPLE", [(GLsync, "sync"), (GLenum, "pname"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Array(GLint, "(length ? *length : bufSize)"), "values")], sideeffects=False),

    # GL_APPLE_texture_range
    GlFunction(Void, "glTextureRangeAPPLE", [(GLenum, "target"), (GLsizei, "length"), (Blob(Const(GLvoid), "length"), "pointer")]),
    GlFunction(Void, "glGetTexParameterPointervAPPLE", [(GLenum, "target"), (GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),

    # GL_APPLE_vertex_array_object
    GlFunction(Void, "glBindVertexArrayAPPLE", [(GLarrayAPPLE, "array")]),
    GlFunction(Void, "glDeleteVertexArraysAPPLE", [(GLsizei, "n"), (Array(Const(GLarrayAPPLE), "n"), "arrays")]),
    GlFunction(Void, "glGenVertexArraysAPPLE", [(GLsizei, "n"), Out(Array(GLarrayAPPLE, "n"), "arrays")]),
    GlFunction(GLboolean, "glIsVertexArrayAPPLE", [(GLarrayAPPLE, "array")], sideeffects=False),

    # GL_APPLE_vertex_array_range
    GlFunction(Void, "glVertexArrayRangeAPPLE", [(GLsizei, "length"), (GLpointer, "pointer")]),
    GlFunction(Void, "glFlushVertexArrayRangeAPPLE", [(GLsizei, "length"), (GLpointer, "pointer")]),
    GlFunction(Void, "glVertexArrayParameteriAPPLE", [(GLenum, "pname"), (GLint, "param")]),

    # GL_APPLE_vertex_program_evaluators
    GlFunction(Void, "glEnableVertexAttribAPPLE", [(GLuint, "index"), (GLenum, "pname")]),
    GlFunction(Void, "glDisableVertexAttribAPPLE", [(GLuint, "index"), (GLenum, "pname")]),
    GlFunction(GLboolean, "glIsVertexAttribEnabledAPPLE", [(GLuint, "index"), (GLenum, "pname")], sideeffects=False),
    GlFunction(Void, "glMapVertexAttrib1dAPPLE", [(GLuint, "index"), (GLuint, "size"), (GLdouble, "u1"), (GLdouble, "u2"), (GLint, "stride"), (GLint, "order"), (OpaqueArray(Const(GLdouble), "_glMapVertexAttrib1dAPPLE_size(size, stride, order)"), "points")]),
    GlFunction(Void, "glMapVertexAttrib1fAPPLE", [(GLuint, "index"), (GLuint, "size"), (GLfloat, "u1"), (GLfloat, "u2"), (GLint, "stride"), (GLint, "order"), (OpaqueArray(Const(GLfloat), "_glMapVertexAttrib1fAPPLE_size(size, stride, order)"), "points")]),
    GlFunction(Void, "glMapVertexAttrib2dAPPLE", [(GLuint, "index"), (GLuint, "size"), (GLdouble, "u1"), (GLdouble, "u2"), (GLint, "ustride"), (GLint, "uorder"), (GLdouble, "v1"), (GLdouble, "v2"), (GLint, "vstride"), (GLint, "vorder"), (OpaqueArray(Const(GLdouble), "_glMapVertexAttrib2dAPPLE_size(size, ustride, uorder, vstride, vorder)"), "points")]),
    GlFunction(Void, "glMapVertexAttrib2fAPPLE", [(GLuint, "index"), (GLuint, "size"), (GLfloat, "u1"), (GLfloat, "u2"), (GLint, "ustride"), (GLint, "uorder"), (GLfloat, "v1"), (GLfloat, "v2"), (GLint, "vstride"), (GLint, "vorder"), (OpaqueArray(Const(GLfloat), "_glMapVertexAttrib2fAPPLE_size(size, ustride, uorder, vstride, vorder)"), "points")]),

    # GL_ARB_ES2_compatibility
    GlFunction(Void, "glReleaseShaderCompiler", []),
    GlFunction(Void, "glShaderBinary", [(GLsizei, "count"), (Array(Const(GLuint), "count"), "shaders"), (GLenum, "binaryformat"), (Blob(Const(GLvoid), "length"), "binary"), (GLsizei, "length")]),
    GlFunction(Void, "glGetShaderPrecisionFormat", [(GLenum, "shadertype"), (GLenum, "precisiontype"), Out(Array(GLint, 2), "range"), Out(Array(GLint, 2), "precision")], sideeffects=False),
    GlFunction(Void, "glDepthRangef", [(GLfloat, "n"), (GLfloat, "f")]),
    GlFunction(Void, "glClearDepthf", [(GLfloat, "d")]),

    # GL_ARB_ES3_1_compatibility
    GlFunction(Void, "glMemoryBarrierByRegion", [(GLbitfield_barrier, "barriers")]),

    # GL_ARB_ES3_2_compatibility
    GlFunction(Void, "glPrimitiveBoundingBoxARB", [(GLfloat, "minX"), (GLfloat, "minY"), (GLfloat, "minZ"), (GLfloat, "minW"), (GLfloat, "maxX"), (GLfloat, "maxY"), (GLfloat, "maxZ"), (GLfloat, "maxW")]),

    # GL_ARB_base_instance
    GlFunction(Void, "glDrawArraysInstancedBaseInstance", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count"), (GLsizei, "instancecount"), (GLuint, "baseinstance")]),
    GlFunction(Void, "glDrawElementsInstancedBaseInstance", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount"), (GLuint, "baseinstance")]),
    GlFunction(Void, "glDrawElementsInstancedBaseVertexBaseInstance", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount"), (GLint, "basevertex"), (GLuint, "baseinstance")]),

    # GL_ARB_bindless_texture
    GlFunction(GLtextureHandle, "glGetTextureHandleARB", [(GLtexture, "texture")]),
    GlFunction(GLtextureHandle, "glGetTextureSamplerHandleARB", [(GLtexture, "texture"), (GLsampler, "sampler")]),
    GlFunction(Void, "glMakeTextureHandleResidentARB", [(GLtextureHandle, "handle")]),
    GlFunction(Void, "glMakeTextureHandleNonResidentARB", [(GLtextureHandle, "handle")]),
    GlFunction(GLimageHandle, "glGetImageHandleARB", [(GLtexture, "texture"), (GLint, "level"), (GLboolean, "layered"), (GLint, "layer"), (GLenum, "format")]),
    GlFunction(Void, "glMakeImageHandleResidentARB", [(GLimageHandle, "handle"), (GLenum, "access")]),
    GlFunction(Void, "glMakeImageHandleNonResidentARB", [(GLimageHandle, "handle")]),
    GlFunction(Void, "glUniformHandleui64ARB", [(GLlocation, "location"), (GLuint64, "value")]),
    GlFunction(Void, "glUniformHandleui64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count"), "value")]),
    GlFunction(Void, "glProgramUniformHandleui64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64, "value")]),
    GlFunction(Void, "glProgramUniformHandleui64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count"), "values")]),
    GlFunction(GLboolean, "glIsTextureHandleResidentARB", [(GLtextureHandle, "handle")], sideeffects=False),
    GlFunction(GLboolean, "glIsImageHandleResidentARB", [(GLimageHandle, "handle")], sideeffects=False),
    GlFunction(Void, "glVertexAttribL1ui64ARB", [(GLuint, "index"), (GLuint64, "x")]),
    GlFunction(Void, "glVertexAttribL1ui64vARB", [(GLuint, "index"), (Pointer(Const(GLuint64)), "v")]),
    GlFunction(Void, "glGetVertexAttribLui64vARB", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLuint64, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_ARB_blend_func_extended
    GlFunction(Void, "glBindFragDataLocationIndexed", [(GLprogram, "program"), (GLuint, "colorNumber"), (GLuint, "index"), (GLstringConst, "name")]),
    GlFunction(GLint, "glGetFragDataIndex", [(GLprogram, "program"), (GLstringConst, "name")], sideeffects=False),

    # GL_ARB_buffer_storage
    GlFunction(Void, "glBufferStorage", [ (GLenum, "target"), (GLsizeiptr, "size"), (Blob(Const(GLvoid), "size"), "data"), (GLbitfield_storage, "flags")]),

    # GL_ARB_cl_event
    GlFunction(GLsync, "glCreateSyncFromCLeventARB", [(Opaque("struct _cl_context *"), "context"), (Opaque("struct _cl_event *"), "event"), (GLbitfield, "flags")], sideeffects=False),

    # GL_ARB_clear_buffer_object
    GlFunction(Void, "glClearBufferData", [(GLenum, "target"), (GLenum, "internalformat"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glClearBufferData_size(format, type)"), "data")]),
    GlFunction(Void, "glClearBufferSubData", [(GLenum, "target"), (GLenum, "internalformat"), (GLintptr, "offset"), (GLsizeiptr, "size"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glClearBufferData_size(format, type)"), "data")]),

    # GL_ARB_clear_texture
    GlFunction(Void, "glClearTexImage", [ (GLtexture, "texture"), (GLint, "level"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glClearBufferData_size(format, type)"), "data")]),
    GlFunction(Void, "glClearTexSubImage", [ (GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glClearBufferData_size(format, type)"), "data")]),

    # GL_ARB_clip_control
    GlFunction(Void, "glClipControl", [(GLenum, "origin"), (GLenum, "depth")]),

    # GL_ARB_color_buffer_float
    GlFunction(Void, "glClampColorARB", [(GLenum, "target"), (GLenum, "clamp")]),

    # GL_ARB_compute_shader
    GlFunction(Void, "glDispatchCompute", [(GLuint, "num_groups_x"), (GLuint, "num_groups_y"), (GLuint, "num_groups_z")]),
    GlFunction(Void, "glDispatchComputeIndirect", [(GLintptr, "indirect")]),

    # GL_ARB_compute_variable_group_size
    GlFunction(Void, "glDispatchComputeGroupSizeARB", [(GLuint, "num_groups_x"), (GLuint, "num_groups_y"), (GLuint, "num_groups_z"), (GLuint, "group_size_x"), (GLuint, "group_size_y"), (GLuint, "group_size_z")]),

    # GL_ARB_copy_buffer
    GlFunction(Void, "glCopyBufferSubData", [(GLenum, "readTarget"), (GLenum, "writeTarget"), (GLintptr, "readOffset"), (GLintptr, "writeOffset"), (GLsizeiptr, "size")]),

    # GL_ARB_copy_image
    GlFunction(Void, "glCopyImageSubData", [(GLtexture, "srcName"), (GLenum, "srcTarget"), (GLint, "srcLevel"), (GLint, "srcX"), (GLint, "srcY"), (GLint, "srcZ"), (GLtexture, "dstName"), (GLenum, "dstTarget"), (GLint, "dstLevel"), (GLint, "dstX"), (GLint, "dstY"), (GLint, "dstZ"), (GLsizei, "srcWidth"), (GLsizei, "srcHeight"), (GLsizei, "srcDepth")]),

    # GL_ARB_debug_output
    GlFunction(Void, "glDebugMessageControlARB", [(GLenum, "source"), (GLenum, "type"), (GLenum, "severity"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "ids"), (GLboolean, "enabled")], sideeffects=True),
    GlFunction(Void, "glDebugMessageInsertARB", [(GLenum, "source"), (GLenum, "type"), (GLuint, "id"), (GLenum, "severity"), (GLsizei, "length"), InGlString(GLchar, "length", "buf")], sideeffects=True),
    GlFunction(Void, "glDebugMessageCallbackARB", [(GLDEBUGPROCARB, "callback"), (GLpointerConst, "userParam")], sideeffects=False),
    GlFunction(GLuint, "glGetDebugMessageLogARB", [(GLuint, "count"), (GLsizei, "bufsize"), Out(Array(GLenum, "count"), "sources"), Out(Array(GLenum, "count"), "types"), Out(Array(GLuint, "count"), "ids"), Out(Array(GLenum, "count"), "severities"), Out(Array(GLsizei, "count"), "lengths"), Out(String(GLchar, "_glGetDebugMessageLog_length(messageLog, lengths, _result)"), "messageLog")], sideeffects=False, fail=0),

    # GL_ARB_direct_state_access
    GlFunction(Void, "glCreateTransformFeedbacks", [(GLsizei, "n"), Out(Array(GLfeedback, "n"), "ids")]),
    GlFunction(Void, "glTransformFeedbackBufferBase", [(GLfeedback, "xfb"), (GLuint, "index"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glTransformFeedbackBufferRange", [(GLfeedback, "xfb"), (GLuint, "index"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size")]),
    GlFunction(Void, "glGetTransformFeedbackiv", [(GLfeedback, "xfb"), (GLenum, "pname"), Out(Pointer(GLint), "param")], sideeffects=False),
    GlFunction(Void, "glGetTransformFeedbacki_v", [(GLfeedback, "xfb"), (GLenum, "pname"), (GLuint, "index"), Out(Pointer(GLint), "param")], sideeffects=False),
    GlFunction(Void, "glGetTransformFeedbacki64_v", [(GLfeedback, "xfb"), (GLenum, "pname"), (GLuint, "index"), Out(Pointer(GLint64), "param")], sideeffects=False),
    GlFunction(Void, "glCreateBuffers", [(GLsizei, "n"), Out(Array(GLbuffer, "n"), "buffers")]),
    GlFunction(Void, "glNamedBufferStorage", [ (GLbuffer, "buffer"), (GLsizeiptr, "size"), (Blob(Const(Void), "size"), "data"), (GLbitfield_storage, "flags")]),
    GlFunction(Void, "glNamedBufferData", [(GLbuffer, "buffer"), (GLsizeiptr, "size"), (Blob(Const(Void), "size"), "data"), (GLenum, "usage")]),
    GlFunction(Void, "glNamedBufferSubData", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size"), (Blob(Const(Void), "size"), "data")]),
    GlFunction(Void, "glCopyNamedBufferSubData", [(GLbuffer, "readBuffer"), (GLbuffer, "writeBuffer"), (GLintptr, "readOffset"), (GLintptr, "writeOffset"), (GLsizeiptr, "size")]),
    GlFunction(Void, "glClearNamedBufferData", [(GLbuffer, "buffer"), (GLenum, "internalformat"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glClearBufferData_size(format, type)"), "data")]),
    GlFunction(Void, "glClearNamedBufferSubData", [(GLbuffer, "buffer"), (GLenum, "internalformat"), (GLintptr, "offset"), (GLsizeiptr, "size"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glClearBufferData_size(format, type)"), "data")]),
    GlFunction(GLmap, "glMapNamedBuffer", [(GLbuffer, "buffer"), (GLenum, "access")]),
    GlFunction(GLmap, "glMapNamedBufferRange", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "length"), (GLbitfield_access, "access")]),
    GlFunction(GLboolean, "glUnmapNamedBuffer", [(GLbuffer, "buffer")]),
    GlFunction(Void, "glFlushMappedNamedBufferRange", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "length")]),
    GlFunction(Void, "glGetNamedBufferParameteriv", [(GLbuffer, "buffer"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedBufferParameteri64v", [(GLbuffer, "buffer"), (GLenum, "pname"), Out(Array(GLint64, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedBufferPointerv", [(GLbuffer, "buffer"), (GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedBufferSubData", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size"), Out(OpaqueBlob(Void, "size"), "data")], sideeffects=False),
    GlFunction(Void, "glCreateFramebuffers", [(GLsizei, "n"), Out(Array(GLframebuffer, "n"), "framebuffers")]),
    GlFunction(Void, "glNamedFramebufferRenderbuffer", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLenum, "renderbuffertarget"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glNamedFramebufferParameteri", [(GLframebuffer, "framebuffer"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glNamedFramebufferTexture", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glNamedFramebufferTextureLayer", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLint, "layer")]),
    GlFunction(Void, "glNamedFramebufferDrawBuffer", [(GLframebuffer, "framebuffer"), (GLenum, "buf")]),
    GlFunction(Void, "glNamedFramebufferDrawBuffers", [(GLframebuffer, "framebuffer"), (GLsizei, "n"), (Array(Const(GLenum), "n"), "bufs")]),
    GlFunction(Void, "glNamedFramebufferReadBuffer", [(GLframebuffer, "framebuffer"), (GLenum, "src")]),
    GlFunction(Void, "glInvalidateNamedFramebufferData", [(GLframebuffer, "framebuffer"), (GLsizei, "numAttachments"), (Array(Const(GLenum), "numAttachments"), "attachments")]),
    GlFunction(Void, "glInvalidateNamedFramebufferSubData", [(GLframebuffer, "framebuffer"), (GLsizei, "numAttachments"), (Array(Const(GLenum), "numAttachments"), "attachments"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glClearNamedFramebufferiv", [(GLframebuffer, "framebuffer"), (GLenum, "buffer"), (GLint, "drawbuffer"), (Array(Const(GLint), "_glClearBuffer_size(buffer)"), "value")]),
    GlFunction(Void, "glClearNamedFramebufferuiv", [(GLframebuffer, "framebuffer"), (GLenum, "buffer"), (GLint, "drawbuffer"), (Array(Const(GLuint), "_glClearBuffer_size(buffer)"), "value")]),
    GlFunction(Void, "glClearNamedFramebufferfv", [(GLframebuffer, "framebuffer"), (GLenum, "buffer"), (GLint, "drawbuffer"), (Array(Const(GLfloat), "_glClearBuffer_size(buffer)"), "value")]),
    GlFunction(Void, "glClearNamedFramebufferfi", [(GLframebuffer, "framebuffer"), (GLenum, "buffer"), (GLint, "drawbuffer"), (GLfloat, "depth"), (GLint, "stencil")]),
    GlFunction(Void, "glBlitNamedFramebuffer", [(GLframebuffer, "readFramebuffer"), (GLframebuffer, "drawFramebuffer"), (GLint, "srcX0"), (GLint, "srcY0"), (GLint, "srcX1"), (GLint, "srcY1"), (GLint, "dstX0"), (GLint, "dstY0"), (GLint, "dstX1"), (GLint, "dstY1"), (GLbitfield, "mask"), (GLenum, "filter")]),
    GlFunction(GLenum, "glCheckNamedFramebufferStatus", [(GLframebuffer, "framebuffer"), (GLenum, "target")]),
    GlFunction(Void, "glGetNamedFramebufferParameteriv", [(GLframebuffer, "framebuffer"), (GLenum, "pname"), Out(Pointer(GLint), "param")], sideeffects=False),
    GlFunction(Void, "glGetNamedFramebufferAttachmentParameteriv", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glCreateRenderbuffers", [(GLsizei, "n"), Out(Array(GLrenderbuffer, "n"), "renderbuffers")]),
    GlFunction(Void, "glNamedRenderbufferStorage", [(GLrenderbuffer, "renderbuffer"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glNamedRenderbufferStorageMultisample", [(GLrenderbuffer, "renderbuffer"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glGetNamedRenderbufferParameteriv", [(GLrenderbuffer, "renderbuffer"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glCreateTextures", [(GLenum, "target"), (GLsizei, "n"), Out(Array(GLtexture, "n"), "textures")]),
    GlFunction(Void, "glTextureBuffer", [(GLtexture, "texture"), (GLenum, "internalformat"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glTextureBufferRange", [(GLtexture, "texture"), (GLenum, "internalformat"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size")]),
    GlFunction(Void, "glTextureStorage1D", [(GLtexture, "texture"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width")]),
    GlFunction(Void, "glTextureStorage2D", [(GLtexture, "texture"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glTextureStorage3D", [(GLtexture, "texture"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth")]),
    GlFunction(Void, "glTextureStorage2DMultisample", [(GLtexture, "texture"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLboolean, "fixedsamplelocations")]),
    GlFunction(Void, "glTextureStorage3DMultisample", [(GLtexture, "texture"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "fixedsamplelocations")]),
    GlFunction(Void, "glTextureSubImage1D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glTexImage1D_size(format, type, width)"), "pixels")]),
    GlFunction(Void, "glTextureSubImage2D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glTexImage2D_size(format, type, width, height)"), "pixels")]),
    GlFunction(Void, "glTextureSubImage3D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glCompressedTextureSubImage1D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(Void), "writeCompressedTex(data, format, width, 0, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTextureSubImage2D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(Void), "writeCompressedTex(data, format, width, height, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTextureSubImage3D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(Void), "writeCompressedTex(data, format, width, height, depth, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCopyTextureSubImage1D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glCopyTextureSubImage2D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glCopyTextureSubImage3D", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glTextureParameterf", [(GLtexture, "texture"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glTextureParameterfv", [(GLtexture, "texture"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTextureParameteri", [(GLtexture, "texture"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glTextureParameterIiv", [(GLtexture, "texture"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTextureParameterIuiv", [(GLtexture, "texture"), (GLenum, "pname"), (Array(Const(GLuint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTextureParameteriv", [(GLtexture, "texture"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGenerateTextureMipmap", [(GLtexture, "texture")]),
    GlFunction(Void, "glBindTextureUnit", [(GLuint, "unit"), (GLtexture, "texture")]),
    GlFunction(Void, "glGetTextureImage", [(GLtexture, "texture"), (GLint, "level"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(GLpointer, "pixels")]),
    GlFunction(Void, "glGetCompressedTextureImage", [(GLtexture, "texture"), (GLint, "level"), (GLsizei, "bufSize"), Out(GLpointer, "pixels")]),
    GlFunction(Void, "glGetTextureLevelParameterfv", [(GLtexture, "texture"), (GLint, "level"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureLevelParameteriv", [(GLtexture, "texture"), (GLint, "level"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureParameterfv", [(GLtexture, "texture"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureParameterIiv", [(GLtexture, "texture"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureParameterIuiv", [(GLtexture, "texture"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureParameteriv", [(GLtexture, "texture"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glCreateVertexArrays", [(GLsizei, "n"), Out(Array(GLarray, "n"), "arrays")]),
    GlFunction(Void, "glDisableVertexArrayAttrib", [(GLarray, "vaobj"), (GLuint, "index")]),
    GlFunction(Void, "glEnableVertexArrayAttrib", [(GLarray, "vaobj"), (GLuint, "index")]),
    GlFunction(Void, "glVertexArrayElementBuffer", [(GLarray, "vaobj"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glVertexArrayVertexBuffer", [(GLarray, "vaobj"), (GLuint, "bindingindex"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizei, "stride")]),
    GlFunction(Void, "glVertexArrayVertexBuffers", [(GLarray, "vaobj"), (GLuint, "first"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "buffers"), (Array(Const(GLintptr), "count"), "offsets"), (Array(Const(GLsizei), "count"), "strides")]),
    GlFunction(Void, "glVertexArrayAttribBinding", [(GLarray, "vaobj"), (GLuint, "attribindex"), (GLuint, "bindingindex")]),
    GlFunction(Void, "glVertexArrayAttribFormat", [(GLarray, "vaobj"), (GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLboolean, "normalized"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexArrayAttribIFormat", [(GLarray, "vaobj"), (GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexArrayAttribLFormat", [(GLarray, "vaobj"), (GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexArrayBindingDivisor", [(GLarray, "vaobj"), (GLuint, "bindingindex"), (GLuint, "divisor")]),
    GlFunction(Void, "glGetVertexArrayiv", [(GLarray, "vaobj"), (GLenum, "pname"), Out(Pointer(GLint), "param")], sideeffects=False),
    GlFunction(Void, "glGetVertexArrayIndexediv", [(GLarray, "vaobj"), (GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLint), "param")], sideeffects=False),
    GlFunction(Void, "glGetVertexArrayIndexed64iv", [(GLarray, "vaobj"), (GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLint64), "param")], sideeffects=False),
    GlFunction(Void, "glCreateSamplers", [(GLsizei, "n"), Out(Array(GLsampler, "n"), "samplers")]),
    GlFunction(Void, "glCreateProgramPipelines", [(GLsizei, "n"), Out(Array(GLpipeline, "n"), "pipelines")]),
    GlFunction(Void, "glCreateQueries", [(GLenum, "target"), (GLsizei, "n"), Out(Array(GLquery, "n"), "ids")]),
    GlFunction(Void, "glGetQueryBufferObjecti64v", [(GLquery, "id"), (GLbuffer, "buffer"), (GLenum, "pname"), (GLintptr, "offset")]),
    GlFunction(Void, "glGetQueryBufferObjectiv", [(GLquery, "id"), (GLbuffer, "buffer"), (GLenum, "pname"), (GLintptr, "offset")]),
    GlFunction(Void, "glGetQueryBufferObjectui64v", [(GLquery, "id"), (GLbuffer, "buffer"), (GLenum, "pname"), (GLintptr, "offset")]),
    GlFunction(Void, "glGetQueryBufferObjectuiv", [(GLquery, "id"), (GLbuffer, "buffer"), (GLenum, "pname"), (GLintptr, "offset")]),

    # GL_ARB_draw_buffers
    GlFunction(Void, "glDrawBuffersARB", [(GLsizei, "n"), (Array(Const(GLenum), "n"), "bufs")]),

    # GL_ARB_draw_buffers_blend
    GlFunction(Void, "glBlendEquationiARB", [(GLuint, "buf"), (GLenum, "mode")]),
    GlFunction(Void, "glBlendEquationSeparateiARB", [(GLuint, "buf"), (GLenum, "modeRGB"), (GLenum, "modeAlpha")]),
    GlFunction(Void, "glBlendFunciARB", [(GLuint, "buf"), (GLenum, "src"), (GLenum, "dst")]),
    GlFunction(Void, "glBlendFuncSeparateiARB", [(GLuint, "buf"), (GLenum, "srcRGB"), (GLenum, "dstRGB"), (GLenum, "srcAlpha"), (GLenum, "dstAlpha")]),

    # GL_ARB_draw_elements_base_vertex
    GlFunction(Void, "glDrawElementsBaseVertex", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLint, "basevertex")]),
    GlFunction(Void, "glDrawRangeElementsBaseVertex", [(GLenum_mode, "mode"), (GLuint, "start"), (GLuint, "end"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLint, "basevertex")]),
    GlFunction(Void, "glDrawElementsInstancedBaseVertex", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount"), (GLint, "basevertex")]),
    GlFunction(Void, "glMultiDrawElementsBaseVertex", [(GLenum_mode, "mode"), (Array(Const(GLsizei), "drawcount"), "count"), (GLenum, "type"), (Array(Const(GLindexBuffer("count[{i}]", "type")), "drawcount"), "indices"), (GLsizei, "drawcount"), (Array(Const(GLint), "drawcount"), "basevertex")]),

    # GL_ARB_draw_indirect
    GlFunction(Void, "glDrawArraysIndirect", [(GLenum_mode, "mode"), (GLdrawArraysIndirectBuffer(), "indirect")]),
    GlFunction(Void, "glDrawElementsIndirect", [(GLenum_mode, "mode"), (GLenum, "type"), (GLdrawElementsIndirectBuffer(), "indirect")]),

    # GL_ARB_draw_instanced
    GlFunction(Void, "glDrawArraysInstancedARB", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count"), (GLsizei, "instancecount")]),
    GlFunction(Void, "glDrawElementsInstancedARB", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount")]),

    # GL_ARB_framebuffer_no_attachments
    GlFunction(Void, "glFramebufferParameteri", [(GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glGetFramebufferParameteriv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_ARB_framebuffer_object
    GlFunction(GLboolean, "glIsRenderbuffer", [(GLrenderbuffer, "renderbuffer")], sideeffects=False),
    GlFunction(Void, "glBindRenderbuffer", [(GLenum, "target"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glDeleteRenderbuffers", [(GLsizei, "n"), (Array(Const(GLrenderbuffer), "n"), "renderbuffers")]),
    GlFunction(Void, "glGenRenderbuffers", [(GLsizei, "n"), Out(Array(GLrenderbuffer, "n"), "renderbuffers")]),
    GlFunction(Void, "glRenderbufferStorage", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glGetRenderbufferParameteriv", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLboolean, "glIsFramebuffer", [(GLframebuffer, "framebuffer")], sideeffects=False),
    GlFunction(Void, "glBindFramebuffer", [(GLenum, "target"), (GLframebuffer, "framebuffer")]),
    GlFunction(Void, "glDeleteFramebuffers", [(GLsizei, "n"), (Array(Const(GLframebuffer), "n"), "framebuffers")]),
    GlFunction(Void, "glGenFramebuffers", [(GLsizei, "n"), Out(Array(GLframebuffer, "n"), "framebuffers")]),
    GlFunction(GLenum, "glCheckFramebufferStatus", [(GLenum, "target")]),
    GlFunction(Void, "glFramebufferTexture1D", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glFramebufferTexture2D", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glFramebufferTexture3D", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level"), (GLint, "zoffset")]),
    GlFunction(Void, "glFramebufferRenderbuffer", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "renderbuffertarget"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glGetFramebufferAttachmentParameteriv", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGenerateMipmap", [(GLenum, "target")]),
    GlFunction(Void, "glBlitFramebuffer", [(GLint, "srcX0"), (GLint, "srcY0"), (GLint, "srcX1"), (GLint, "srcY1"), (GLint, "dstX0"), (GLint, "dstY0"), (GLint, "dstX1"), (GLint, "dstY1"), (GLbitfield_attrib, "mask"), (GLenum, "filter")]),
    GlFunction(Void, "glRenderbufferStorageMultisample", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glFramebufferTextureLayer", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLint, "layer")]),

    # GL_ARB_geometry_shader4
    GlFunction(Void, "glProgramParameteriARB", [(GLprogram, "program"), (GLenum, "pname"), (GLint, "value")]),
    GlFunction(Void, "glFramebufferTextureARB", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glFramebufferTextureLayerARB", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLint, "layer")]),
    GlFunction(Void, "glFramebufferTextureFaceARB", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLenum, "face")]),

    # GL_ARB_get_program_binary
    GlFunction(Void, "glGetProgramBinary", [(GLprogram, "program"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLenum), "binaryFormat"), Out(OpaqueBlob(GLvoid, "length ? *length : bufSize"), "binary")], sideeffects=False),
    GlFunction(Void, "glProgramBinary", [(GLprogram, "program"), (GLenum, "binaryFormat"), (Blob(Const(GLvoid), "length"), "binary"), (GLsizei, "length")]),
    GlFunction(Void, "glProgramParameteri", [(GLprogram, "program"), (GLenum, "pname"), (GLint, "value")]),

    # GL_ARB_get_texture_sub_image
    GlFunction(Void, "glGetTextureSubImage", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(GLpointer, "pixels")]),
    GlFunction(Void, "glGetCompressedTextureSubImage", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLsizei, "bufSize"), Out(GLpointer, "pixels")]),

    # GL_ARB_gl_spirv
    GlFunction(Void, "glSpecializeShaderARB", [(GLshader, "shader"), (GLstringConst, "pEntryPoint"), (GLuint, "numSpecializationConstants"), (Array(Const(GLuint), "numSpecializationConstants"), "pConstantIndex"), (Array(Const(GLuint), "numSpecializationConstants"), "pConstantValue")]),

    # GL_ARB_gpu_shader_fp64
    GlFunction(Void, "glUniform1d", [(GLlocation, "location"), (GLdouble, "x")]),
    GlFunction(Void, "glUniform2d", [(GLlocation, "location"), (GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glUniform3d", [(GLlocation, "location"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glUniform4d", [(GLlocation, "location"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glUniform1dv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count"), "value")]),
    GlFunction(Void, "glUniform2dv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*2"), "value")]),
    GlFunction(Void, "glUniform3dv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*3"), "value")]),
    GlFunction(Void, "glUniform4dv", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*4"), "value")]),
    GlFunction(Void, "glUniformMatrix2dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*2"), "value")]),
    GlFunction(Void, "glUniformMatrix3dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*3"), "value")]),
    GlFunction(Void, "glUniformMatrix4dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*4"), "value")]),
    GlFunction(Void, "glUniformMatrix2x3dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*3"), "value")]),
    GlFunction(Void, "glUniformMatrix2x4dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*4"), "value")]),
    GlFunction(Void, "glUniformMatrix3x2dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*2"), "value")]),
    GlFunction(Void, "glUniformMatrix3x4dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*4"), "value")]),
    GlFunction(Void, "glUniformMatrix4x2dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*2"), "value")]),
    GlFunction(Void, "glUniformMatrix4x3dv", [(GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*3"), "value")]),
    GlFunction(Void, "glGetUniformdv", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaqueArray(GLdouble, "_glGetUniformdv_size(location)"), "params")], sideeffects=False),

    # GL_ARB_gpu_shader_int64
    GlFunction(Void, "glUniform1i64ARB", [(GLlocation, "location"), (GLint64, "x")]),
    GlFunction(Void, "glUniform2i64ARB", [(GLlocation, "location"), (GLint64, "x"), (GLint64, "y")]),
    GlFunction(Void, "glUniform3i64ARB", [(GLlocation, "location"), (GLint64, "x"), (GLint64, "y"), (GLint64, "z")]),
    GlFunction(Void, "glUniform4i64ARB", [(GLlocation, "location"), (GLint64, "x"), (GLint64, "y"), (GLint64, "z"), (GLint64, "w")]),
    GlFunction(Void, "glUniform1i64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64), "count*1"), "value")]),
    GlFunction(Void, "glUniform2i64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64), "count*2"), "value")]),
    GlFunction(Void, "glUniform3i64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64), "count*3"), "value")]),
    GlFunction(Void, "glUniform4i64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64), "count*4"), "value")]),
    GlFunction(Void, "glUniform1ui64ARB", [(GLlocation, "location"), (GLuint64, "x")]),
    GlFunction(Void, "glUniform2ui64ARB", [(GLlocation, "location"), (GLuint64, "x"), (GLuint64, "y")]),
    GlFunction(Void, "glUniform3ui64ARB", [(GLlocation, "location"), (GLuint64, "x"), (GLuint64, "y"), (GLuint64, "z")]),
    GlFunction(Void, "glUniform4ui64ARB", [(GLlocation, "location"), (GLuint64, "x"), (GLuint64, "y"), (GLuint64, "z"), (GLuint64, "w")]),
    GlFunction(Void, "glUniform1ui64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count*1"), "value")]),
    GlFunction(Void, "glUniform2ui64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count*2"), "value")]),
    GlFunction(Void, "glUniform3ui64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count*3"), "value")]),
    GlFunction(Void, "glUniform4ui64vARB", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count*4"), "value")]),
    GlFunction(Void, "glGetUniformi64vARB", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaquePointer(GLint64), "params")], sideeffects=False),
    GlFunction(Void, "glGetUniformui64vARB", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaquePointer(GLuint64), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformi64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLint64, "bufSize"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformui64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLuint64, "bufSize"), "params")], sideeffects=False),
    GlFunction(Void, "glProgramUniform1i64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLint64, "x")]),
    GlFunction(Void, "glProgramUniform2i64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLint64, "x"), (GLint64, "y")]),
    GlFunction(Void, "glProgramUniform3i64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLint64, "x"), (GLint64, "y"), (GLint64, "z")]),
    GlFunction(Void, "glProgramUniform4i64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLint64, "x"), (GLint64, "y"), (GLint64, "z"), (GLint64, "w")]),
    GlFunction(Void, "glProgramUniform1i64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64), "count"), "value")]),
    GlFunction(Void, "glProgramUniform2i64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform3i64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform4i64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniform1ui64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64, "x")]),
    GlFunction(Void, "glProgramUniform2ui64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64, "x"), (GLuint64, "y")]),
    GlFunction(Void, "glProgramUniform3ui64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64, "x"), (GLuint64, "y"), (GLuint64, "z")]),
    GlFunction(Void, "glProgramUniform4ui64ARB", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64, "x"), (GLuint64, "y"), (GLuint64, "z"), (GLuint64, "w")]),
    GlFunction(Void, "glProgramUniform1ui64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count"), "value")]),
    GlFunction(Void, "glProgramUniform2ui64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform3ui64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform4ui64vARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count*4"), "value")]),

    # GL_ARB_indirect_parameters
    GlFunction(Void, "glMultiDrawArraysIndirectCountARB", [(GLenum_mode, "mode"), (GLdrawArraysIndirectBuffer("maxdrawcount", "stride"), "indirect"), (GLintptr, "drawcount"), (GLsizei, "maxdrawcount"), (GLsizei, "stride")]),
    GlFunction(Void, "glMultiDrawElementsIndirectCountARB", [(GLenum_mode, "mode"), (GLenum, "type"), (GLdrawElementsIndirectBuffer("maxdrawcount", "stride"), "indirect"), (GLintptr, "drawcount"), (GLsizei, "maxdrawcount"), (GLsizei, "stride")]),

    # GL_ARB_instanced_arrays
    GlFunction(Void, "glVertexAttribDivisorARB", [(GLuint, "index"), (GLuint, "divisor")]),

    # GL_ARB_internalformat_query
    GlFunction(Void, "glGetInternalformativ", [(GLenum, "target"), (GLenum, "internalformat"), (GLenum, "pname"), (GLsizei, "bufSize"), Out(Array(GLint, "bufSize"), "params")], sideeffects=False),

    # GL_ARB_internalformat_query2
    GlFunction(Void, "glGetInternalformati64v", [(GLenum, "target"), (GLenum, "internalformat"), (GLenum, "pname"), (GLsizei, "bufSize"), Out(Array(GLint64, "bufSize"), "params")], sideeffects=False),

    # GL_ARB_invalidate_subdata
    GlFunction(Void, "glInvalidateTexSubImage", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth")]),
    GlFunction(Void, "glInvalidateTexImage", [(GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glInvalidateBufferSubData", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "length")]),
    GlFunction(Void, "glInvalidateBufferData", [(GLbuffer, "buffer")]),
    GlFunction(Void, "glInvalidateFramebuffer", [(GLenum, "target"), (GLsizei, "numAttachments"), (Array(Const(GLenum), "numAttachments"), "attachments")]),
    GlFunction(Void, "glInvalidateSubFramebuffer", [(GLenum, "target"), (GLsizei, "numAttachments"), (Array(Const(GLenum), "numAttachments"), "attachments"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),

    # GL_ARB_map_buffer_range
    GlFunction(GLmap, "glMapBufferRange", [(GLenum, "target"), (GLintptr, "offset"), (GLsizeiptr, "length"), (GLbitfield_access, "access")]),
    GlFunction(Void, "glFlushMappedBufferRange", [(GLenum, "target"), (GLintptr, "offset"), (GLsizeiptr, "length")]),

    # GL_ARB_matrix_palette
    GlFunction(Void, "glCurrentPaletteMatrixARB", [(GLint, "index")]),
    GlFunction(Void, "glMatrixIndexubvARB", [(GLint, "size"), (Array(Const(GLubyte), "size"), "indices")]),
    GlFunction(Void, "glMatrixIndexusvARB", [(GLint, "size"), (Array(Const(GLushort), "size"), "indices")]),
    GlFunction(Void, "glMatrixIndexuivARB", [(GLint, "size"), (Array(Const(GLuint), "size"), "indices")]),
    GlFunction(Void, "glMatrixIndexPointerARB", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),

    # GL_ARB_multi_bind
    GlFunction(Void, "glBindBuffersBase", [(GLenum, "target"), (GLuint, "first"), (GLsizei, "count"), (Array(Const(GLbuffer), "count"), "buffers")]),
    GlFunction(Void, "glBindBuffersRange", [(GLenum, "target"), (GLuint, "first"), (GLsizei, "count"), (Array(Const(GLbuffer), "count"), "buffers"), (Array(Const(GLintptr), "count"), "offsets"), (Array(Const(GLsizeiptr), "count"), "sizes")]),
    GlFunction(Void, "glBindTextures", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLtexture), "count"), "textures")]),
    GlFunction(Void, "glBindSamplers", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLsampler), "count"), "samplers")]),
    GlFunction(Void, "glBindImageTextures", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLtexture), "count"), "textures")]),
    GlFunction(Void, "glBindVertexBuffers", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLbuffer), "count"), "buffers"), (Array(Const(GLintptr), "count"), "offsets"), (Array(Const(GLsizei), "count"), "strides")]),

    # GL_ARB_multi_draw_indirect
    GlFunction(Void, "glMultiDrawArraysIndirect", [(GLenum_mode, "mode"), (GLdrawArraysIndirectBuffer("drawcount", "stride"), "indirect"), (GLsizei, "drawcount"), (GLsizei, "stride")]),
    GlFunction(Void, "glMultiDrawElementsIndirect", [(GLenum_mode, "mode"), (GLenum, "type"), (GLdrawElementsIndirectBuffer("drawcount", "stride"), "indirect"), (GLsizei, "drawcount"), (GLsizei, "stride")]),

    # GL_ARB_multisample
    GlFunction(Void, "glSampleCoverageARB", [(GLfloat, "value"), (GLboolean, "invert")]),

    # GL_ARB_multitexture
    GlFunction(Void, "glActiveTextureARB", [(GLenum, "texture")]),
    GlFunction(Void, "glClientActiveTextureARB", [(GLenum, "texture")]),
    GlFunction(Void, "glMultiTexCoord1dARB", [(GLenum, "target"), (GLdouble, "s")]),
    GlFunction(Void, "glMultiTexCoord1dvARB", [(GLenum, "target"), (Pointer(Const(GLdouble)), "v")]),
    GlFunction(Void, "glMultiTexCoord1fARB", [(GLenum, "target"), (GLfloat, "s")]),
    GlFunction(Void, "glMultiTexCoord1fvARB", [(GLenum, "target"), (Pointer(Const(GLfloat)), "v")]),
    GlFunction(Void, "glMultiTexCoord1iARB", [(GLenum, "target"), (GLint, "s")]),
    GlFunction(Void, "glMultiTexCoord1ivARB", [(GLenum, "target"), (Pointer(Const(GLint)), "v")]),
    GlFunction(Void, "glMultiTexCoord1sARB", [(GLenum, "target"), (GLshort, "s")]),
    GlFunction(Void, "glMultiTexCoord1svARB", [(GLenum, "target"), (Pointer(Const(GLshort)), "v")]),
    GlFunction(Void, "glMultiTexCoord2dARB", [(GLenum, "target"), (GLdouble, "s"), (GLdouble, "t")]),
    GlFunction(Void, "glMultiTexCoord2dvARB", [(GLenum, "target"), (Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord2fARB", [(GLenum, "target"), (GLfloat, "s"), (GLfloat, "t")]),
    GlFunction(Void, "glMultiTexCoord2fvARB", [(GLenum, "target"), (Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord2iARB", [(GLenum, "target"), (GLint, "s"), (GLint, "t")]),
    GlFunction(Void, "glMultiTexCoord2ivARB", [(GLenum, "target"), (Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord2sARB", [(GLenum, "target"), (GLshort, "s"), (GLshort, "t")]),
    GlFunction(Void, "glMultiTexCoord2svARB", [(GLenum, "target"), (Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord3dARB", [(GLenum, "target"), (GLdouble, "s"), (GLdouble, "t"), (GLdouble, "r")]),
    GlFunction(Void, "glMultiTexCoord3dvARB", [(GLenum, "target"), (Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord3fARB", [(GLenum, "target"), (GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r")]),
    GlFunction(Void, "glMultiTexCoord3fvARB", [(GLenum, "target"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord3iARB", [(GLenum, "target"), (GLint, "s"), (GLint, "t"), (GLint, "r")]),
    GlFunction(Void, "glMultiTexCoord3ivARB", [(GLenum, "target"), (Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord3sARB", [(GLenum, "target"), (GLshort, "s"), (GLshort, "t"), (GLshort, "r")]),
    GlFunction(Void, "glMultiTexCoord3svARB", [(GLenum, "target"), (Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord4dARB", [(GLenum, "target"), (GLdouble, "s"), (GLdouble, "t"), (GLdouble, "r"), (GLdouble, "q")]),
    GlFunction(Void, "glMultiTexCoord4dvARB", [(GLenum, "target"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glMultiTexCoord4fARB", [(GLenum, "target"), (GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r"), (GLfloat, "q")]),
    GlFunction(Void, "glMultiTexCoord4fvARB", [(GLenum, "target"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glMultiTexCoord4iARB", [(GLenum, "target"), (GLint, "s"), (GLint, "t"), (GLint, "r"), (GLint, "q")]),
    GlFunction(Void, "glMultiTexCoord4ivARB", [(GLenum, "target"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glMultiTexCoord4sARB", [(GLenum, "target"), (GLshort, "s"), (GLshort, "t"), (GLshort, "r"), (GLshort, "q")]),
    GlFunction(Void, "glMultiTexCoord4svARB", [(GLenum, "target"), (Array(Const(GLshort), 4), "v")]),

    # GL_ARB_occlusion_query
    GlFunction(Void, "glGenQueriesARB", [(GLsizei, "n"), Out(Array(GLquery, "n"), "ids")]),
    GlFunction(Void, "glDeleteQueriesARB", [(GLsizei, "n"), (Array(Const(GLquery), "n"), "ids")]),
    GlFunction(GLboolean, "glIsQueryARB", [(GLquery, "id")], sideeffects=False),
    GlFunction(Void, "glBeginQueryARB", [(GLenum, "target"), (GLquery, "id")]),
    GlFunction(Void, "glEndQueryARB", [(GLenum, "target")]),
    GlFunction(Void, "glGetQueryivARB", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetQueryObjectivARB", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjectuivARB", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")]),

    # GL_ARB_parallel_shader_compile
    GlFunction(Void, "glMaxShaderCompilerThreadsARB", [(GLuint, "count")]),

    # GL_ARB_point_parameters
    GlFunction(Void, "glPointParameterfARB", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glPointParameterfvARB", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),

    # GL_ARB_program_interface_query
    GlFunction(Void, "glGetProgramInterfaceiv", [(GLprogram, "program"), (GLenum, "programInterface"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLuint, "glGetProgramResourceIndex", [(GLprogram, "program"), (GLenum, "programInterface"), (GLstringConst, "name")], sideeffects=False),
    GlFunction(Void, "glGetProgramResourceName", [(GLprogram, "program"), (GLenum, "programInterface"), (GLuint, "index"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "name")]),
    GlFunction(Void, "glGetProgramResourceiv", [(GLprogram, "program"), (GLenum, "programInterface"), (GLuint, "index"), (GLsizei, "propCount"), (Array(Const(GLenum), "propCount"), "props"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Array(GLint, "bufSize"), "params")]),
    GlFunction(GLlocation, "glGetProgramResourceLocation", [(GLprogram, "program"), (GLenum, "programInterface"), (GLstringConst, "name")]),
    GlFunction(GLint, "glGetProgramResourceLocationIndex", [(GLprogram, "program"), (GLenum, "programInterface"), (GLstringConst, "name")], sideeffects=False),

    # GL_ARB_provoking_vertex
    GlFunction(Void, "glProvokingVertex", [(GLenum, "mode")]),

    # GL_ARB_robustness
    GlFunction(GLenum, "glGetGraphicsResetStatusARB", [], sideeffects=False),
    GlFunction(Void, "glGetnMapdvARB", [(GLenum, "target"), (GLenum, "query"), (GLsizei, "bufSize"), Out(Array(GLdouble, "bufSize/sizeof(GLdouble)"), "v")], sideeffects=False),
    GlFunction(Void, "glGetnMapfvARB", [(GLenum, "target"), (GLenum, "query"), (GLsizei, "bufSize"), Out(Array(GLfloat, "bufSize/sizeof(GLfloat)"), "v")], sideeffects=False),
    GlFunction(Void, "glGetnMapivARB", [(GLenum, "target"), (GLenum, "query"), (GLsizei, "bufSize"), Out(Array(GLint, "bufSize/sizeof(GLint)"), "v")], sideeffects=False),
    GlFunction(Void, "glGetnPixelMapfvARB", [(GLenum, "map"), (GLsizei, "bufSize"), Out(Array(GLfloat, "bufSize/sizeof(GLfloat)"), "values")]),
    GlFunction(Void, "glGetnPixelMapuivARB", [(GLenum, "map"), (GLsizei, "bufSize"), Out(Array(GLuint, "bufSize/sizeof(GLuint)"), "values")]),
    GlFunction(Void, "glGetnPixelMapusvARB", [(GLenum, "map"), (GLsizei, "bufSize"), Out(Array(GLushort, "bufSize/sizeof(GLushort)"), "values")]),
    GlFunction(Void, "glGetnPolygonStippleARB", [(GLsizei, "bufSize"), Out(OpaqueBlob(GLubyte, "bufSize"), "pattern")]),
    GlFunction(Void, "glGetnColorTableARB", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "table")], sideeffects=False),
    GlFunction(Void, "glGetnConvolutionFilterARB", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "image")]),
    GlFunction(Void, "glGetnSeparableFilterARB", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "rowBufSize"), Out(OpaqueBlob(GLvoid, "rowBufSize"), "row"), (GLsizei, "columnBufSize"), Out(OpaqueBlob(GLvoid, "columnBufSize"), "column"), Out(GLpointer, "span")]),
    GlFunction(Void, "glGetnHistogramARB", [(GLenum, "target"), (GLboolean, "reset"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "values")]),
    GlFunction(Void, "glGetnMinmaxARB", [(GLenum, "target"), (GLboolean, "reset"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "values")]),
    GlFunction(Void, "glGetnTexImageARB", [(GLenum, "target"), (GLint, "level"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "img")]),
    GlFunction(Void, "glReadnPixelsARB", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "data")]),
    GlFunction(Void, "glGetnCompressedTexImageARB", [(GLenum, "target"), (GLint, "lod"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "img")]),
    GlFunction(Void, "glGetnUniformfvARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLfloat, "bufSize/sizeof(GLfloat)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformivARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLint, "bufSize/sizeof(GLint)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformuivARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLuint, "bufSize/sizeof(GLuint)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformdvARB", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLdouble, "bufSize/sizeof(GLdouble)"), "params")], sideeffects=False),

    # GL_ARB_sample_locations
    GlFunction(Void, "glFramebufferSampleLocationsfvARB", [(GLenum, "target"), (GLuint, "start"), (GLsizei, "count"), (Array(Const(GLfloat), "count*2"), "v")]),
    GlFunction(Void, "glNamedFramebufferSampleLocationsfvARB", [(GLframebuffer, "framebuffer"), (GLuint, "start"), (GLsizei, "count"), (Array(Const(GLfloat), "count*2"), "v")]),
    GlFunction(Void, "glEvaluateDepthValuesARB", []),

    # GL_ARB_sample_shading
    GlFunction(Void, "glMinSampleShadingARB", [(GLfloat, "value")]),

    # GL_ARB_sampler_objects
    GlFunction(Void, "glGenSamplers", [(GLsizei, "count"), Out(Array(GLsampler, "count"), "samplers")]),
    GlFunction(Void, "glDeleteSamplers", [(GLsizei, "count"), (Array(Const(GLsampler), "count"), "samplers")]),
    GlFunction(GLboolean, "glIsSampler", [(GLsampler, "sampler")], sideeffects=False),
    GlFunction(Void, "glBindSampler", [(GLuint, "unit"), (GLsampler, "sampler")]),
    GlFunction(Void, "glSamplerParameteri", [(GLsampler, "sampler"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glSamplerParameteriv", [(GLsampler, "sampler"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "param")]),
    GlFunction(Void, "glSamplerParameterf", [(GLsampler, "sampler"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glSamplerParameterfv", [(GLsampler, "sampler"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "param")]),
    GlFunction(Void, "glSamplerParameterIiv", [(GLsampler, "sampler"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "param")]),
    GlFunction(Void, "glSamplerParameterIuiv", [(GLsampler, "sampler"), (GLenum, "pname"), (Array(Const(GLuint), "_gl_param_size(pname)"), "param")]),
    GlFunction(Void, "glGetSamplerParameteriv", [(GLsampler, "sampler"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetSamplerParameterIiv", [(GLsampler, "sampler"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetSamplerParameterfv", [(GLsampler, "sampler"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetSamplerParameterIuiv", [(GLsampler, "sampler"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_ARB_separate_shader_objects
    GlFunction(Void, "glUseProgramStages", [(GLpipeline, "pipeline"), (GLbitfield_shader, "stages"), (GLprogram, "program")]),
    GlFunction(Void, "glActiveShaderProgram", [(GLpipeline, "pipeline"), (GLprogram, "program")]),
    GlFunction(GLprogram, "glCreateShaderProgramv", [(GLenum, "type"), (GLsizei, "count"), (Array(Const(GLstringConst), "count"), "strings")]),
    GlFunction(Void, "glBindProgramPipeline", [(GLpipeline, "pipeline")]),
    GlFunction(Void, "glDeleteProgramPipelines", [(GLsizei, "n"), (Array(Const(GLuint), "n"), "pipelines")]),
    GlFunction(Void, "glGenProgramPipelines", [(GLsizei, "n"), Out(Array(GLpipeline, "n"), "pipelines")]),
    GlFunction(GLboolean, "glIsProgramPipeline", [(GLpipeline, "pipeline")], sideeffects=False),
    GlFunction(Void, "glGetProgramPipelineiv", [(GLpipeline, "pipeline"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glProgramUniform1i", [(GLprogram, "program"), (GLlocation, "location"), (GLint, "v0")]),
    GlFunction(Void, "glProgramUniform1iv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count"), "value")]),
    GlFunction(Void, "glProgramUniform1f", [(GLprogram, "program"), (GLlocation, "location"), (GLfloat, "v0")]),
    GlFunction(Void, "glProgramUniform1fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count"), "value")]),
    GlFunction(Void, "glProgramUniform1d", [(GLprogram, "program"), (GLlocation, "location"), (GLdouble, "v0")]),
    GlFunction(Void, "glProgramUniform1dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count"), "value")]),
    GlFunction(Void, "glProgramUniform1ui", [(GLprogram, "program"), (GLlocation, "location"), (GLuint, "v0")]),
    GlFunction(Void, "glProgramUniform1uiv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "value")]),
    GlFunction(Void, "glProgramUniform2i", [(GLprogram, "program"), (GLlocation, "location"), (GLint, "v0"), (GLint, "v1")]),
    GlFunction(Void, "glProgramUniform2iv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform2f", [(GLprogram, "program"), (GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1")]),
    GlFunction(Void, "glProgramUniform2fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform2d", [(GLprogram, "program"), (GLlocation, "location"), (GLdouble, "v0"), (GLdouble, "v1")]),
    GlFunction(Void, "glProgramUniform2dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform2ui", [(GLprogram, "program"), (GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1")]),
    GlFunction(Void, "glProgramUniform2uiv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform3i", [(GLprogram, "program"), (GLlocation, "location"), (GLint, "v0"), (GLint, "v1"), (GLint, "v2")]),
    GlFunction(Void, "glProgramUniform3iv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform3f", [(GLprogram, "program"), (GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1"), (GLfloat, "v2")]),
    GlFunction(Void, "glProgramUniform3fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform3d", [(GLprogram, "program"), (GLlocation, "location"), (GLdouble, "v0"), (GLdouble, "v1"), (GLdouble, "v2")]),
    GlFunction(Void, "glProgramUniform3dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform3ui", [(GLprogram, "program"), (GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1"), (GLuint, "v2")]),
    GlFunction(Void, "glProgramUniform3uiv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform4i", [(GLprogram, "program"), (GLlocation, "location"), (GLint, "v0"), (GLint, "v1"), (GLint, "v2"), (GLint, "v3")]),
    GlFunction(Void, "glProgramUniform4iv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniform4f", [(GLprogram, "program"), (GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1"), (GLfloat, "v2"), (GLfloat, "v3")]),
    GlFunction(Void, "glProgramUniform4fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniform4d", [(GLprogram, "program"), (GLlocation, "location"), (GLdouble, "v0"), (GLdouble, "v1"), (GLdouble, "v2"), (GLdouble, "v3")]),
    GlFunction(Void, "glProgramUniform4dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniform4ui", [(GLprogram, "program"), (GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1"), (GLuint, "v2"), (GLuint, "v3")]),
    GlFunction(Void, "glProgramUniform4uiv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2x3fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3x2fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2x4fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4x2fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3x4fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4x3fv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2x3dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3x2dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2x4dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4x2dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3x4dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4x3dv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*3"), "value")]),
    GlFunction(Void, "glValidateProgramPipeline", [(GLpipeline, "pipeline")]),
    GlFunction(Void, "glGetProgramPipelineInfoLog", [(GLpipeline, "pipeline"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "infoLog")], sideeffects=False),

    # GL_ARB_shader_atomic_counters
    GlFunction(Void, "glGetActiveAtomicCounterBufferiv", [(GLprogram, "program"), (GLuint, "bufferIndex"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_ARB_shader_image_load_store
    GlFunction(Void, "glBindImageTexture", [(GLuint, "unit"), (GLtexture, "texture"), (GLint, "level"), (GLboolean, "layered"), (GLint, "layer"), (GLenum, "access"), (GLenum, "format")]),
    GlFunction(Void, "glMemoryBarrier", [(GLbitfield_barrier, "barriers")]),

    # GL_ARB_shader_objects
    GlFunction(Void, "glDeleteObjectARB", [(GLhandleARB, "obj")]),
    GlFunction(GLhandleARB, "glGetHandleARB", [(GLenum, "pname")], sideeffects=False),
    GlFunction(Void, "glDetachObjectARB", [(GLhandleARB, "containerObj"), (GLhandleARB, "attachedObj")]),
    GlFunction(GLhandleARB, "glCreateShaderObjectARB", [(GLenum, "shaderType")]),
    GlFunction(Void, "glShaderSourceARB", [(GLhandleARB, "shaderObj"), (GLsizei, "count"), (Const(Array(String(Const(GLcharARB), "_glShaderSource_length(string, length, {i})"), "count")), "string"), (Array(Const(GLint), "count"), "length")]),
    GlFunction(Void, "glCompileShaderARB", [(GLhandleARB, "shaderObj")]),
    GlFunction(GLhandleARB, "glCreateProgramObjectARB", []),
    GlFunction(Void, "glAttachObjectARB", [(GLhandleARB, "containerObj"), (GLhandleARB, "obj")]),
    GlFunction(Void, "glLinkProgramARB", [(GLhandleARB, "programObj")]),
    GlFunction(Void, "glUseProgramObjectARB", [(GLhandleARB, "programObj")]),
    GlFunction(Void, "glValidateProgramARB", [(GLhandleARB, "programObj")]),
    GlFunction(Void, "glUniform1fARB", [(GLlocationARB, "location"), (GLfloat, "v0")]),
    GlFunction(Void, "glUniform2fARB", [(GLlocationARB, "location"), (GLfloat, "v0"), (GLfloat, "v1")]),
    GlFunction(Void, "glUniform3fARB", [(GLlocationARB, "location"), (GLfloat, "v0"), (GLfloat, "v1"), (GLfloat, "v2")]),
    GlFunction(Void, "glUniform4fARB", [(GLlocationARB, "location"), (GLfloat, "v0"), (GLfloat, "v1"), (GLfloat, "v2"), (GLfloat, "v3")]),
    GlFunction(Void, "glUniform1iARB", [(GLlocationARB, "location"), (GLint, "v0")]),
    GlFunction(Void, "glUniform2iARB", [(GLlocationARB, "location"), (GLint, "v0"), (GLint, "v1")]),
    GlFunction(Void, "glUniform3iARB", [(GLlocationARB, "location"), (GLint, "v0"), (GLint, "v1"), (GLint, "v2")]),
    GlFunction(Void, "glUniform4iARB", [(GLlocationARB, "location"), (GLint, "v0"), (GLint, "v1"), (GLint, "v2"), (GLint, "v3")]),
    GlFunction(Void, "glUniform1fvARB", [(GLlocationARB, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count"), "value")]),
    GlFunction(Void, "glUniform2fvARB", [(GLlocationARB, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*2"), "value")]),
    GlFunction(Void, "glUniform3fvARB", [(GLlocationARB, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*3"), "value")]),
    GlFunction(Void, "glUniform4fvARB", [(GLlocationARB, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "value")]),
    GlFunction(Void, "glUniform1ivARB", [(GLlocationARB, "location"), (GLsizei, "count"), (Array(Const(GLint), "count"), "value")]),
    GlFunction(Void, "glUniform2ivARB", [(GLlocationARB, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*2"), "value")]),
    GlFunction(Void, "glUniform3ivARB", [(GLlocationARB, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*3"), "value")]),
    GlFunction(Void, "glUniform4ivARB", [(GLlocationARB, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "value")]),
    GlFunction(Void, "glUniformMatrix2fvARB", [(GLlocationARB, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*2"), "value")]),
    GlFunction(Void, "glUniformMatrix3fvARB", [(GLlocationARB, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*3"), "value")]),
    GlFunction(Void, "glUniformMatrix4fvARB", [(GLlocationARB, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*4"), "value")]),
    GlFunction(Void, "glGetObjectParameterfvARB", [(GLhandleARB, "obj"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetObjectParameterivARB", [(GLhandleARB, "obj"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetInfoLogARB", [(GLhandleARB, "obj"), (GLsizei, "maxLength"), Out(Pointer(GLsizei), "length"), OutGlString(GLcharARB, "length", "infoLog")], sideeffects=False),
    GlFunction(Void, "glGetAttachedObjectsARB", [(GLhandleARB, "containerObj"), (GLsizei, "maxCount"), Out(Pointer(GLsizei), "count"), Out(Array(GLhandleARB, "(count ? *count : maxCount)"), "obj")], sideeffects=False),
    GlFunction(GLlocationARB, "glGetUniformLocationARB", [(GLhandleARB, "programObj"), (GLstringConstARB, "name")]),
    GlFunction(Void, "glGetActiveUniformARB", [(GLhandleARB, "programObj"), (GLuint, "index"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLint), "size"), Out(Pointer(GLenum), "type"), OutGlString(GLcharARB, "length", "name")], sideeffects=False),
    GlFunction(Void, "glGetUniformfvARB", [(GLhandleARB, "programObj"), (GLlocationARB, "location"), Out(OpaquePointer(GLfloat), "params")], sideeffects=False),
    GlFunction(Void, "glGetUniformivARB", [(GLhandleARB, "programObj"), (GLlocationARB, "location"), Out(OpaquePointer(GLint), "params")], sideeffects=False),
    GlFunction(Void, "glGetShaderSourceARB", [(GLhandleARB, "obj"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLcharARB, "length", "source")], sideeffects=False),

    # GL_ARB_shader_storage_buffer_object
    GlFunction(Void, "glShaderStorageBlockBinding", [(GLprogram, "program"), (GLuint, "storageBlockIndex"), (GLuint, "storageBlockBinding")]),

    # GL_ARB_shader_subroutine
    GlFunction(GLlocation, "glGetSubroutineUniformLocation", [(GLprogram, "program"), (GLenum, "shadertype"), (GLstringConst, "name")]),
    GlFunction(GLsubroutine, "glGetSubroutineIndex", [(GLprogram, "program"), (GLenum, "shadertype"), (GLstringConst, "name")]),
    GlFunction(Void, "glGetActiveSubroutineUniformiv", [(GLprogram, "program"), (GLenum, "shadertype"), (GLsubroutine, "index"), (GLenum, "pname"), Out(OpaqueArray(GLint, "_glGetActiveSubroutineUniformiv_size(pname)"), "values")], sideeffects=False),
    GlFunction(Void, "glGetActiveSubroutineUniformName", [(GLprogram, "program"), (GLenum, "shadertype"), (GLsubroutine, "index"), (GLsizei, "bufsize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "name")], sideeffects=False),
    GlFunction(Void, "glGetActiveSubroutineName", [(GLprogram, "program"), (GLenum, "shadertype"), (GLsubroutine, "index"), (GLsizei, "bufsize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "name")], sideeffects=False),
    GlFunction(Void, "glUniformSubroutinesuiv", [(GLenum, "shadertype"), (GLsizei, "count"), (Array(Const(GLsubroutine), "count"), "indices")]),
    GlFunction(Void, "glGetUniformSubroutineuiv", [(GLenum, "shadertype"), (GLlocation, "location"), Out(OpaquePointer(GLuint), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramStageiv", [(GLprogram, "program"), (GLenum, "shadertype"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "values")], sideeffects=False),

    # GL_ARB_shading_language_include
    GlFunction(Void, "glNamedStringARB", [(GLenum, "type"), (GLint, "namelen"), InGlString(GLchar, "namelen", "name"), (GLint, "stringlen"), InGlString(GLchar, "stringlen", "string")]),
    GlFunction(Void, "glDeleteNamedStringARB", [(GLint, "namelen"), InGlString(GLchar, "namelen", "name")]),
    GlFunction(Void, "glCompileShaderIncludeARB", [(GLshader, "shader"), (GLsizei, "count"), (Array(Const(String(Const(GLchar), "_glShaderSource_length(path, length, {i})")), "count"), "path"), (Array(Const(GLint), "count"), "length")]),
    GlFunction(GLboolean, "glIsNamedStringARB", [(GLint, "namelen"), InGlString(GLchar, "namelen", "name")], sideeffects=False),
    GlFunction(Void, "glGetNamedStringARB", [(GLint, "namelen"), InGlString(GLchar, "namelen", "name"), (GLsizei, "bufSize"), Out(Pointer(GLint), "stringlen"), OutGlString(GLchar, "stringlen", "string")], sideeffects=False),
    GlFunction(Void, "glGetNamedStringivARB", [(GLint, "namelen"), InGlString(GLchar, "namelen", "name"), (GLenum, "pname"), Out(OpaqueArray(GLint, "_glGetNamedStringivARB_size(pname)"), "params")], sideeffects=False),

    # GL_ARB_sparse_buffer
    GlFunction(Void, "glBufferPageCommitmentARB", [(GLenum, "target"), (GLintptr, "offset"), (GLsizeiptr, "size"), (GLboolean, "commit")]),
    GlFunction(Void, "glNamedBufferPageCommitmentEXT", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size"), (GLboolean, "commit")]),
    GlFunction(Void, "glNamedBufferPageCommitmentARB", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size"), (GLboolean, "commit")]),

    # GL_ARB_sparse_texture
    GlFunction(Void, "glTexPageCommitmentARB", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "resident")]),

    # GL_ARB_sync
    GlFunction(GLsync, "glFenceSync", [(GLenum, "condition"), (GLbitfield, "flags")]),
    GlFunction(GLboolean, "glIsSync", [(GLsync, "sync")], sideeffects=False),
    GlFunction(Void, "glDeleteSync", [(GLsync, "sync")]),
    GlFunction(GLenum, "glClientWaitSync", [(GLsync, "sync"), (GLbitfield_sync_flush, "flags"), (GLuint64, "timeout")]),
    GlFunction(Void, "glWaitSync", [(GLsync, "sync"), (GLbitfield, "flags"), (GLuint64, "timeout")]),
    GlFunction(Void, "glGetInteger64v", [(GLenum, "pname"), Out(Array(GLint64, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetSynciv", [(GLsync, "sync"), (GLenum, "pname"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Array(GLint, "(length ? *length : bufSize)"), "values")]),

    # GL_ARB_tessellation_shader
    GlFunction(Void, "glPatchParameteri", [(GLenum, "pname"), (GLint, "value")]),
    GlFunction(Void, "glPatchParameterfv", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "values")]),

    # GL_ARB_texture_barrier
    GlFunction(Void, "glTextureBarrier", []),

    # GL_ARB_texture_buffer_object
    GlFunction(Void, "glTexBufferARB", [(GLenum, "target"), (GLenum, "internalformat"), (GLbuffer, "buffer")]),

    # GL_ARB_texture_buffer_range
    GlFunction(Void, "glTexBufferRange", [(GLenum, "target"), (GLenum, "internalformat"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size")]),

    # GL_ARB_texture_compression
    GlFunction(Void, "glCompressedTexImage3DARB", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, internalformat, width, height, depth, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexImage2DARB", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, internalformat, width, height, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexImage1DARB", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, internalformat, width, 0, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexSubImage3DARB", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, format, width, height, depth, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexSubImage2DARB", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, format, width, height, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexSubImage1DARB", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, format, width, 0, 0, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glGetCompressedTexImageARB", [(GLenum, "target"), (GLint, "level"), Out(GLpointer, "img")]),

    # GL_ARB_texture_multisample
    GlFunction(Void, "glTexImage2DMultisample", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLboolean, "fixedsamplelocations")]),
    GlFunction(Void, "glTexImage3DMultisample", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "fixedsamplelocations")]),
    GlFunction(Void, "glGetMultisamplefv", [(GLenum, "pname"), (GLuint, "index"), Out(Array(GLfloat, 2), "val")], sideeffects=False),
    GlFunction(Void, "glSampleMaski", [(GLuint, "index"), (GLbitfield, "mask")]),

    # GL_ARB_texture_storage
    GlFunction(Void, "glTexStorage1D", [(GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width")]),
    GlFunction(Void, "glTexStorage2D", [(GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glTexStorage3D", [(GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth")]),

    # GL_EXT_texture_storage_compression
    GlFunction(Void, "glTexStorageAttribs2DEXT", [(GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLattribs_texStorage, "attrib_list")]),
    GlFunction(Void, "glTexStorageAttribs3DEXT", [(GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLattribs_texStorage, "attrib_list")]),

    # GL_ARB_texture_storage_multisample
    GlFunction(Void, "glTexStorage2DMultisample", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLboolean, "fixedsamplelocations")]),
    GlFunction(Void, "glTexStorage3DMultisample", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "fixedsamplelocations")]),

    # GL_EXT_EGL_image_storage
    GlFunction(Void, "glEGLImageTargetTexStorageEXT", [(GLenum, "target"), (GLeglImageOES, "image"), (GLattribs_texStorage, "attrib_list")]),
    GlFunction(Void, "glEGLImageTargetTextureStorageEXT", [(GLtexture, "texture"), (GLeglImageOES, "image"), (GLattribs_texStorage, "attrib_list")]),

    # GL_ARB_texture_view
    GlFunction(Void, "glTextureView", [(GLtexture, "texture"), (GLenum, "target"), (GLtexture, "origtexture"), (GLenum, "internalformat"), (GLuint, "minlevel"), (GLuint, "numlevels"), (GLuint, "minlayer"), (GLuint, "numlayers")]),

    # GL_ARB_timer_query
    GlFunction(Void, "glQueryCounter", [(GLquery, "id"), (GLenum, "target")]),
    GlFunction(Void, "glGetQueryObjecti64v", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLint64, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjectui64v", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLuint64, "_gl_param_size(pname)"), "params")]),

    # GL_ARB_transform_feedback2
    GlFunction(Void, "glBindTransformFeedback", [(GLenum, "target"), (GLfeedback, "id")]),
    GlFunction(Void, "glDeleteTransformFeedbacks", [(GLsizei, "n"), (Array(Const(GLfeedback), "n"), "ids")]),
    GlFunction(Void, "glGenTransformFeedbacks", [(GLsizei, "n"), Out(Array(GLfeedback, "n"), "ids")]),
    GlFunction(GLboolean, "glIsTransformFeedback", [(GLfeedback, "id")], sideeffects=False),
    GlFunction(Void, "glPauseTransformFeedback", []),
    GlFunction(Void, "glResumeTransformFeedback", []),
    GlFunction(Void, "glDrawTransformFeedback", [(GLenum_mode, "mode"), (GLfeedback, "id")]),

    # GL_ARB_transform_feedback3
    GlFunction(Void, "glDrawTransformFeedbackStream", [(GLenum_mode, "mode"), (GLfeedback, "id"), (GLuint, "stream")]),
    GlFunction(Void, "glBeginQueryIndexed", [(GLenum, "target"), (GLuint, "index"), (GLfeedback, "id")]),
    GlFunction(Void, "glEndQueryIndexed", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(Void, "glGetQueryIndexediv", [(GLenum, "target"), (GLuint, "index"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_ARB_transform_feedback_instanced
    GlFunction(Void, "glDrawTransformFeedbackInstanced", [(GLenum_mode, "mode"), (GLfeedback, "id"), (GLsizei, "instancecount")]),
    GlFunction(Void, "glDrawTransformFeedbackStreamInstanced", [(GLenum_mode, "mode"), (GLfeedback, "id"), (GLuint, "stream"), (GLsizei, "instancecount")]),

    # GL_ARB_transpose_matrix
    GlFunction(Void, "glLoadTransposeMatrixfARB", [(Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glLoadTransposeMatrixdARB", [(Array(Const(GLdouble), 16), "m")]),
    GlFunction(Void, "glMultTransposeMatrixfARB", [(Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glMultTransposeMatrixdARB", [(Array(Const(GLdouble), 16), "m")]),

    # GL_ARB_uniform_buffer_object
    GlFunction(Void, "glGetUniformIndices", [(GLprogram, "program"), (GLsizei, "uniformCount"), (Array(Const(GLstringConst), "uniformCount"), "uniformNames"), Out(Array(GLuint, "uniformCount"), "uniformIndices")], sideeffects=False),
    GlFunction(Void, "glGetActiveUniformsiv", [(GLprogram, "program"), (GLsizei, "uniformCount"), (Array(Const(GLuint), "uniformCount"), "uniformIndices"), (GLenum, "pname"), Out(OpaqueArray(GLint, "_glGetActiveUniformsiv_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetActiveUniformName", [(GLprogram, "program"), (GLuint, "uniformIndex"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "uniformName")], sideeffects=False),
    GlFunction(GLuniformBlock, "glGetUniformBlockIndex", [(GLprogram, "program"), (GLstringConst, "uniformBlockName")]),
    GlFunction(Void, "glGetActiveUniformBlockiv", [(GLprogram, "program"), (GLuniformBlock, "uniformBlockIndex"), (GLenum, "pname"), Out(OpaqueArray(GLint, "_glGetActiveUniformBlockiv_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetActiveUniformBlockName", [(GLprogram, "program"), (GLuniformBlock, "uniformBlockIndex"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "uniformBlockName")]),
    GlFunction(Void, "glUniformBlockBinding", [(GLprogram, "program"), (GLuniformBlock, "uniformBlockIndex"), (GLuint, "uniformBlockBinding")]),

    # GL_ARB_vertex_array_object
    GlFunction(Void, "glBindVertexArray", [(GLarray, "array")]),
    GlFunction(Void, "glDeleteVertexArrays", [(GLsizei, "n"), (Array(Const(GLarray), "n"), "arrays")]),
    GlFunction(Void, "glGenVertexArrays", [(GLsizei, "n"), Out(Array(GLarray, "n"), "arrays")]),
    GlFunction(GLboolean, "glIsVertexArray", [(GLarray, "array")], sideeffects=False),

    # GL_ARB_vertex_attrib_64bit
    GlFunction(Void, "glVertexAttribL1d", [(GLuint, "index"), (GLdouble, "x")]),
    GlFunction(Void, "glVertexAttribL2d", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glVertexAttribL3d", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glVertexAttribL4d", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glVertexAttribL1dv", [(GLuint, "index"), (Pointer(Const(GLdouble)), "v")]),
    GlFunction(Void, "glVertexAttribL2dv", [(GLuint, "index"), (Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glVertexAttribL3dv", [(GLuint, "index"), (Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glVertexAttribL4dv", [(GLuint, "index"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glVertexAttribLPointer", [(GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glGetVertexAttribLdv", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_ARB_vertex_attrib_binding
    GlFunction(Void, "glBindVertexBuffer", [(GLuint, "bindingindex"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizei, "stride")]),
    GlFunction(Void, "glVertexAttribFormat", [(GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLboolean, "normalized"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexAttribIFormat", [(GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexAttribLFormat", [(GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexAttribBinding", [(GLuint, "attribindex"), (GLuint, "bindingindex")]),
    GlFunction(Void, "glVertexBindingDivisor", [(GLuint, "bindingindex"), (GLuint, "divisor")]),

    # GL_ARB_vertex_blend
    GlFunction(Void, "glWeightbvARB", [(GLint, "size"), (Array(Const(GLbyte), "size"), "weights")]),
    GlFunction(Void, "glWeightsvARB", [(GLint, "size"), (Array(Const(GLshort), "size"), "weights")]),
    GlFunction(Void, "glWeightivARB", [(GLint, "size"), (Array(Const(GLint), "size"), "weights")]),
    GlFunction(Void, "glWeightfvARB", [(GLint, "size"), (Array(Const(GLfloat), "size"), "weights")]),
    GlFunction(Void, "glWeightdvARB", [(GLint, "size"), (Array(Const(GLdouble), "size"), "weights")]),
    GlFunction(Void, "glWeightubvARB", [(GLint, "size"), (Array(Const(GLubyte), "size"), "weights")]),
    GlFunction(Void, "glWeightusvARB", [(GLint, "size"), (Array(Const(GLushort), "size"), "weights")]),
    GlFunction(Void, "glWeightuivARB", [(GLint, "size"), (Array(Const(GLuint), "size"), "weights")]),
    GlFunction(Void, "glWeightPointerARB", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glVertexBlendARB", [(GLint, "count")]),

    # GL_ARB_vertex_buffer_object
    GlFunction(Void, "glBindBufferARB", [(GLenum, "target"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glDeleteBuffersARB", [(GLsizei, "n"), (Array(Const(GLbuffer), "n"), "buffers")]),
    GlFunction(Void, "glGenBuffersARB", [(GLsizei, "n"), Out(Array(GLbuffer, "n"), "buffers")]),
    GlFunction(GLboolean, "glIsBufferARB", [(GLbuffer, "buffer")], sideeffects=False),
    GlFunction(Void, "glBufferDataARB", [(GLenum, "target"), (GLsizeiptrARB, "size"), (Blob(Const(GLvoid), "size"), "data"), (GLenum, "usage")]),
    GlFunction(Void, "glBufferSubDataARB", [(GLenum, "target"), (GLintptrARB, "offset"), (GLsizeiptrARB, "size"), (Blob(Const(GLvoid), "size"), "data")]),
    GlFunction(Void, "glGetBufferSubDataARB", [(GLenum, "target"), (GLintptrARB, "offset"), (GLsizeiptrARB, "size"), Out(OpaqueBlob(GLvoid, "size"), "data")], sideeffects=False),
    GlFunction(GLmap, "glMapBufferARB", [(GLenum, "target"), (GLenum, "access")]),
    GlFunction(GLboolean, "glUnmapBufferARB", [(GLenum, "target")]),
    GlFunction(Void, "glGetBufferParameterivARB", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetBufferPointervARB", [(GLenum, "target"), (GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),

    # GL_ARB_vertex_program
    GlFunction(Void, "glVertexAttrib1dARB", [(GLuint, "index"), (GLdouble, "x")]),
    GlFunction(Void, "glVertexAttrib1dvARB", [(GLuint, "index"), (Pointer(Const(GLdouble)), "v")]),
    GlFunction(Void, "glVertexAttrib1fARB", [(GLuint, "index"), (GLfloat, "x")]),
    GlFunction(Void, "glVertexAttrib1fvARB", [(GLuint, "index"), (Pointer(Const(GLfloat)), "v")]),
    GlFunction(Void, "glVertexAttrib1sARB", [(GLuint, "index"), (GLshort, "x")]),
    GlFunction(Void, "glVertexAttrib1svARB", [(GLuint, "index"), (Pointer(Const(GLshort)), "v")]),
    GlFunction(Void, "glVertexAttrib2dARB", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glVertexAttrib2dvARB", [(GLuint, "index"), (Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glVertexAttrib2fARB", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glVertexAttrib2fvARB", [(GLuint, "index"), (Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glVertexAttrib2sARB", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glVertexAttrib2svARB", [(GLuint, "index"), (Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glVertexAttrib3dARB", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glVertexAttrib3dvARB", [(GLuint, "index"), (Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glVertexAttrib3fARB", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glVertexAttrib3fvARB", [(GLuint, "index"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glVertexAttrib3sARB", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glVertexAttrib3svARB", [(GLuint, "index"), (Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glVertexAttrib4NbvARB", [(GLuint, "index"), (Array(Const(GLbyte), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4NivARB", [(GLuint, "index"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4NsvARB", [(GLuint, "index"), (Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4NubARB", [(GLuint, "index"), (GLubyte, "x"), (GLubyte, "y"), (GLubyte, "z"), (GLubyte, "w")]),
    GlFunction(Void, "glVertexAttrib4NubvARB", [(GLuint, "index"), (Array(Const(GLubyte), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4NuivARB", [(GLuint, "index"), (Array(Const(GLuint), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4NusvARB", [(GLuint, "index"), (Array(Const(GLushort), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4bvARB", [(GLuint, "index"), (Array(Const(GLbyte), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4dARB", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glVertexAttrib4dvARB", [(GLuint, "index"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4fARB", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glVertexAttrib4fvARB", [(GLuint, "index"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4ivARB", [(GLuint, "index"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4sARB", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y"), (GLshort, "z"), (GLshort, "w")]),
    GlFunction(Void, "glVertexAttrib4svARB", [(GLuint, "index"), (Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4ubvARB", [(GLuint, "index"), (Array(Const(GLubyte), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4uivARB", [(GLuint, "index"), (Array(Const(GLuint), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4usvARB", [(GLuint, "index"), (Array(Const(GLushort), 4), "v")]),
    GlFunction(Void, "glVertexAttribPointerARB", [(GLuint, "index"), (size_bgra, "size"), (GLenum, "type"), (GLboolean, "normalized"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glEnableVertexAttribArrayARB", [(GLuint, "index")]),
    GlFunction(Void, "glDisableVertexAttribArrayARB", [(GLuint, "index")]),
    GlFunction(Void, "glProgramStringARB", [(GLenum, "target"), (GLenum, "format"), (GLsizei, "len"), (String(Const(Void), "len"), "string")]),
    GlFunction(Void, "glBindProgramARB", [(GLenum, "target"), (GLprogramARB, "program")]),
    GlFunction(Void, "glDeleteProgramsARB", [(GLsizei, "n"), (Array(Const(GLprogramARB), "n"), "programs")]),
    GlFunction(Void, "glGenProgramsARB", [(GLsizei, "n"), Out(Array(GLprogramARB, "n"), "programs")]),
    GlFunction(Void, "glProgramEnvParameter4dARB", [(GLenum, "target"), (GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glProgramEnvParameter4dvARB", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLdouble), 4), "params")]),
    GlFunction(Void, "glProgramEnvParameter4fARB", [(GLenum, "target"), (GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glProgramEnvParameter4fvARB", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLfloat), 4), "params")]),
    GlFunction(Void, "glProgramLocalParameter4dARB", [(GLenum, "target"), (GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glProgramLocalParameter4dvARB", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLdouble), 4), "params")]),
    GlFunction(Void, "glProgramLocalParameter4fARB", [(GLenum, "target"), (GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glProgramLocalParameter4fvARB", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLfloat), 4), "params")]),
    GlFunction(Void, "glGetProgramEnvParameterdvARB", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLdouble, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramEnvParameterfvARB", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLfloat, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramLocalParameterdvARB", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLdouble, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramLocalParameterfvARB", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLfloat, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramivARB", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramStringARB", [(GLenum, "target"), (GLenum, "pname"), Out(GLpointer, "string")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribdvARB", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribfvARB", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribivARB", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribPointervARB", [(GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLpointer), "pointer")], sideeffects=False),
    GlFunction(GLboolean, "glIsProgramARB", [(GLprogramARB, "program")], sideeffects=False),

    # GL_ARB_vertex_shader
    GlFunction(Void, "glBindAttribLocationARB", [(GLhandleARB, "programObj"), (GLuint, "index"), (GLstringConstARB, "name")]),
    GlFunction(Void, "glGetActiveAttribARB", [(GLhandleARB, "programObj"), (GLuint, "index"), (GLsizei, "maxLength"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLint), "size"), Out(Pointer(GLenum), "type"), OutGlString(GLcharARB, "length", "name")], sideeffects=False),
    GlFunction(GLint, "glGetAttribLocationARB", [(GLhandleARB, "programObj"), (GLstringConstARB, "name")]),

    # GL_ARB_vertex_type_2_10_10_10_rev
    GlFunction(Void, "glVertexAttribP1ui", [(GLuint, "index"), (GLenum, "type"), (GLboolean, "normalized"), (GLuint, "value")]),
    GlFunction(Void, "glVertexAttribP1uiv", [(GLuint, "index"), (GLenum, "type"), (GLboolean, "normalized"), (Pointer(Const(GLuint)), "value")]),
    GlFunction(Void, "glVertexAttribP2ui", [(GLuint, "index"), (GLenum, "type"), (GLboolean, "normalized"), (GLuint, "value")]),
    GlFunction(Void, "glVertexAttribP2uiv", [(GLuint, "index"), (GLenum, "type"), (GLboolean, "normalized"), (Pointer(Const(GLuint)), "value")]),
    GlFunction(Void, "glVertexAttribP3ui", [(GLuint, "index"), (GLenum, "type"), (GLboolean, "normalized"), (GLuint, "value")]),
    GlFunction(Void, "glVertexAttribP3uiv", [(GLuint, "index"), (GLenum, "type"), (GLboolean, "normalized"), (Pointer(Const(GLuint)), "value")]),
    GlFunction(Void, "glVertexAttribP4ui", [(GLuint, "index"), (GLenum, "type"), (GLboolean, "normalized"), (GLuint, "value")]),
    GlFunction(Void, "glVertexAttribP4uiv", [(GLuint, "index"), (GLenum, "type"), (GLboolean, "normalized"), (Pointer(Const(GLuint)), "value")]),
    GlFunction(Void, "glVertexP2ui", [(GLenum, "type"), (GLuint, "value")]),
    GlFunction(Void, "glVertexP2uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "value")]),
    GlFunction(Void, "glVertexP3ui", [(GLenum, "type"), (GLuint, "value")]),
    GlFunction(Void, "glVertexP3uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "value")]),
    GlFunction(Void, "glVertexP4ui", [(GLenum, "type"), (GLuint, "value")]),
    GlFunction(Void, "glVertexP4uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "value")]),
    GlFunction(Void, "glTexCoordP1ui", [(GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glTexCoordP1uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glTexCoordP2ui", [(GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glTexCoordP2uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glTexCoordP3ui", [(GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glTexCoordP3uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glTexCoordP4ui", [(GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glTexCoordP4uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glMultiTexCoordP1ui", [(GLenum, "texture"), (GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glMultiTexCoordP1uiv", [(GLenum, "texture"), (GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glMultiTexCoordP2ui", [(GLenum, "texture"), (GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glMultiTexCoordP2uiv", [(GLenum, "texture"), (GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glMultiTexCoordP3ui", [(GLenum, "texture"), (GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glMultiTexCoordP3uiv", [(GLenum, "texture"), (GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glMultiTexCoordP4ui", [(GLenum, "texture"), (GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glMultiTexCoordP4uiv", [(GLenum, "texture"), (GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glNormalP3ui", [(GLenum, "type"), (GLuint, "coords")]),
    GlFunction(Void, "glNormalP3uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "coords")]),
    GlFunction(Void, "glColorP3ui", [(GLenum, "type"), (GLuint, "color")]),
    GlFunction(Void, "glColorP3uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "color")]),
    GlFunction(Void, "glColorP4ui", [(GLenum, "type"), (GLuint, "color")]),
    GlFunction(Void, "glColorP4uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "color")]),
    GlFunction(Void, "glSecondaryColorP3ui", [(GLenum, "type"), (GLuint, "color")]),
    GlFunction(Void, "glSecondaryColorP3uiv", [(GLenum, "type"), (Pointer(Const(GLuint)), "color")]),

    # GL_ARB_viewport_array
    GlFunction(Void, "glViewportArrayv", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "v")]),
    GlFunction(Void, "glViewportIndexedf", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "w"), (GLfloat, "h")]),
    GlFunction(Void, "glViewportIndexedfv", [(GLuint, "index"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glScissorArrayv", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "v")]),
    GlFunction(Void, "glScissorIndexed", [(GLuint, "index"), (GLint, "left"), (GLint, "bottom"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glScissorIndexedv", [(GLuint, "index"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glDepthRangeArrayv", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLdouble), "count*2"), "v")]),
    GlFunction(Void, "glDepthRangeIndexed", [(GLuint, "index"), (GLdouble, "n"), (GLdouble, "f")]),
    GlFunction(Void, "glGetFloati_v", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLfloat, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetDoublei_v", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLdouble, "_gl_param_size(target)"), "data")], sideeffects=False),

    # GL_ARB_window_pos
    GlFunction(Void, "glWindowPos2dARB", [(GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glWindowPos2dvARB", [(Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glWindowPos2fARB", [(GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glWindowPos2fvARB", [(Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glWindowPos2iARB", [(GLint, "x"), (GLint, "y")]),
    GlFunction(Void, "glWindowPos2ivARB", [(Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glWindowPos2sARB", [(GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glWindowPos2svARB", [(Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glWindowPos3dARB", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glWindowPos3dvARB", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glWindowPos3fARB", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glWindowPos3fvARB", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glWindowPos3iARB", [(GLint, "x"), (GLint, "y"), (GLint, "z")]),
    GlFunction(Void, "glWindowPos3ivARB", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glWindowPos3sARB", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glWindowPos3svARB", [(Array(Const(GLshort), 3), "v")]),

    # GL_ATI_draw_buffers
    GlFunction(Void, "glDrawBuffersATI", [(GLsizei, "n"), (Array(Const(GLenum), "n"), "bufs")]),

    # GL_ATI_element_array
    GlFunction(Void, "glElementPointerATI", [(GLenum, "type"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glDrawElementArrayATI", [(GLenum_mode, "mode"), (GLsizei, "count")]),
    GlFunction(Void, "glDrawRangeElementArrayATI", [(GLenum_mode, "mode"), (GLuint, "start"), (GLuint, "end"), (GLsizei, "count")]),

    # GL_ATI_envmap_bumpmap
    GlFunction(Void, "glTexBumpParameterivATI", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "param")]),
    GlFunction(Void, "glTexBumpParameterfvATI", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "param")]),
    GlFunction(Void, "glGetTexBumpParameterivATI", [(GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "param")], sideeffects=False),
    GlFunction(Void, "glGetTexBumpParameterfvATI", [(GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "param")], sideeffects=False),

    # GL_ATI_blend_equation_separate
    GlFunction(Void, "glBlendEquationSeparateATI", [(GLenum, "equationRGB"), (GLenum, "equationAlpha")]),

    # GL_ATI_fragment_shader
    GlFunction(Handle("fragmentShaderATI", GLuint, "range"), "glGenFragmentShadersATI", [(GLuint, "range")]),
    GlFunction(Void, "glBindFragmentShaderATI", [(GLfragmentShaderATI, "id")]),
    GlFunction(Void, "glDeleteFragmentShaderATI", [(GLfragmentShaderATI, "id")]),
    GlFunction(Void, "glBeginFragmentShaderATI", []),
    GlFunction(Void, "glEndFragmentShaderATI", []),
    GlFunction(Void, "glPassTexCoordATI", [(GLenum, "dst"), (GLenum, "coord"), (GLenum, "swizzle")]),
    GlFunction(Void, "glSampleMapATI", [(GLenum, "dst"), (GLenum, "interp"), (GLenum, "swizzle")]),
    GlFunction(Void, "glColorFragmentOp1ATI", [(GLenum, "op"), (GLenum, "dst"), (GLuint, "dstMask"), (GLuint, "dstMod"), (GLenum, "arg1"), (GLuint, "arg1Rep"), (GLuint, "arg1Mod")]),
    GlFunction(Void, "glColorFragmentOp2ATI", [(GLenum, "op"), (GLenum, "dst"), (GLuint, "dstMask"), (GLuint, "dstMod"), (GLenum, "arg1"), (GLuint, "arg1Rep"), (GLuint, "arg1Mod"), (GLenum, "arg2"), (GLuint, "arg2Rep"), (GLuint, "arg2Mod")]),
    GlFunction(Void, "glColorFragmentOp3ATI", [(GLenum, "op"), (GLenum, "dst"), (GLuint, "dstMask"), (GLuint, "dstMod"), (GLenum, "arg1"), (GLuint, "arg1Rep"), (GLuint, "arg1Mod"), (GLenum, "arg2"), (GLuint, "arg2Rep"), (GLuint, "arg2Mod"), (GLenum, "arg3"), (GLuint, "arg3Rep"), (GLuint, "arg3Mod")]),
    GlFunction(Void, "glAlphaFragmentOp1ATI", [(GLenum, "op"), (GLenum, "dst"), (GLuint, "dstMod"), (GLenum, "arg1"), (GLuint, "arg1Rep"), (GLuint, "arg1Mod")]),
    GlFunction(Void, "glAlphaFragmentOp2ATI", [(GLenum, "op"), (GLenum, "dst"), (GLuint, "dstMod"), (GLenum, "arg1"), (GLuint, "arg1Rep"), (GLuint, "arg1Mod"), (GLenum, "arg2"), (GLuint, "arg2Rep"), (GLuint, "arg2Mod")]),
    GlFunction(Void, "glAlphaFragmentOp3ATI", [(GLenum, "op"), (GLenum, "dst"), (GLuint, "dstMod"), (GLenum, "arg1"), (GLuint, "arg1Rep"), (GLuint, "arg1Mod"), (GLenum, "arg2"), (GLuint, "arg2Rep"), (GLuint, "arg2Mod"), (GLenum, "arg3"), (GLuint, "arg3Rep"), (GLuint, "arg3Mod")]),
    GlFunction(Void, "glSetFragmentShaderConstantATI", [(GLenum, "dst"), (Array(Const(GLfloat), 4), "value")]),

    # GL_ATI_map_object_buffer
    GlFunction(GLmap, "glMapObjectBufferATI", [(GLbuffer, "buffer")]),
    GlFunction(Void, "glUnmapObjectBufferATI", [(GLbuffer, "buffer")]),

    # GL_ATI_pn_triangles
    GlFunction(Void, "glPNTrianglesiATI", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glPNTrianglesfATI", [(GLenum, "pname"), (GLfloat, "param")]),

    # GL_ATIX_pn_triangles
    GlFunction(Void, "glPNTrianglesiATIX", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glPNTrianglesfATIX", [(GLenum, "pname"), (GLfloat, "param")]),

    # GL_ATI_separate_stencil
    GlFunction(Void, "glStencilOpSeparateATI", [(GLenum, "face"), (GLenum, "sfail"), (GLenum, "dpfail"), (GLenum, "dppass")]),
    GlFunction(Void, "glStencilFuncSeparateATI", [(GLenum, "frontfunc"), (GLenum, "backfunc"), (GLint, "ref"), (GLuint, "mask")]),

    # GL_ATI_vertex_array_object
    GlFunction(GLuint, "glNewObjectBufferATI", [(GLsizei, "size"), (Blob(Const(GLvoid), "size"), "pointer"), (GLenum, "usage")]),
    GlFunction(GLboolean, "glIsObjectBufferATI", [(GLuint, "buffer")], sideeffects=False),
    GlFunction(Void, "glUpdateObjectBufferATI", [(GLuint, "buffer"), (GLuint, "offset"), (GLsizei, "size"), (Blob(Const(GLvoid), "size"), "pointer"), (GLenum, "preserve")]),
    GlFunction(Void, "glGetObjectBufferfvATI", [(GLuint, "buffer"), (GLenum, "pname"), Out(Pointer(GLfloat), "params")], sideeffects=False),
    GlFunction(Void, "glGetObjectBufferivATI", [(GLuint, "buffer"), (GLenum, "pname"), Out(Pointer(GLint), "params")], sideeffects=False),
    GlFunction(Void, "glFreeObjectBufferATI", [(GLuint, "buffer")]),
    GlFunction(Void, "glArrayObjectATI", [(GLenum, "array"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLuint, "buffer"), (GLuint, "offset")]),
    GlFunction(Void, "glGetArrayObjectfvATI", [(GLenum, "array"), (GLenum, "pname"), Out(Pointer(GLfloat), "params")], sideeffects=False),
    GlFunction(Void, "glGetArrayObjectivATI", [(GLenum, "array"), (GLenum, "pname"), Out(Pointer(GLint), "params")], sideeffects=False),
    GlFunction(Void, "glVariantArrayObjectATI", [(GLuint, "id"), (GLenum, "type"), (GLsizei, "stride"), (GLuint, "buffer"), (GLuint, "offset")]),
    GlFunction(Void, "glGetVariantArrayObjectfvATI", [(GLuint, "id"), (GLenum, "pname"), Out(Pointer(GLfloat), "params")], sideeffects=False),
    GlFunction(Void, "glGetVariantArrayObjectivATI", [(GLuint, "id"), (GLenum, "pname"), Out(Pointer(GLint), "params")], sideeffects=False),

    # GL_ATI_vertex_attrib_array_object
    GlFunction(Void, "glVertexAttribArrayObjectATI", [(GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLboolean, "normalized"), (GLsizei, "stride"), (GLuint, "buffer"), (GLuint, "offset")]),
    GlFunction(Void, "glGetVertexAttribArrayObjectfvATI", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLfloat, "pname"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribArrayObjectivATI", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLint, "pname"), "params")], sideeffects=False),

    # GL_ATI_vertex_streams
    GlFunction(Void, "glVertexStream1sATI", [(GLenum, "stream"), (GLshort, "x")]),
    GlFunction(Void, "glVertexStream1svATI", [(GLenum, "stream"), (Pointer(Const(GLshort)), "coords")]),
    GlFunction(Void, "glVertexStream1iATI", [(GLenum, "stream"), (GLint, "x")]),
    GlFunction(Void, "glVertexStream1ivATI", [(GLenum, "stream"), (Pointer(Const(GLint)), "coords")]),
    GlFunction(Void, "glVertexStream1fATI", [(GLenum, "stream"), (GLfloat, "x")]),
    GlFunction(Void, "glVertexStream1fvATI", [(GLenum, "stream"), (Pointer(Const(GLfloat)), "coords")]),
    GlFunction(Void, "glVertexStream1dATI", [(GLenum, "stream"), (GLdouble, "x")]),
    GlFunction(Void, "glVertexStream1dvATI", [(GLenum, "stream"), (Pointer(Const(GLdouble)), "coords")]),
    GlFunction(Void, "glVertexStream2sATI", [(GLenum, "stream"), (GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glVertexStream2svATI", [(GLenum, "stream"), (Array(Const(GLshort), 2), "coords")]),
    GlFunction(Void, "glVertexStream2iATI", [(GLenum, "stream"), (GLint, "x"), (GLint, "y")]),
    GlFunction(Void, "glVertexStream2ivATI", [(GLenum, "stream"), (Array(Const(GLint), 2), "coords")]),
    GlFunction(Void, "glVertexStream2fATI", [(GLenum, "stream"), (GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glVertexStream2fvATI", [(GLenum, "stream"), (Array(Const(GLfloat), 2), "coords")]),
    GlFunction(Void, "glVertexStream2dATI", [(GLenum, "stream"), (GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glVertexStream2dvATI", [(GLenum, "stream"), (Array(Const(GLdouble), 2), "coords")]),
    GlFunction(Void, "glVertexStream3sATI", [(GLenum, "stream"), (GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glVertexStream3svATI", [(GLenum, "stream"), (Array(Const(GLshort), 3), "coords")]),
    GlFunction(Void, "glVertexStream3iATI", [(GLenum, "stream"), (GLint, "x"), (GLint, "y"), (GLint, "z")]),
    GlFunction(Void, "glVertexStream3ivATI", [(GLenum, "stream"), (Array(Const(GLint), 3), "coords")]),
    GlFunction(Void, "glVertexStream3fATI", [(GLenum, "stream"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glVertexStream3fvATI", [(GLenum, "stream"), (Array(Const(GLfloat), 3), "coords")]),
    GlFunction(Void, "glVertexStream3dATI", [(GLenum, "stream"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glVertexStream3dvATI", [(GLenum, "stream"), (Array(Const(GLdouble), 3), "coords")]),
    GlFunction(Void, "glVertexStream4sATI", [(GLenum, "stream"), (GLshort, "x"), (GLshort, "y"), (GLshort, "z"), (GLshort, "w")]),
    GlFunction(Void, "glVertexStream4svATI", [(GLenum, "stream"), (Array(Const(GLshort), 4), "coords")]),
    GlFunction(Void, "glVertexStream4iATI", [(GLenum, "stream"), (GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glVertexStream4ivATI", [(GLenum, "stream"), (Array(Const(GLint), 4), "coords")]),
    GlFunction(Void, "glVertexStream4fATI", [(GLenum, "stream"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glVertexStream4fvATI", [(GLenum, "stream"), (Array(Const(GLfloat), 4), "coords")]),
    GlFunction(Void, "glVertexStream4dATI", [(GLenum, "stream"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glVertexStream4dvATI", [(GLenum, "stream"), (Array(Const(GLdouble), 4), "coords")]),
    GlFunction(Void, "glNormalStream3bATI", [(GLenum, "stream"), (GLbyte, "nx"), (GLbyte, "ny"), (GLbyte, "nz")]),
    GlFunction(Void, "glNormalStream3bvATI", [(GLenum, "stream"), (Array(Const(GLbyte), 3), "coords")]),
    GlFunction(Void, "glNormalStream3sATI", [(GLenum, "stream"), (GLshort, "nx"), (GLshort, "ny"), (GLshort, "nz")]),
    GlFunction(Void, "glNormalStream3svATI", [(GLenum, "stream"), (Array(Const(GLshort), 3), "coords")]),
    GlFunction(Void, "glNormalStream3iATI", [(GLenum, "stream"), (GLint, "nx"), (GLint, "ny"), (GLint, "nz")]),
    GlFunction(Void, "glNormalStream3ivATI", [(GLenum, "stream"), (Array(Const(GLint), 3), "coords")]),
    GlFunction(Void, "glNormalStream3fATI", [(GLenum, "stream"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz")]),
    GlFunction(Void, "glNormalStream3fvATI", [(GLenum, "stream"), (Array(Const(GLfloat), 3), "coords")]),
    GlFunction(Void, "glNormalStream3dATI", [(GLenum, "stream"), (GLdouble, "nx"), (GLdouble, "ny"), (GLdouble, "nz")]),
    GlFunction(Void, "glNormalStream3dvATI", [(GLenum, "stream"), (Array(Const(GLdouble), 3), "coords")]),
    GlFunction(Void, "glClientActiveVertexStreamATI", [(GLenum, "stream")]),
    GlFunction(Void, "glVertexBlendEnviATI", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glVertexBlendEnvfATI", [(GLenum, "pname"), (GLfloat, "param")]),

    # GL_EXT_base_instance
    GlFunction(Void, "glDrawArraysInstancedBaseInstanceEXT", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count"), (GLsizei, "instancecount"), (GLuint, "baseinstance")]),
    GlFunction(Void, "glDrawElementsInstancedBaseInstanceEXT", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount"), (GLuint, "baseinstance")]),
    GlFunction(Void, "glDrawElementsInstancedBaseVertexBaseInstanceEXT", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount"), (GLint, "basevertex"), (GLuint, "baseinstance")]),

    # GL_EXT_bindable_uniform
    GlFunction(Void, "glUniformBufferEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLbuffer, "buffer")]),
    GlFunction(GLint, "glGetUniformBufferSizeEXT", [(GLprogram, "program"), (GLlocation, "location")]),
    GlFunction(GLintptr, "glGetUniformOffsetEXT", [(GLprogram, "program"), (GLlocation, "location")]),

    # GL_EXT_blend_color
    GlFunction(Void, "glBlendColorEXT", [(GLfloat, "red"), (GLfloat, "green"), (GLfloat, "blue"), (GLfloat, "alpha")]),

    # GL_EXT_blend_equation_separate
    GlFunction(Void, "glBlendEquationSeparateEXT", [(GLenum, "modeRGB"), (GLenum, "modeAlpha")]),

    # GL_EXT_blend_func_extended
    GlFunction(Void, "glBindFragDataLocationIndexedEXT", [(GLprogram, "program"), (GLuint, "colorNumber"), (GLuint, "index"), (GLstringConst, "name")]),
    GlFunction(Void, "glBindFragDataLocationEXT", [(GLprogram, "program"), (GLuint, "color"), (GLstringConst, "name")]),
    GlFunction(GLlocation, "glGetProgramResourceLocationIndexEXT", [(GLprogram, "program"), (GLenum, "programInterface"), (GLstringConst, "name")]),
    GlFunction(GLint, "glGetFragDataIndexEXT", [(GLprogram, "program"), (GLstringConst, "name")]),

    # GL_EXT_blend_func_separate
    GlFunction(Void, "glBlendFuncSeparateEXT", [(GLenum, "sfactorRGB"), (GLenum, "dfactorRGB"), (GLenum, "sfactorAlpha"), (GLenum, "dfactorAlpha")]),

    # GL_EXT_blend_minmax
    GlFunction(Void, "glBlendEquationEXT", [(GLenum, "mode")]),

    # GL_EXT_buffer_storage
    GlFunction(Void, "glBufferStorageEXT", [(GLenum, "target"), (GLsizeiptr, "size"), (Blob(Const(Void), "size"), "data"), (GLbitfield_storage, "flags")]),

    # GL_EXT_clear_texture
    GlFunction(Void, "glClearTexImageEXT", [ (GLtexture, "texture"), (GLint, "level"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glClearBufferData_size(format, type)"), "data")]),
    GlFunction(Void, "glClearTexSubImageEXT", [ (GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glClearBufferData_size(format, type)"), "data")]),

    # GL_EXT_clip_control
    GlFunction(Void, "glClipControlEXT", [(GLenum, "origin"), (GLenum, "depth")]),
    
    # GL_EXT_color_subtable
    GlFunction(Void, "glColorSubTableEXT", [(GLenum, "target"), (GLsizei, "start"), (GLsizei, "count"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glColorSubTable_size(format, type, count)"), "data")]),
    GlFunction(Void, "glCopyColorSubTableEXT", [(GLenum, "target"), (GLsizei, "start"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),

    # GL_EXT_compiled_vertex_array
    GlFunction(Void, "glLockArraysEXT", [(GLint, "first"), (GLsizei, "count")]),
    GlFunction(Void, "glUnlockArraysEXT", []),

    # GL_EXT_convolution
    GlFunction(Void, "glConvolutionFilter1DEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glConvolutionFilter1D_size(format, type, width)"), "image")]),
    GlFunction(Void, "glConvolutionFilter2DEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glConvolutionFilter2D_size(format, type, width, height)"), "image")]),
    GlFunction(Void, "glConvolutionParameterfEXT", [(GLenum, "target"), (GLenum, "pname"), (GLfloat, "params")]),
    GlFunction(Void, "glConvolutionParameterfvEXT", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glConvolutionParameteriEXT", [(GLenum, "target"), (GLenum, "pname"), (GLint, "params")]),
    GlFunction(Void, "glConvolutionParameterivEXT", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glCopyConvolutionFilter1DEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glCopyConvolutionFilter2DEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glGetConvolutionFilterEXT", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetConvolutionFilterEXT_size(target, format, type)"), "image")]),
    GlFunction(Void, "glGetConvolutionParameterfvEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetConvolutionParameterivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetSeparableFilterEXT", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetSeparableFilterEXT_size(target, format, type)"), "row"), Out(OpaqueBlob(GLvoid, "_glGetSeparableFilterEXT_size(target, format, type)"), "column"), Out(OpaqueBlob(GLvoid, "_glGetSeparableFilterEXT_size(target, format, type)"), "span")]),
    GlFunction(Void, "glSeparableFilter2DEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glConvolutionFilter1D_size(format, type, width)"), "row"), (Blob(Const(GLvoid), "_glConvolutionFilter1D_size(format, type, height)"), "column")]),

    # GL_EXT_coordinate_frame
    GlFunction(Void, "glTangent3bEXT", [(GLbyte, "tx"), (GLbyte, "ty"), (GLbyte, "tz")]),
    GlFunction(Void, "glTangent3bvEXT", [(Array(Const(GLbyte), 3), "v")]),
    GlFunction(Void, "glTangent3dEXT", [(GLdouble, "tx"), (GLdouble, "ty"), (GLdouble, "tz")]),
    GlFunction(Void, "glTangent3dvEXT", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glTangent3fEXT", [(GLfloat, "tx"), (GLfloat, "ty"), (GLfloat, "tz")]),
    GlFunction(Void, "glTangent3fvEXT", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glTangent3iEXT", [(GLint, "tx"), (GLint, "ty"), (GLint, "tz")]),
    GlFunction(Void, "glTangent3ivEXT", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glTangent3sEXT", [(GLshort, "tx"), (GLshort, "ty"), (GLshort, "tz")]),
    GlFunction(Void, "glTangent3svEXT", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glBinormal3bEXT", [(GLbyte, "bx"), (GLbyte, "by"), (GLbyte, "bz")]),
    GlFunction(Void, "glBinormal3bvEXT", [(Array(Const(GLbyte), 3), "v")]),
    GlFunction(Void, "glBinormal3dEXT", [(GLdouble, "bx"), (GLdouble, "by"), (GLdouble, "bz")]),
    GlFunction(Void, "glBinormal3dvEXT", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glBinormal3fEXT", [(GLfloat, "bx"), (GLfloat, "by"), (GLfloat, "bz")]),
    GlFunction(Void, "glBinormal3fvEXT", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glBinormal3iEXT", [(GLint, "bx"), (GLint, "by"), (GLint, "bz")]),
    GlFunction(Void, "glBinormal3ivEXT", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glBinormal3sEXT", [(GLshort, "bx"), (GLshort, "by"), (GLshort, "bz")]),
    GlFunction(Void, "glBinormal3svEXT", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glTangentPointerEXT", [(GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glBinormalPointerEXT", [(GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),

    # GL_EXT_copy_image
    GlFunction(Void, "glCopyImageSubDataEXT", [(GLtexture, "srcName"), (GLenum, "srcTarget"), (GLint, "srcLevel"), (GLint, "srcX"), (GLint, "srcY"), (GLint, "srcZ"), (GLtexture, "dstName"), (GLenum, "dstTarget"), (GLint, "dstLevel"), (GLint, "dstX"), (GLint, "dstY"), (GLint, "dstZ"), (GLsizei, "srcWidth"), (GLsizei, "srcHeight"), (GLsizei, "srcDepth")]),

    # GL_EXT_copy_texture
    GlFunction(Void, "glCopyTexImage1DEXT", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLint, "border")]),
    GlFunction(Void, "glCopyTexImage2DEXT", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border")]),
    GlFunction(Void, "glCopyTexSubImage1DEXT", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glCopyTexSubImage2DEXT", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glCopyTexSubImage3DEXT", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),

    # GL_EXT_cull_vertex
    GlFunction(Void, "glCullParameterdvEXT", [(GLenum, "pname"), (Array(GLdouble, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glCullParameterfvEXT", [(GLenum, "pname"), (Array(GLfloat, "_gl_param_size(pname)"), "params")]),

    # GL_EXT_debug_label
    GlFunction(Void, "glLabelObjectEXT", [(GLenum, "type"), (GLuint, "object"), (GLsizei, "length"), (GLstringConst, "label")]),
    GlFunction(Void, "glGetObjectLabelEXT", [(GLenum, "type"), (GLuint, "object"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(GLstring, "label")], sideeffects=False),

    # GL_EXT_debug_marker
    GlFunction(Void, "glInsertEventMarkerEXT", [(GLsizei, "length"), (String(Const(GLchar), "length ? length : strlen(marker)"), "marker")], sideeffects=True),
    GlFunction(Void, "glPushGroupMarkerEXT", [(GLsizei, "length"), (String(Const(GLchar), "length ? length : strlen(marker)"), "marker")], sideeffects=True),
    GlFunction(Void, "glPopGroupMarkerEXT", [], sideeffects=True),

    # GL_EXT_depth_bounds_test
    GlFunction(Void, "glDepthBoundsEXT", [(GLclampd, "zmin"), (GLclampd, "zmax")]),

    # GL_EXT_direct_state_access
    GlFunction(Void, "glBindMultiTextureEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLtexture, "texture")]),
    GlFunction(GLenum, "glCheckNamedFramebufferStatusEXT", [(GLframebuffer, "framebuffer"), (GLenum, "target")]),
    GlFunction(Void, "glClearNamedBufferDataEXT", [(GLbuffer, "buffer"), (GLenum, "internalformat"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glClearBufferData_size(format, type)"), "data")]),
    GlFunction(Void, "glClearNamedBufferSubDataEXT", [(GLbuffer, "buffer"), (GLenum, "internalformat"), (GLsizeiptr, "offset"), (GLsizeiptr, "size"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(Void), "_glClearBufferData_size(format, type)"), "data")]),
    GlFunction(Void, "glClientAttribDefaultEXT", [(GLbitfield_client_attrib, "mask")]),
    GlFunction(Void, "glCompressedMultiTexImage1DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "imageSize"), "bits")]),
    GlFunction(Void, "glCompressedMultiTexImage2DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "imageSize"), "bits")]),
    GlFunction(Void, "glCompressedMultiTexImage3DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "imageSize"), "bits")]),
    GlFunction(Void, "glCompressedMultiTexSubImage1DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "imageSize"), "bits")]),
    GlFunction(Void, "glCompressedMultiTexSubImage2DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "imageSize"), "bits")]),
    GlFunction(Void, "glCompressedMultiTexSubImage3DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "imageSize"), "bits")]),
    GlFunction(Void, "glCompressedTextureImage1DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(bits, internalformat, width, 0, 0, imageSize, can_unpack_subimage(), {})"), "bits")]),
    GlFunction(Void, "glCompressedTextureImage2DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(bits, internalformat, width, height, 0, imageSize, can_unpack_subimage(), {})"), "bits")]),
    GlFunction(Void, "glCompressedTextureImage3DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(bits, internalformat, width, height, depth, imageSize, can_unpack_subimage(), {})"), "bits")]),
    GlFunction(Void, "glCompressedTextureSubImage1DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(bits, format, width, 0, 0, imageSize, can_unpack_subimage(), {})"), "bits")]),
    GlFunction(Void, "glCompressedTextureSubImage2DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(bits, format, width, height, 0, imageSize, can_unpack_subimage(), {})"), "bits")]),
    GlFunction(Void, "glCompressedTextureSubImage3DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(bits, format, width, height, depth, imageSize, can_unpack_subimage(), {})"), "bits")]),
    GlFunction(Void, "glCopyMultiTexImage1DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLint, "border")]),
    GlFunction(Void, "glCopyMultiTexImage2DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border")]),
    GlFunction(Void, "glCopyMultiTexSubImage1DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glCopyMultiTexSubImage2DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glCopyMultiTexSubImage3DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glCopyTextureImage1DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLint, "border")]),
    GlFunction(Void, "glCopyTextureImage2DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border")]),
    GlFunction(Void, "glCopyTextureSubImage1DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glCopyTextureSubImage2DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glCopyTextureSubImage3DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glDisableClientStateIndexedEXT", [(GLenum, "array"), (GLuint, "index")]),
    GlFunction(Void, "glDisableClientStateiEXT", [(GLenum, "array"), (GLuint, "index")]),
    #GlFunction(Void, "glDisableIndexedEXT", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(Void, "glDisableVertexArrayAttribEXT", [(GLarray, "vaobj"), (GLuint, "index")]),
    GlFunction(Void, "glDisableVertexArrayEXT", [(GLarray, "vaobj"), (GLenum, "array")]),
    GlFunction(Void, "glEnableClientStateIndexedEXT", [(GLenum, "array"), (GLuint, "index")]),
    GlFunction(Void, "glEnableClientStateiEXT", [(GLenum, "array"), (GLuint, "index")]),
    #GlFunction(Void, "glEnableIndexedEXT", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(Void, "glEnableVertexArrayAttribEXT", [(GLarray, "vaobj"), (GLuint, "index")]),
    GlFunction(Void, "glEnableVertexArrayEXT", [(GLarray, "vaobj"), (GLenum, "array")]),
    GlFunction(Void, "glFlushMappedNamedBufferRangeEXT", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "length")]),
    GlFunction(Void, "glFramebufferDrawBufferEXT", [(GLframebuffer, "framebuffer"), (GLenum, "mode")]),
    GlFunction(Void, "glFramebufferDrawBuffersEXT", [(GLframebuffer, "framebuffer"), (GLsizei, "n"), (Array(Const(GLenum), "n"), "bufs")]),
    GlFunction(Void, "glFramebufferReadBufferEXT", [(GLframebuffer, "framebuffer"), (GLenum, "mode")]),
    GlFunction(Void, "glGenerateMultiTexMipmapEXT", [(GLenum, "texunit"), (GLenum, "target")]),
    GlFunction(Void, "glGenerateTextureMipmapEXT", [(GLtexture, "texture"), (GLenum, "target")]),
    #GlFunction(Void, "glGetBooleanIndexedvEXT", [(GLenum, "target"), (GLuint, "index"), (Array(GLboolean, "COMPSIZE(target)"), "data")]),
    GlFunction(Void, "glGetCompressedMultiTexImageEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "lod"), Out(OpaqueBlob(GLvoid, "_glGetCompressedMultiTexImageEXT_size(target, lod)"), "img")]),
    GlFunction(Void, "glGetCompressedTextureImageEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "lod"), Out(OpaqueBlob(GLvoid, "_glGetCompressedTextureImageEXT_size(target, lod)"), "img")]),
    GlFunction(Void, "glGetDoubleIndexedvEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLdouble, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetDoublei_vEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLdouble, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetFloatIndexedvEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLfloat, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetFloati_vEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLfloat, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetFramebufferParameterivEXT", [(GLframebuffer, "framebuffer"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    #GlFunction(Void, "glGetIntegerIndexedvEXT", [(GLenum, "target"), (GLuint, "index"), (Array(GLint, "COMPSIZE(target)"), "data")]),
    GlFunction(Void, "glGetMultiTexEnvfvEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexEnvivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexGendvEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexGenfvEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexGenivEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexImageEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetMultiTexImageEXT_size(target, level, format, type)"), "pixels")]),
    GlFunction(Void, "glGetMultiTexLevelParameterfvEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexLevelParameterivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexParameterIivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexParameterIuivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexParameterfvEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMultiTexParameterivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedBufferParameterivEXT", [(GLbuffer, "buffer"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedBufferPointervEXT", [(GLbuffer, "buffer"), (GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedBufferSubDataEXT", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size"), Out(OpaqueBlob(GLvoid, "size"), "data")], sideeffects=False),
    GlFunction(Void, "glGetNamedFramebufferAttachmentParameterivEXT", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedFramebufferParameterivEXT", [(GLframebuffer, "framebuffer"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedProgramLocalParameterIivEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), Out(Array(GLint, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedProgramLocalParameterIuivEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), Out(Array(GLuint, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedProgramLocalParameterdvEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), Out(Array(GLdouble, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedProgramLocalParameterfvEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), Out(Array(GLfloat, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedProgramStringEXT", [(GLprogram, "program"), (GLenum, "target"), (GLenum, "pname"), Out(OpaqueBlob(GLvoid, "_glGetNamedProgramStringEXT_size(program,pname)"), "string")], sideeffects=False),
    GlFunction(Void, "glGetNamedProgramivEXT", [(GLprogram, "program"), (GLenum, "target"), (GLenum, "pname"), Out(Pointer(GLint), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedRenderbufferParameterivEXT", [(GLrenderbuffer, "renderbuffer"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetPointerIndexedvEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLpointer, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetPointeri_vEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLpointer, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetTextureImageEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum, "format"), (GLenum, "type"), Out(GLpointer, "pixels")]),
    GlFunction(Void, "glGetTextureLevelParameterfvEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureLevelParameterivEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureParameterIivEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureParameterIuivEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureParameterfvEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTextureParameterivEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexArrayIntegeri_vEXT", [(GLarray, "vaobj"), (GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLint), "param")], sideeffects=False),
    GlFunction(Void, "glGetVertexArrayIntegervEXT", [(GLarray, "vaobj"), (GLenum, "pname"), Out(Pointer(GLint), "param")], sideeffects=False),
    GlFunction(Void, "glGetVertexArrayPointeri_vEXT", [(GLarray, "vaobj"), (GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLpointer), "param")], sideeffects=False),
    GlFunction(Void, "glGetVertexArrayPointervEXT", [(GLarray, "vaobj"), (GLenum, "pname"), Out(Pointer(GLpointer), "param")], sideeffects=False),
    #GlFunction(GLboolean, "glIsEnabledIndexedEXT", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(GLmap, "glMapNamedBufferEXT", [(GLbuffer, "buffer"), (GLenum, "access")]),
    GlFunction(GLmap, "glMapNamedBufferRangeEXT", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "length"), (GLbitfield_access, "access")]),
    GlFunction(Void, "glMatrixFrustumEXT", [(GLenum, "mode"), (GLdouble, "left"), (GLdouble, "right"), (GLdouble, "bottom"), (GLdouble, "top"), (GLdouble, "zNear"), (GLdouble, "zFar")]),
    GlFunction(Void, "glMatrixLoadIdentityEXT", [(GLenum, "mode")]),
    GlFunction(Void, "glMatrixLoadTransposedEXT", [(GLenum, "mode"), (Array(Const(GLdouble), 16), "m")]),
    GlFunction(Void, "glMatrixLoadTransposefEXT", [(GLenum, "mode"), (Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glMatrixLoaddEXT", [(GLenum, "mode"), (Array(Const(GLdouble), 16), "m")]),
    GlFunction(Void, "glMatrixLoadfEXT", [(GLenum, "mode"), (Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glMatrixMultTransposedEXT", [(GLenum, "mode"), (Array(Const(GLdouble), 16), "m")]),
    GlFunction(Void, "glMatrixMultTransposefEXT", [(GLenum, "mode"), (Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glMatrixMultdEXT", [(GLenum, "mode"), (Array(Const(GLdouble), 16), "m")]),
    GlFunction(Void, "glMatrixMultfEXT", [(GLenum, "mode"), (Array(Const(GLfloat), 16), "m")]),
    GlFunction(Void, "glMatrixOrthoEXT", [(GLenum, "mode"), (GLdouble, "left"), (GLdouble, "right"), (GLdouble, "bottom"), (GLdouble, "top"), (GLdouble, "zNear"), (GLdouble, "zFar")]),
    GlFunction(Void, "glMatrixPopEXT", [(GLenum, "mode")]),
    GlFunction(Void, "glMatrixPushEXT", [(GLenum, "mode")]),
    GlFunction(Void, "glMatrixRotatedEXT", [(GLenum, "mode"), (GLdouble, "angle"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glMatrixRotatefEXT", [(GLenum, "mode"), (GLfloat, "angle"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glMatrixScaledEXT", [(GLenum, "mode"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glMatrixScalefEXT", [(GLenum, "mode"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glMatrixTranslatedEXT", [(GLenum, "mode"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glMatrixTranslatefEXT", [(GLenum, "mode"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glMultiTexBufferEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "internalformat"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glMultiTexCoordPointerEXT", [(GLenum, "texunit"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glMultiTexEnvfEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glMultiTexEnvfvEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexEnviEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glMultiTexEnvivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexGendEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), (GLdouble, "param")]),
    GlFunction(Void, "glMultiTexGendvEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLdouble), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexGenfEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glMultiTexGenfvEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexGeniEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glMultiTexGenivEXT", [(GLenum, "texunit"), (GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexImage1DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage1D_size(format, type, width)"), "pixels")]),
    GlFunction(Void, "glMultiTexImage2DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage2D_size(format, type, width, height)"), "pixels")]),
    GlFunction(Void, "glMultiTexImage3DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glMultiTexParameterIivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexParameterIuivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLuint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexParameterfEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glMultiTexParameterfvEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexParameteriEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glMultiTexParameterivEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glMultiTexRenderbufferEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glMultiTexSubImage1DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage1D_size(format, type, width)"), "pixels")]),
    GlFunction(Void, "glMultiTexSubImage2DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage2D_size(format, type, width, height)"), "pixels")]),
    GlFunction(Void, "glMultiTexSubImage3DEXT", [(GLenum, "texunit"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glNamedBufferDataEXT", [(GLbuffer, "buffer"), (GLsizeiptr, "size"), (Blob(Const(GLvoid), "size"), "data"), (GLenum, "usage")]),
    GlFunction(Void, "glNamedBufferStorageEXT", [ (GLbuffer, "buffer"), (GLsizeiptr, "size"), (Blob(Const(GLvoid), "size"), "data"), (GLbitfield_storage, "flags")]),
    GlFunction(Void, "glNamedBufferSubDataEXT", [(GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size"), (Blob(Const(GLvoid), "size"), "data")]),
    GlFunction(Void, "glNamedCopyBufferSubDataEXT", [(GLbuffer, "readBuffer"), (GLbuffer, "writeBuffer"), (GLintptr, "readOffset"), (GLintptr, "writeOffset"), (GLsizeiptr, "size")]),
    GlFunction(Void, "glNamedFramebufferParameteriEXT", [(GLframebuffer, "framebuffer"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glNamedFramebufferRenderbufferEXT", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLenum, "renderbuffertarget"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glNamedFramebufferTexture1DEXT", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glNamedFramebufferTexture2DEXT", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glNamedFramebufferTexture3DEXT", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level"), (GLint, "zoffset")]),
    GlFunction(Void, "glNamedFramebufferTextureEXT", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glNamedFramebufferTextureFaceEXT", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLenum, "face")]),
    GlFunction(Void, "glNamedFramebufferTextureLayerEXT", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLint, "layer")]),
    GlFunction(Void, "glNamedProgramLocalParameter4dEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glNamedProgramLocalParameter4dvEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (Array(Const(GLdouble), 4), "params")]),
    GlFunction(Void, "glNamedProgramLocalParameter4fEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glNamedProgramLocalParameter4fvEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (Array(Const(GLfloat), 4), "params")]),
    GlFunction(Void, "glNamedProgramLocalParameterI4iEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glNamedProgramLocalParameterI4ivEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (Array(Const(GLint), 4), "params")]),
    GlFunction(Void, "glNamedProgramLocalParameterI4uiEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (GLuint, "x"), (GLuint, "y"), (GLuint, "z"), (GLuint, "w")]),
    GlFunction(Void, "glNamedProgramLocalParameterI4uivEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (Array(Const(GLuint), 4), "params")]),
    GlFunction(Void, "glNamedProgramLocalParameters4fvEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "params")]),
    GlFunction(Void, "glNamedProgramLocalParametersI4ivEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "params")]),
    GlFunction(Void, "glNamedProgramLocalParametersI4uivEXT", [(GLprogram, "program"), (GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLuint), "count*4"), "params")]),
    GlFunction(Void, "glNamedProgramStringEXT", [(GLprogram, "program"), (GLenum, "target"), (GLenum, "format"), (GLsizei, "len"), (String(Const(GLvoid), "len"), "string")]),
    GlFunction(Void, "glNamedRenderbufferStorageEXT", [(GLrenderbuffer, "renderbuffer"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glNamedRenderbufferStorageMultisampleCoverageEXT", [(GLrenderbuffer, "renderbuffer"), (GLsizei, "coverageSamples"), (GLsizei, "colorSamples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glNamedRenderbufferStorageMultisampleEXT", [(GLrenderbuffer, "renderbuffer"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glProgramUniform1dEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLdouble, "x")]),
    GlFunction(Void, "glProgramUniform1dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count"), "value")]),
    GlFunction(Void, "glProgramUniform1fEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLfloat, "v0")]),
    GlFunction(Void, "glProgramUniform1fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count"), "value")]),
    GlFunction(Void, "glProgramUniform1iEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLint, "v0")]),
    GlFunction(Void, "glProgramUniform1ivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count"), "value")]),
    GlFunction(Void, "glProgramUniform1uiEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLuint, "v0")]),
    GlFunction(Void, "glProgramUniform1uivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "value")]),
    GlFunction(Void, "glProgramUniform2dEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glProgramUniform2dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform2fEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1")]),
    GlFunction(Void, "glProgramUniform2fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform2iEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLint, "v0"), (GLint, "v1")]),
    GlFunction(Void, "glProgramUniform2ivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform2uiEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1")]),
    GlFunction(Void, "glProgramUniform2uivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform3dEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glProgramUniform3dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform3fEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1"), (GLfloat, "v2")]),
    GlFunction(Void, "glProgramUniform3fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform3iEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLint, "v0"), (GLint, "v1"), (GLint, "v2")]),
    GlFunction(Void, "glProgramUniform3ivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform3uiEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1"), (GLuint, "v2")]),
    GlFunction(Void, "glProgramUniform3uivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform4dEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glProgramUniform4dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLdouble), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniform4fEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLfloat, "v0"), (GLfloat, "v1"), (GLfloat, "v2"), (GLfloat, "v3")]),
    GlFunction(Void, "glProgramUniform4fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniform4iEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLint, "v0"), (GLint, "v1"), (GLint, "v2"), (GLint, "v3")]),
    GlFunction(Void, "glProgramUniform4ivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniform4uiEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1"), (GLuint, "v2"), (GLuint, "v3")]),
    GlFunction(Void, "glProgramUniform4uivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2x3dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2x3fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2x4dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*2*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix2x4fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*2*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3x2dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3x2fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3x4dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*3*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix3x4fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*3*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*4"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4x2dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4x2fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*2"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4x3dvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLdouble), "count*4*3"), "value")]),
    GlFunction(Void, "glProgramUniformMatrix4x3fvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (GLboolean, "transpose"), (Array(Const(GLfloat), "count*4*3"), "value")]),
    GlFunction(Void, "glPushClientAttribDefaultEXT", [(GLbitfield_client_attrib, "mask")]),
    GlFunction(Void, "glTextureBufferEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "internalformat"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glTextureBufferRangeEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "internalformat"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size")]),
    GlFunction(Void, "glTextureImage1DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage1D_size(format, type, width)"), "pixels")]),
    GlFunction(Void, "glTextureImage2DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage2D_size(format, type, width, height)"), "pixels")]),
    GlFunction(Void, "glTextureImage3DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLenum_int, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glTexturePageCommitmentEXT", [(GLtexture, "texture"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "commit")]),
    GlFunction(Void, "glTextureParameterIivEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTextureParameterIuivEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLuint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTextureParameterfEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glTextureParameterfvEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTextureParameteriEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glTextureParameterivEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTextureRenderbufferEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glTextureStorage1DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width")]),
    GlFunction(Void, "glTextureStorage2DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glTextureStorage2DMultisampleEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLboolean, "fixedsamplelocations")]),
    GlFunction(Void, "glTextureStorage3DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth")]),
    GlFunction(Void, "glTextureStorage3DMultisampleEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "fixedsamplelocations")]),
    GlFunction(Void, "glTextureSubImage1DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage1D_size(format, type, width)"), "pixels")]),
    GlFunction(Void, "glTextureSubImage2DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage2D_size(format, type, width, height)"), "pixels")]),
    GlFunction(Void, "glTextureSubImage3DEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(GLboolean, "glUnmapNamedBufferEXT", [(GLbuffer, "buffer")]),
    GlFunction(Void, "glVertexArrayBindVertexBufferEXT", [(GLarray, "vaobj"), (GLuint, "bindingindex"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizei, "stride")]),
    GlFunction(Void, "glVertexArrayColorOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayEdgeFlagOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayFogCoordOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayIndexOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayMultiTexCoordOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLenum, "texunit"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayNormalOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArraySecondaryColorOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayTexCoordOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayVertexAttribBindingEXT", [(GLarray, "vaobj"), (GLuint, "attribindex"), (GLuint, "bindingindex")]),
    GlFunction(Void, "glVertexArrayVertexAttribDivisorEXT", [(GLarray, "vaobj"), (GLuint, "index"), (GLuint, "divisor")]),
    GlFunction(Void, "glVertexArrayVertexAttribFormatEXT", [(GLarray, "vaobj"), (GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLboolean, "normalized"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexArrayVertexAttribIFormatEXT", [(GLarray, "vaobj"), (GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexArrayVertexAttribIOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayVertexAttribLFormatEXT", [(GLarray, "vaobj"), (GLuint, "attribindex"), (GLint, "size"), (GLenum, "type"), (GLuint, "relativeoffset")]),
    GlFunction(Void, "glVertexArrayVertexAttribLOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayVertexAttribOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLboolean, "normalized"), (GLsizei, "stride"), (GLintptr, "offset")]),
    GlFunction(Void, "glVertexArrayVertexBindingDivisorEXT", [(GLarray, "vaobj"), (GLuint, "bindingindex"), (GLuint, "divisor")]),
    GlFunction(Void, "glVertexArrayVertexOffsetEXT", [(GLarray, "vaobj"), (GLbuffer, "buffer"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLintptr, "offset")]),

    # GL_EXT_discard_framebuffer
    GlFunction(Void, "glDiscardFramebufferEXT", [(GLenum, "target"), (GLsizei, "numAttachments"), (Array(Const(GLenum), "numAttachments"), "attachments")]),

    # GL_EXT_disjoint_timer_query
    GlFunction(Void, "glGenQueriesEXT", [(GLsizei, "n"), Out(Array(GLquery, "n"), "ids")]),
    GlFunction(Void, "glDeleteQueriesEXT", [(GLsizei, "n"), (Array(Const(GLquery), "n"), "ids")]),
    GlFunction(GLboolean, "glIsQueryEXT", [(GLquery, "id")], sideeffects=False),
    GlFunction(Void, "glBeginQueryEXT", [(GLenum, "target"), (GLquery, "id")]),
    GlFunction(Void, "glEndQueryEXT", [(GLenum, "target")]),
    GlFunction(Void, "glQueryCounterEXT", [(GLquery, "id"), (GLenum, "target")]),
    GlFunction(Void, "glGetQueryivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetQueryObjectivEXT", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjectuivEXT", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjecti64vEXT", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLint64, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetQueryObjectui64vEXT", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLuint64, "_gl_param_size(pname)"), "params")]),

    # GL_EXT_draw_buffers
    GlFunction(Void, "glDrawBuffersEXT", [(GLsizei, "n"), (Array(Const(GLenum), "n"), "bufs")]),

    # GL_EXT_draw_buffers2
    GlFunction(Void, "glColorMaskIndexedEXT", [(GLuint, "index"), (GLboolean, "r"), (GLboolean, "g"), (GLboolean, "b"), (GLboolean, "a")]),
    GlFunction(Void, "glGetBooleanIndexedvEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLboolean, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetIntegerIndexedvEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLint, "_gl_param_size(target)"), "data")], sideeffects=False),
    GlFunction(Void, "glEnableIndexedEXT", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(Void, "glDisableIndexedEXT", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(GLboolean, "glIsEnabledIndexedEXT", [(GLenum, "target"), (GLuint, "index")], sideeffects=False),

    # GL_EXT_draw_buffers_indexed
    GlFunction(Void, "glEnableiEXT", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(Void, "glDisableiEXT", [(GLenum, "target"), (GLuint, "index")]),
    GlFunction(Void, "glBlendEquationiEXT", [(GLuint, "buf"), (GLenum, "mode")]),
    GlFunction(Void, "glBlendEquationSeparateiEXT", [(GLuint, "buf"), (GLenum, "modeRGB"), (GLenum, "modeAlpha")]),
    GlFunction(Void, "glBlendFunciEXT", [(GLuint, "buf"), (GLenum, "src"), (GLenum, "dst")]),
    GlFunction(Void, "glBlendFuncSeparateiEXT", [(GLuint, "buf"), (GLenum, "srcRGB"), (GLenum, "dstRGB"), (GLenum, "srcAlpha"), (GLenum, "dstAlpha")]),
    GlFunction(Void, "glColorMaskiEXT", [(GLuint, "index"), (GLboolean, "r"), (GLboolean, "g"), (GLboolean, "b"), (GLboolean, "a")]),
    GlFunction(GLboolean, "glIsEnablediEXT", [(GLenum, "target"), (GLuint, "index")], sideeffects=False),

    # GL_EXT_draw_elements_base_vertex
    GlFunction(Void, "glDrawElementsBaseVertexEXT", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLint, "basevertex")]),
    GlFunction(Void, "glDrawRangeElementsBaseVertexEXT", [(GLenum_mode, "mode"), (GLuint, "start"), (GLuint, "end"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLint, "basevertex")]),
    GlFunction(Void, "glDrawElementsInstancedBaseVertexEXT", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount"), (GLint, "basevertex")]),
    GlFunction(Void, "glMultiDrawElementsBaseVertexEXT", [(GLenum_mode, "mode"), (Array(Const(GLsizei), "drawcount"), "count"), (GLenum, "type"), (Array(Const(GLindexBuffer("count[{i}]", "type")), "drawcount"), "indices"), (GLsizei, "drawcount"), (Array(Const(GLint), "drawcount"), "basevertex")]),

    # GL_EXT_draw_instanced
    GlFunction(Void, "glDrawArraysInstancedEXT", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count"), (GLsizei, "instancecount")]),
    GlFunction(Void, "glDrawElementsInstancedEXT", [(GLenum_mode, "mode"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices"), (GLsizei, "instancecount")]),

    # GL_EXT_draw_range_elements
    GlFunction(Void, "glDrawRangeElementsEXT", [(GLenum_mode, "mode"), (GLuint, "start"), (GLuint, "end"), (GLsizei, "count"), (GLenum, "type"), (GLindexBuffer("count", "type"), "indices")]),

    # GL_EXT_fog_coord
    GlFunction(Void, "glFogCoordfEXT", [(GLfloat, "coord")]),
    GlFunction(Void, "glFogCoordfvEXT", [(Pointer(Const(GLfloat)), "coord")]),
    GlFunction(Void, "glFogCoorddEXT", [(GLdouble, "coord")]),
    GlFunction(Void, "glFogCoorddvEXT", [(Pointer(Const(GLdouble)), "coord")]),
    GlFunction(Void, "glFogCoordPointerEXT", [(GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),

    # GL_EXT_framebuffer_blit
    GlFunction(Void, "glBlitFramebufferEXT", [(GLint, "srcX0"), (GLint, "srcY0"), (GLint, "srcX1"), (GLint, "srcY1"), (GLint, "dstX0"), (GLint, "dstY0"), (GLint, "dstX1"), (GLint, "dstY1"), (GLbitfield_attrib, "mask"), (GLenum, "filter")]),

    # GL_EXT_framebuffer_multisample
    GlFunction(Void, "glRenderbufferStorageMultisampleEXT", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),

    # GL_EXT_framebuffer_object
    GlFunction(GLboolean, "glIsRenderbufferEXT", [(GLrenderbuffer, "renderbuffer")], sideeffects=False),
    GlFunction(Void, "glBindRenderbufferEXT", [(GLenum, "target"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glDeleteRenderbuffersEXT", [(GLsizei, "n"), (Array(Const(GLrenderbuffer), "n"), "renderbuffers")]),
    GlFunction(Void, "glGenRenderbuffersEXT", [(GLsizei, "n"), Out(Array(GLrenderbuffer, "n"), "renderbuffers")]),
    GlFunction(Void, "glRenderbufferStorageEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glGetRenderbufferParameterivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLboolean, "glIsFramebufferEXT", [(GLframebuffer, "framebuffer")], sideeffects=False),
    GlFunction(Void, "glBindFramebufferEXT", [(GLenum, "target"), (GLframebuffer, "framebuffer")]),
    GlFunction(Void, "glDeleteFramebuffersEXT", [(GLsizei, "n"), (Array(Const(GLframebuffer), "n"), "framebuffers")]),
    GlFunction(Void, "glGenFramebuffersEXT", [(GLsizei, "n"), Out(Array(GLframebuffer, "n"), "framebuffers")]),
    GlFunction(GLenum, "glCheckFramebufferStatusEXT", [(GLenum, "target")]),
    GlFunction(Void, "glFramebufferTexture1DEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glFramebufferTexture2DEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glFramebufferTexture3DEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level"), (GLint, "zoffset")]),
    GlFunction(Void, "glFramebufferRenderbufferEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "renderbuffertarget"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glGetFramebufferAttachmentParameterivEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGenerateMipmapEXT", [(GLenum, "target")]),

    # GL_EXT_geometry_shader
    GlFunction(Void, "glFramebufferTextureEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level")]),

    # GL_EXT_geometry_shader4
    GlFunction(Void, "glProgramParameteriEXT", [(GLprogram, "program"), (GLenum, "pname"), (GLint, "value")]),

    # GL_EXT_gpu_program_parameters
    GlFunction(Void, "glProgramEnvParameters4fvEXT", [(GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "params")]),
    GlFunction(Void, "glProgramLocalParameters4fvEXT", [(GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "params")]),

    # GL_EXT_gpu_shader4
    GlFunction(Void, "glGetUniformuivEXT", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaqueArray(GLuint, "_glGetUniformuivEXT_size(program, location)"), "params")], sideeffects=False),
    GlFunction(GLint, "glGetFragDataLocationEXT", [(GLprogram, "program"), (GLstringConst, "name")], sideeffects=False),
    GlFunction(Void, "glUniform1uiEXT", [(GLlocation, "location"), (GLuint, "v0")]),
    GlFunction(Void, "glUniform2uiEXT", [(GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1")]),
    GlFunction(Void, "glUniform3uiEXT", [(GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1"), (GLuint, "v2")]),
    GlFunction(Void, "glUniform4uiEXT", [(GLlocation, "location"), (GLuint, "v0"), (GLuint, "v1"), (GLuint, "v2"), (GLuint, "v3")]),
    GlFunction(Void, "glUniform1uivEXT", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "value")]),
    GlFunction(Void, "glUniform2uivEXT", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*2"), "value")]),
    GlFunction(Void, "glUniform3uivEXT", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*3"), "value")]),
    GlFunction(Void, "glUniform4uivEXT", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint), "count*4"), "value")]),

    # GL_EXT_histogram
    GlFunction(Void, "glGetHistogramEXT", [(GLenum, "target"), (GLboolean, "reset"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetHistogramEXT_size(target, format, type)"), "values")]),
    GlFunction(Void, "glGetHistogramParameterfvEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetHistogramParameterivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetMinmaxEXT", [(GLenum, "target"), (GLboolean, "reset"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetMinmaxEXT_size(target, format, type)"), "values")]),
    GlFunction(Void, "glGetMinmaxParameterfvEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMinmaxParameterivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glHistogramEXT", [(GLenum, "target"), (GLsizei, "width"), (GLenum, "internalformat"), (GLboolean, "sink")]),
    GlFunction(Void, "glMinmaxEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLboolean, "sink")]),
    GlFunction(Void, "glResetHistogramEXT", [(GLenum, "target")]),
    GlFunction(Void, "glResetMinmaxEXT", [(GLenum, "target")]),

    # GL_EXT_index_func
    GlFunction(Void, "glIndexFuncEXT", [(GLenum, "func"), (GLclampf, "ref")]),

    # GL_EXT_index_material
    GlFunction(Void, "glIndexMaterialEXT", [(GLenum, "face"), (GLenum, "mode")]),

    # GL_EXT_instanced_arrays
    GlFunction(Void, "glVertexAttribDivisorEXT", [(GLuint, "index"), (GLuint, "divisor")]),

    # GL_EXT_light_texture
    GlFunction(Void, "glApplyTextureEXT", [(GLenum, "mode")]),
    GlFunction(Void, "glTextureLightEXT", [(GLenum, "pname")]),
    GlFunction(Void, "glTextureMaterialEXT", [(GLenum, "face"), (GLenum, "mode")]),

    # GL_EXT_map_buffer_range
    GlFunction(GLmap, "glMapBufferRangeEXT", [(GLenum, "target"), (GLintptr, "offset"), (GLsizeiptr, "length"), (GLbitfield_access, "access")]),
    GlFunction(Void, "glFlushMappedBufferRangeEXT", [(GLenum, "target"), (GLintptr, "offset"), (GLsizeiptr, "length")]),

    # GL_EXT_multi_draw_arrays
    GlFunction(Void, "glMultiDrawArraysEXT", [(GLenum_mode, "mode"), (Array(Const(GLint), "drawcount"), "first"), (Array(Const(GLsizei), "drawcount"), "count"), (GLsizei, "drawcount")]),
    GlFunction(Void, "glMultiDrawElementsEXT", [(GLenum_mode, "mode"), (Array(Const(GLsizei), "drawcount"), "count"), (GLenum, "type"), (Array(Const(GLindexBuffer("count[{i}]", "type")), "drawcount"), "indices"), (GLsizei, "drawcount")]),

    # GL_EXT_multi_draw_indirect
    GlFunction(Void, "glMultiDrawArraysIndirectEXT", [(GLenum_mode, "mode"), (GLpointerConst, "indirect"), (GLsizei, "drawcount"), (GLsizei, "stride")]),
    GlFunction(Void, "glMultiDrawElementsIndirectEXT", [(GLenum_mode, "mode"), (GLenum, "type"), (GLpointerConst, "indirect"), (GLsizei, "drawcount"), (GLsizei, "stride")]),

    # GL_EXT_multisample
    GlFunction(Void, "glSampleMaskEXT", [(GLclampf, "value"), (GLboolean, "invert")]),
    GlFunction(Void, "glSamplePatternEXT", [(GLenum, "pattern")]),

    # GL_EXT_multisampled_render_to_texture
    GlFunction(Void, "glFramebufferTexture2DMultisampleEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level"), (GLsizei, "samples")]),

    # GL_EXT_multiview_draw_buffers
    GlFunction(Void, "glReadBufferIndexedEXT", [(GLenum, "src"), (GLint, "index")]),
    GlFunction(Void, "glDrawBuffersIndexedEXT", [(GLint, "n"), (Array(Const(GLenum), "n"), "location"), (Array(Const(GLint), "n"), "indices")]),
    GlFunction(Void, "glGetIntegeri_vEXT", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLint, "_gl_param_size(target)"), "data")], sideeffects=False),

    # GL_EXT_occlusion_query_boolean

    # GL_EXT_paletted_texture
    GlFunction(Void, "glColorTableEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glColorTable_size(format, type, width)"), "table")]),
    GlFunction(Void, "glGetColorTableEXT", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetColorTableEXT_size(target, format, type)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetColorTableParameterivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetColorTableParameterfvEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_EXT_pixel_transform
    GlFunction(Void, "glPixelTransformParameteriEXT", [(GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glPixelTransformParameterfEXT", [(GLenum, "target"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glPixelTransformParameterivEXT", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glPixelTransformParameterfvEXT", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetPixelTransformParameterivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetPixelTransformParameterfvEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_EXT_point_parameters
    GlFunction(Void, "glPointParameterfEXT", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glPointParameterfvEXT", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),

    # GL_EXT_polygon_offset
    GlFunction(Void, "glPolygonOffsetEXT", [(GLfloat, "factor"), (GLfloat, "bias")]),

    # GL_EXT_polygon_offset_clamp
    GlFunction(Void, "glPolygonOffsetClampEXT", [(GLfloat, "factor"), (GLfloat, "units"), (GLfloat, "clamp")]),

    # GL_EXT_primitive_bounding_box
    GlFunction(Void, "glPrimitiveBoundingBoxEXT", [(GLfloat, "minX"), (GLfloat, "minY"), (GLfloat, "minZ"), (GLfloat, "minW"), (GLfloat, "maxX"), (GLfloat, "maxY"), (GLfloat, "maxZ"), (GLfloat, "maxW")]),

    # GL_EXT_provoking_vertex
    GlFunction(Void, "glProvokingVertexEXT", [(GLenum, "mode")]),

    # GL_EXT_raster_multisample
    GlFunction(Void, "glRasterSamplesEXT", [(GLuint, "samples"), (GLboolean, "fixedsamplelocations")]),

    # GL_EXT_robustness
    GlFunction(GLenum, "glGetGraphicsResetStatusEXT", [], sideeffects=False),
    GlFunction(Void, "glReadnPixelsEXT", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "data")]),
    GlFunction(Void, "glGetnUniformfvEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLfloat, "bufSize"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformivEXT", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLint, "bufSize"), "params")], sideeffects=False),

    # GL_EXT_secondary_color
    GlFunction(Void, "glSecondaryColor3bEXT", [(GLbyte, "red"), (GLbyte, "green"), (GLbyte, "blue")]),
    GlFunction(Void, "glSecondaryColor3bvEXT", [(Array(Const(GLbyte), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3dEXT", [(GLdouble, "red"), (GLdouble, "green"), (GLdouble, "blue")]),
    GlFunction(Void, "glSecondaryColor3dvEXT", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3fEXT", [(GLfloat, "red"), (GLfloat, "green"), (GLfloat, "blue")]),
    GlFunction(Void, "glSecondaryColor3fvEXT", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3iEXT", [(GLint, "red"), (GLint, "green"), (GLint, "blue")]),
    GlFunction(Void, "glSecondaryColor3ivEXT", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3sEXT", [(GLshort, "red"), (GLshort, "green"), (GLshort, "blue")]),
    GlFunction(Void, "glSecondaryColor3svEXT", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3ubEXT", [(GLubyte, "red"), (GLubyte, "green"), (GLubyte, "blue")]),
    GlFunction(Void, "glSecondaryColor3ubvEXT", [(Array(Const(GLubyte), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3uiEXT", [(GLuint, "red"), (GLuint, "green"), (GLuint, "blue")]),
    GlFunction(Void, "glSecondaryColor3uivEXT", [(Array(Const(GLuint), 3), "v")]),
    GlFunction(Void, "glSecondaryColor3usEXT", [(GLushort, "red"), (GLushort, "green"), (GLushort, "blue")]),
    GlFunction(Void, "glSecondaryColor3usvEXT", [(Array(Const(GLushort), 3), "v")]),
    GlFunction(Void, "glSecondaryColorPointerEXT", [(size_bgra, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),

    # GL_EXT_separate_shader_objects
    GlFunction(Void, "glUseShaderProgramEXT", [(GLenum, "type"), (GLprogram, "program")]),
    GlFunction(Void, "glActiveProgramEXT", [(GLprogram, "program")]),
    GlFunction(GLprogram, "glCreateShaderProgramEXT", [(GLenum, "type"), (GLstringConst, "string")]),
    GlFunction(Void, "glActiveShaderProgramEXT", [(GLpipeline, "pipeline"), (GLprogram, "program")]),
    GlFunction(Void, "glBindProgramPipelineEXT", [(GLpipeline, "pipeline")]),
    GlFunction(GLprogram, "glCreateShaderProgramvEXT", [(GLenum, "type"), (GLsizei, "count"), (Const(Array(GLstringConst, "count")), "strings")]),
    GlFunction(Void, "glDeleteProgramPipelinesEXT", [(GLsizei, "n"), (Array(Const(GLuint), "n"), "pipelines")]),
    GlFunction(Void, "glGenProgramPipelinesEXT", [(GLsizei, "n"), Out(Array(GLpipeline, "n"), "pipelines")]),
    GlFunction(Void, "glGetProgramPipelineInfoLogEXT", [(GLpipeline, "pipeline"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(GLstring, "infoLog")], sideeffects=False),
    GlFunction(Void, "glGetProgramPipelineivEXT", [(GLpipeline, "pipeline"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLboolean, "glIsProgramPipelineEXT", [(GLpipeline, "pipeline")], sideeffects=False),
    GlFunction(Void, "glUseProgramStagesEXT", [(GLpipeline, "pipeline"), (GLbitfield_shader, "stages"), (GLprogram, "program")]),
    GlFunction(Void, "glValidateProgramPipelineEXT", [(GLpipeline, "pipeline")]),

    # GL_EXT_shader_image_load_store
    GlFunction(Void, "glBindImageTextureEXT", [(GLuint, "index"), (GLtexture, "texture"), (GLint, "level"), (GLboolean, "layered"), (GLint, "layer"), (GLenum, "access"), (GLint, "format")]),
    GlFunction(Void, "glMemoryBarrierEXT", [(GLbitfield_barrier, "barriers")]),

    # GL_EXT_shader_pixel_local_storage2
    GlFunction(Void, "glFramebufferPixelLocalStorageSizeEXT", [(GLframebuffer, "target"), (GLsizei, "size")]),
    GlFunction(GLsizei, "glGetFramebufferPixelLocalStorageSizeEXT", [(GLframebuffer, "target")], sideeffects=False),
    GlFunction(Void, "glClearPixelLocalStorageuiEXT", [(GLsizei, "offset"), (GLsizei, "n"), (Array(Const(GLuint), "n"), "values")]),

    # GL_EXT_sparse_texture
    GlFunction(Void, "glTexPageCommitmentEXT", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "commit")]),

    # GL_EXT_stencil_clear_tag
    GlFunction(Void, "glStencilClearTagEXT", [(GLsizei, "stencilTagBits"), (GLuint, "stencilClearTag")]),

    # GL_EXT_stencil_two_side
    GlFunction(Void, "glActiveStencilFaceEXT", [(GLenum, "face")]),

    # GL_EXT_subtexture
    GlFunction(Void, "glTexSubImage1DEXT", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage1D_size(format, type, width)"), "pixels")]),
    GlFunction(Void, "glTexSubImage2DEXT", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage2D_size(format, type, width, height)"), "pixels")]),

    # GL_EXT_tessellation_shader
    GlFunction(Void, "glPatchParameteriEXT", [(GLenum, "pname"), (GLint, "value")]),

    # GL_EXT_texture3D
    GlFunction(Void, "glTexImage3DEXT", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glTexSubImage3DEXT", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),

    # GL_EXT_texture_array
    GlFunction(Void, "glFramebufferTextureLayerEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLint, "layer")]),

    # GL_EXT_texture_border_clamp
    GlFunction(Void, "glTexParameterIivEXT", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexParameterIuivEXT", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLuint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetTexParameterIivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexParameterIuivEXT", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glSamplerParameterIivEXT", [(GLuint, "sampler"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "param")]),
    GlFunction(Void, "glSamplerParameterIuivEXT", [(GLuint, "sampler"), (GLenum, "pname"), (Array(Const(GLuint), "_gl_param_size(pname)"), "param")]),
    GlFunction(Void, "glGetSamplerParameterIivEXT", [(GLuint, "sampler"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetSamplerParameterIuivEXT", [(GLuint, "sampler"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_EXT_texture_buffer
    GlFunction(Void, "glTexBufferEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glTexBufferRangeEXT", [(GLenum, "target"), (GLenum, "internalformat"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size")]),

    # GL_EXT_texture_buffer_object

    # GL_EXT_texture_filter_minmax

    # GL_EXT_texture_integer
    GlFunction(Void, "glClearColorIiEXT", [(GLint, "red"), (GLint, "green"), (GLint, "blue"), (GLint, "alpha")]),
    GlFunction(Void, "glClearColorIuiEXT", [(GLuint, "red"), (GLuint, "green"), (GLuint, "blue"), (GLuint, "alpha")]),

    # GL_EXT_texture_object
    GlFunction(GLboolean, "glAreTexturesResidentEXT", [(GLsizei, "n"), (Array(Const(GLtexture), "n"), "textures"), Out(Array(GLboolean, "n"), "residences")], sideeffects=False),
    GlFunction(Void, "glBindTextureEXT", [(GLenum, "target"), (GLtexture, "texture")]),
    GlFunction(Void, "glDeleteTexturesEXT", [(GLsizei, "n"), (Array(Const(GLtexture), "n"), "textures")]),
    GlFunction(Void, "glGenTexturesEXT", [(GLsizei, "n"), Out(Array(GLtexture, "n"), "textures")]),
    GlFunction(GLboolean, "glIsTextureEXT", [(GLtexture, "texture")], sideeffects=False),
    GlFunction(Void, "glPrioritizeTexturesEXT", [(GLsizei, "n"), (Array(Const(GLtexture), "n"), "textures"), (Array(Const(GLclampf), "n"), "priorities")]),

    # GL_EXT_texture_perturb_normal
    GlFunction(Void, "glTextureNormalEXT", [(GLenum, "mode")]),

    # GL_EXT_texture_storage
    GlFunction(Void, "glTexStorage1DEXT", [(GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width")]),
    GlFunction(Void, "glTexStorage2DEXT", [(GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glTexStorage3DEXT", [(GLenum, "target"), (GLsizei, "levels"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth")]),

    # GL_EXT_texture_view
    GlFunction(Void, "glTextureViewEXT", [(GLtexture, "texture"), (GLenum, "target"), (GLtexture, "origtexture"), (GLenum, "internalformat"), (GLuint, "minlevel"), (GLuint, "numlevels"), (GLuint, "minlayer"), (GLuint, "numlayers")]),

    # GL_EXT_timer_query

    # GL_EXT_transform_feedback
    GlFunction(Void, "glBeginTransformFeedbackEXT", [(GLenum_mode, "primitiveMode")]),
    GlFunction(Void, "glEndTransformFeedbackEXT", []),
    GlFunction(Void, "glBindBufferRangeEXT", [(GLenum, "target"), (GLuint, "index"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size")]),
    GlFunction(Void, "glBindBufferOffsetEXT", [(GLenum, "target"), (GLuint, "index"), (GLbuffer, "buffer"), (GLintptr, "offset")]),
    GlFunction(Void, "glBindBufferBaseEXT", [(GLenum, "target"), (GLuint, "index"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glTransformFeedbackVaryingsEXT", [(GLprogram, "program"), (GLsizei, "count"), (Array(Const(GLstringConst), "count"), "varyings"), (GLenum, "bufferMode")]),
    GlFunction(Void, "glGetTransformFeedbackVaryingEXT", [(GLprogram, "program"), (GLuint, "index"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLsizei), "size"), Out(Pointer(GLenum), "type"), OutGlString(GLchar, "length", "name")], sideeffects=False),

    # GL_EXT_vertex_array
    GlFunction(Void, "glArrayElementEXT", [(GLint, "i")]),
    GlFunction(Void, "glColorPointerEXT", [(size_bgra, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLsizei, "count"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glDrawArraysEXT", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count")]),
    GlFunction(Void, "glEdgeFlagPointerEXT", [(GLsizei, "stride"), (GLsizei, "count"), (OpaquePointer(Const(GLboolean)), "pointer")]),
    GlFunction(Void, "glGetPointervEXT", [(GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),
    GlFunction(Void, "glIndexPointerEXT", [(GLenum, "type"), (GLsizei, "stride"), (GLsizei, "count"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glNormalPointerEXT", [(GLenum, "type"), (GLsizei, "stride"), (GLsizei, "count"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glTexCoordPointerEXT", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLsizei, "count"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glVertexPointerEXT", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLsizei, "count"), (GLpointerConst, "pointer")]),

    # GL_EXT_vertex_attrib_64bit
    GlFunction(Void, "glVertexAttribL1dEXT", [(GLuint, "index"), (GLdouble, "x")]),
    GlFunction(Void, "glVertexAttribL2dEXT", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glVertexAttribL3dEXT", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glVertexAttribL4dEXT", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glVertexAttribL1dvEXT", [(GLuint, "index"), (Pointer(Const(GLdouble)), "v")]),
    GlFunction(Void, "glVertexAttribL2dvEXT", [(GLuint, "index"), (Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glVertexAttribL3dvEXT", [(GLuint, "index"), (Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glVertexAttribL4dvEXT", [(GLuint, "index"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glVertexAttribLPointerEXT", [(GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (Blob(Const(GLvoid), "size"), "pointer")]),
    GlFunction(Void, "glGetVertexAttribLdvEXT", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_EXT_vertex_shader
    GlFunction(Void, "glBeginVertexShaderEXT", []),
    GlFunction(Void, "glEndVertexShaderEXT", []),
    GlFunction(Void, "glBindVertexShaderEXT", [(GLuint, "id")]),
    GlFunction(GLuint, "glGenVertexShadersEXT", [(GLuint, "range")]),
    GlFunction(Void, "glDeleteVertexShaderEXT", [(GLuint, "id")]),
    GlFunction(Void, "glShaderOp1EXT", [(GLenum, "op"), (GLuint, "res"), (GLuint, "arg1")]),
    GlFunction(Void, "glShaderOp2EXT", [(GLenum, "op"), (GLuint, "res"), (GLuint, "arg1"), (GLuint, "arg2")]),
    GlFunction(Void, "glShaderOp3EXT", [(GLenum, "op"), (GLuint, "res"), (GLuint, "arg1"), (GLuint, "arg2"), (GLuint, "arg3")]),
    GlFunction(Void, "glSwizzleEXT", [(GLuint, "res"), (GLuint, "in"), (GLenum, "outX"), (GLenum, "outY"), (GLenum, "outZ"), (GLenum, "outW")]),
    GlFunction(Void, "glWriteMaskEXT", [(GLuint, "res"), (GLuint, "in"), (GLenum, "outX"), (GLenum, "outY"), (GLenum, "outZ"), (GLenum, "outW")]),
    GlFunction(Void, "glInsertComponentEXT", [(GLuint, "res"), (GLuint, "src"), (GLuint, "num")]),
    GlFunction(Void, "glExtractComponentEXT", [(GLuint, "res"), (GLuint, "src"), (GLuint, "num")]),
    GlFunction(GLuint, "glGenSymbolsEXT", [(GLenum, "datatype"), (GLenum, "storagetype"), (GLenum, "range"), (GLuint, "components")]),
    GlFunction(Void, "glSetInvariantEXT", [(GLuint, "id"), (GLenum, "type"), (OpaqueBlob(Const(GLvoid), "_glSetInvariantEXT_size(id, type)"), "addr")]),
    GlFunction(Void, "glSetLocalConstantEXT", [(GLuint, "id"), (GLenum, "type"), (OpaqueBlob(Const(GLvoid), "_glSetLocalConstantEXT_size(id, type)"), "addr")]),
    GlFunction(Void, "glVariantbvEXT", [(GLuint, "id"), (OpaqueArray(Const(GLbyte), "_glVariantbvEXT_size(id)"), "addr")]),
    GlFunction(Void, "glVariantsvEXT", [(GLuint, "id"), (OpaqueArray(Const(GLshort), "_glVariantsvEXT_size(id)"), "addr")]),
    GlFunction(Void, "glVariantivEXT", [(GLuint, "id"), (OpaqueArray(Const(GLint), "_glVariantivEXT_size(id)"), "addr")]),
    GlFunction(Void, "glVariantfvEXT", [(GLuint, "id"), (OpaqueArray(Const(GLfloat), "_glVariantfvEXT_size(id)"), "addr")]),
    GlFunction(Void, "glVariantdvEXT", [(GLuint, "id"), (OpaqueArray(Const(GLdouble), "_glVariantdvEXT_size(id)"), "addr")]),
    GlFunction(Void, "glVariantubvEXT", [(GLuint, "id"), (OpaqueArray(Const(GLubyte), "_glVariantubvEXT_size(id)"), "addr")]),
    GlFunction(Void, "glVariantusvEXT", [(GLuint, "id"), (OpaqueArray(Const(GLushort), "_glVariantusvEXT_size(id)"), "addr")]),
    GlFunction(Void, "glVariantuivEXT", [(GLuint, "id"), (OpaqueArray(Const(GLuint), "_glVariantuivEXT_size(id)"), "addr")]),
    GlFunction(Void, "glVariantPointerEXT", [(GLuint, "id"), (GLenum, "type"), (GLuint, "stride"), (OpaqueBlob(Const(GLvoid), "_glVariantPointerEXT_size(id, type, stride)"), "addr")]),
    GlFunction(Void, "glEnableVariantClientStateEXT", [(GLuint, "id")]),
    GlFunction(Void, "glDisableVariantClientStateEXT", [(GLuint, "id")]),
    GlFunction(GLuint, "glBindLightParameterEXT", [(GLenum, "light"), (GLenum, "value")]),
    GlFunction(GLuint, "glBindMaterialParameterEXT", [(GLenum, "face"), (GLenum, "value")]),
    GlFunction(GLuint, "glBindTexGenParameterEXT", [(GLenum, "unit"), (GLenum, "coord"), (GLenum, "value")]),
    GlFunction(GLuint, "glBindTextureUnitParameterEXT", [(GLenum, "unit"), (GLenum, "value")]),
    GlFunction(GLuint, "glBindParameterEXT", [(GLenum, "value")]),
    GlFunction(GLboolean, "glIsVariantEnabledEXT", [(GLuint, "id"), (GLenum, "cap")], sideeffects=False),
    GlFunction(Void, "glGetVariantBooleanvEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLboolean, "_glGetVariantBooleanvEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetVariantIntegervEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLint, "_glGetVariantIntegervEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetVariantFloatvEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLfloat, "_glGetVariantFloatvEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetVariantPointervEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLpointer, "_glGetVariantPointervEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetInvariantBooleanvEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLboolean, "_glGetInvariantBooleanvEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetInvariantIntegervEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLint, "_glGetInvariantIntegervEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetInvariantFloatvEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLfloat, "_glGetInvariantFloatvEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetLocalConstantBooleanvEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLboolean, "_glGetLocalConstantBooleanvEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetLocalConstantIntegervEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLint, "_glGetLocalConstantIntegervEXT_size(id)"), "data")], sideeffects=False),
    GlFunction(Void, "glGetLocalConstantFloatvEXT", [(GLuint, "id"), (GLenum, "value"), Out(OpaqueArray(GLfloat, "_glGetLocalConstantFloatvEXT_size(id)"), "data")], sideeffects=False),

    # GL_EXT_vertex_weighting
    GlFunction(Void, "glVertexWeightfEXT", [(GLfloat, "weight")]),
    GlFunction(Void, "glVertexWeightfvEXT", [(Pointer(Const(GLfloat)), "weight")]),
    GlFunction(Void, "glVertexWeightPointerEXT", [(GLsizei, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),

    # GL_EXT_x11_sync_object
    GlFunction(GLsync, "glImportSyncEXT", [(GLenum, "external_sync_type"), (GLintptr, "external_sync"), (GLbitfield, "flags")]),

    # GL_GREMEDY_frame_terminator
    GlFunction(Void, "glFrameTerminatorGREMEDY", []),

    # GL_GREMEDY_string_marker
    GlFunction(Void, "glStringMarkerGREMEDY", [(GLsizei, "len"), (String(Const(GLvoid), "len > 0 ? len : strlen((const char *)string)"), "string")], sideeffects=True),

    # GL_HP_image_transform
    GlFunction(Void, "glImageTransformParameteriHP", [(GLenum, "target"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glImageTransformParameterfHP", [(GLenum, "target"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glImageTransformParameterivHP", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glImageTransformParameterfvHP", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetImageTransformParameterivHP", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetImageTransformParameterfvHP", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_IBM_multimode_draw_arrays
    GlFunction(Void, "glMultiModeDrawArraysIBM", [(Array(Const(GLenum_mode), "drawcount"), "mode"), (Array(Const(GLint), "drawcount"), "first"), (Array(Const(GLsizei), "drawcount"), "count"), (GLsizei, "drawcount"), (GLint, "modestride")]),
    GlFunction(Void, "glMultiModeDrawElementsIBM", [(Array(Const(GLenum_mode), "drawcount"), "mode"), (Array(Const(GLsizei), "drawcount"), "count"), (GLenum, "type"), (Array(Const(GLindexBuffer("count[{i}]", "type")), "drawcount"), "indices"), (GLsizei, "drawcount"), (GLint, "modestride")]),

    # GL_IBM_vertex_array_lists
    GlFunction(Void, "glColorPointerListIBM", [(size_bgra, "size"), (GLenum, "type"), (GLint, "stride"), (OpaquePointer(GLpointerConst), "pointer"), (GLint, "ptrstride")]),
    GlFunction(Void, "glSecondaryColorPointerListIBM", [(size_bgra, "size"), (GLenum, "type"), (GLint, "stride"), (OpaquePointer(GLpointerConst), "pointer"), (GLint, "ptrstride")]),
    GlFunction(Void, "glEdgeFlagPointerListIBM", [(GLint, "stride"), (OpaquePointer(Opaque("const GLboolean *")), "pointer"), (GLint, "ptrstride")]),
    GlFunction(Void, "glFogCoordPointerListIBM", [(GLenum, "type"), (GLint, "stride"), (OpaquePointer(GLpointerConst), "pointer"), (GLint, "ptrstride")]),
    GlFunction(Void, "glIndexPointerListIBM", [(GLenum, "type"), (GLint, "stride"), (OpaquePointer(GLpointerConst), "pointer"), (GLint, "ptrstride")]),
    GlFunction(Void, "glNormalPointerListIBM", [(GLenum, "type"), (GLint, "stride"), (OpaquePointer(GLpointerConst), "pointer"), (GLint, "ptrstride")]),
    GlFunction(Void, "glTexCoordPointerListIBM", [(GLint, "size"), (GLenum, "type"), (GLint, "stride"), (OpaquePointer(GLpointerConst), "pointer"), (GLint, "ptrstride")]),
    GlFunction(Void, "glVertexPointerListIBM", [(GLint, "size"), (GLenum, "type"), (GLint, "stride"), (OpaquePointer(GLpointerConst), "pointer"), (GLint, "ptrstride")]),

    # GL_IMG_multisampled_render_to_texture
    GlFunction(Void, "glRenderbufferStorageMultisampleIMG", [(GLenum, "target"), (GLsizei, "samples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glFramebufferTexture2DMultisampleIMG", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level"), (GLsizei, "samples")]),

    # GL_INGR_blend_func_separate
    GlFunction(Void, "glBlendFuncSeparateINGR", [(GLenum, "sfactorRGB"), (GLenum, "dfactorRGB"), (GLenum, "sfactorAlpha"), (GLenum, "dfactorAlpha")]),

    # GL_INTEL_map_texture
    GlFunction(Void, "glSyncTextureINTEL", [(GLtexture, "texture")]),
    GlFunction(Void, "glUnmapTexture2DINTEL", [(GLtexture, "texture"), (GLint, "level")]),
    GlFunction(OpaquePointer(GLvoid), "glMapTexture2DINTEL", [(GLtexture, "texture"), (GLint, "level"), (GLbitfield_access, "access"), Out(Pointer(GLint), "stride"), Out(Pointer(GLenum), "layout")]),

    # GL_INTEL_parallel_arrays
    GlFunction(Void, "glVertexPointervINTEL", [(GLint, "size"), (GLenum, "type"), (OpaqueArray(GLpointerConst, "size"), "pointer")]),
    GlFunction(Void, "glNormalPointervINTEL", [(GLenum, "type"), (OpaqueArray(GLpointerConst, "size"), "pointer")]),
    GlFunction(Void, "glColorPointervINTEL", [(size_bgra, "size"), (GLenum, "type"), (OpaqueArray(GLpointerConst, "size"), "pointer")]),
    GlFunction(Void, "glTexCoordPointervINTEL", [(GLint, "size"), (GLenum, "type"), (OpaqueArray(GLpointerConst, "size"), "pointer")]),

    # GL_INTEL_performance_query
    GlFunction(Void, "glBeginPerfQueryINTEL", [(GLuint, "queryHandle")], sideeffects=False),
    GlFunction(Void, "glCreatePerfQueryINTEL", [(GLuint, "queryId"), Out(Pointer(GLuint), "queryHandle")], sideeffects=False),
    GlFunction(Void, "glDeletePerfQueryINTEL", [(GLuint, "queryHandle")], sideeffects=False),
    GlFunction(Void, "glEndPerfQueryINTEL", [(GLuint, "queryHandle")], sideeffects=False),
    GlFunction(Void, "glGetFirstPerfQueryIdINTEL", [Out(Pointer(GLuint), "queryId")], sideeffects=False),
    GlFunction(Void, "glGetNextPerfQueryIdINTEL", [(GLuint, "queryId"), Out(Pointer(GLuint), "nextQueryId")], sideeffects=False),
    GlFunction(Void, "glGetPerfCounterInfoINTEL", [(GLuint, "queryId"), (GLuint, "counterId"), (GLuint, "counterNameLength"), Out(GLstring, "counterName"), (GLuint, "counterDescLength"), Out(GLstring, "counterDesc"), Out(Pointer(GLuint), "counterOffset"), Out(Pointer(GLuint), "counterDataSize"), Out(Pointer(GLuint), "counterTypeEnum"), Out(Pointer(GLuint), "counterDataTypeEnum"), Out(Pointer(GLuint64), "rawCounterMaxValue")], sideeffects=False),
    GlFunction(Void, "glGetPerfQueryDataINTEL", [(GLuint, "queryHandle"), (GLuint, "flags"), (GLsizei, "dataSize"), Out(OpaqueBlob(GLvoid, "datasize"), "data"), Out(Pointer(GLuint), "bytesWritten")], sideeffects=False),
    GlFunction(Void, "glGetPerfQueryIdByNameINTEL", [(GLstring, "queryName"), Out(Pointer(GLuint), "queryId")], sideeffects=False),
    GlFunction(Void, "glGetPerfQueryInfoINTEL", [(GLuint, "queryId"), (GLuint, "queryNameLength"), Out(GLstring, "queryName"), Out(Pointer(GLuint), "dataSize"), Out(Pointer(GLuint), "noCounters"), Out(Pointer(GLuint), "noInstances"), Out(Pointer(GLuint), "capsMask")], sideeffects=False),

    # GL_KHR_blend_equation_advanced
    GlFunction(Void, "glBlendBarrierKHR", []),

    # GL_KHR_debug
    GlFunction(Void, "glDebugMessageControl", [(GLenum, "source"), (GLenum, "type"), (GLenum, "severity"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "ids"), (GLboolean, "enabled")], sideeffects=True),
    GlFunction(Void, "glDebugMessageInsert", [(GLenum, "source"), (GLenum, "type"), (GLuint, "id"), (GLenum, "severity"), (GLsizei, "length"), InGlString(GLchar, "length", "buf")], sideeffects=True),
    GlFunction(Void, "glDebugMessageCallback", [(GLDEBUGPROC, "callback"), (OpaquePointer(Const(Void)), "userParam")], sideeffects=False),
    GlFunction(GLuint, "glGetDebugMessageLog", [(GLuint, "count"), (GLsizei, "bufsize"), Out(Array(GLenum, "count"), "sources"), Out(Array(GLenum, "count"), "types"), Out(Array(GLuint, "count"), "ids"), Out(Array(GLenum, "count"), "severities"), Out(Array(GLsizei, "count"), "lengths"), Out(String(GLchar, "_glGetDebugMessageLog_length(messageLog, lengths, _result)"), "messageLog")], sideeffects=False, fail=0),
    GlFunction(Void, "glPushDebugGroup", [(GLenum, "source"), (GLuint, "id"), (GLsizei, "length"), InGlString(GLchar, "length", "message")], sideeffects=True),
    GlFunction(Void, "glPopDebugGroup", [], sideeffects=True),
    GlFunction(Void, "glObjectLabel", [(GLenum, "identifier"), (GLuint, "name"), (GLsizei, "length"), InGlString(GLchar, "length", "label")], sideeffects=True),
    GlFunction(Void, "glGetObjectLabel", [(GLenum, "identifier"), (GLuint, "name"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "label")], sideeffects=False),
    GlFunction(Void, "glObjectPtrLabel", [(OpaquePointer(Const(Void)), "ptr"), (GLsizei, "length"), InGlString(GLchar, "length", "label")], sideeffects=True),
    GlFunction(Void, "glGetObjectPtrLabel", [(OpaquePointer(Const(Void)), "ptr"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "label")], sideeffects=False),
    GlFunction(Void, "glDebugMessageControlKHR", [(GLenum, "source"), (GLenum, "type"), (GLenum, "severity"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "ids"), (GLboolean, "enabled")], sideeffects=True),
    GlFunction(Void, "glDebugMessageInsertKHR", [(GLenum, "source"), (GLenum, "type"), (GLuint, "id"), (GLenum, "severity"), (GLsizei, "length"), InGlString(GLchar, "length", "buf")], sideeffects=True),
    GlFunction(Void, "glDebugMessageCallbackKHR", [(GLDEBUGPROCKHR, "callback"), (OpaquePointer(Const(Void)), "userParam")], sideeffects=False),
    GlFunction(GLuint, "glGetDebugMessageLogKHR", [(GLuint, "count"), (GLsizei, "bufsize"), Out(Array(GLenum, "count"), "sources"), Out(Array(GLenum, "count"), "types"), Out(Array(GLuint, "count"), "ids"), Out(Array(GLenum, "count"), "severities"), Out(Array(GLsizei, "count"), "lengths"), Out(String(GLchar, "_glGetDebugMessageLog_length(messageLog, lengths, _result)"), "messageLog")], sideeffects=False, fail=0),
    GlFunction(Void, "glPushDebugGroupKHR", [(GLenum, "source"), (GLuint, "id"), (GLsizei, "length"), InGlString(GLchar, "length", "message")], sideeffects=True),
    GlFunction(Void, "glPopDebugGroupKHR", [], sideeffects=True),
    GlFunction(Void, "glObjectLabelKHR", [(GLenum, "identifier"), (GLuint, "name"), (GLsizei, "length"), InGlString(GLchar, "length", "label")], sideeffects=True),
    GlFunction(Void, "glGetObjectLabelKHR", [(GLenum, "identifier"), (GLuint, "name"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "label")], sideeffects=False),
    GlFunction(Void, "glObjectPtrLabelKHR", [(OpaquePointer(Const(Void)), "ptr"), (GLsizei, "length"), InGlString(GLchar, "length", "label")], sideeffects=True),
    GlFunction(Void, "glGetObjectPtrLabelKHR", [(OpaquePointer(Const(Void)), "ptr"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), OutGlString(GLchar, "length", "label")], sideeffects=False),
    GlFunction(Void, "glGetPointervKHR", [(GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),

    # GL_KHR_robustness
    GlFunction(GLenum, "glGetGraphicsResetStatus", [], sideeffects=False),
    GlFunction(Void, "glReadnPixels", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "data")]),
    GlFunction(Void, "glGetnUniformfv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLfloat, "bufSize/sizeof(GLfloat)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformiv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLint, "bufSize/sizeof(GLint)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformuiv", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLuint, "bufSize/sizeof(GLuint)"), "params")], sideeffects=False),
    GlFunction(GLenum, "glGetGraphicsResetStatusKHR", [], sideeffects=False),
    GlFunction(Void, "glReadnPixelsKHR", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLenum, "format"), (GLenum, "type"), (GLsizei, "bufSize"), Out(OpaqueBlob(GLvoid, "bufSize"), "data")]),
    GlFunction(Void, "glGetnUniformfvKHR", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLfloat, "bufSize/sizeof(GLfloat)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformivKHR", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLint, "bufSize/sizeof(GLint)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetnUniformuivKHR", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "bufSize"), Out(Array(GLuint, "bufSize/sizeof(GLuint)"), "params")], sideeffects=False),

    # GL_KTX_buffer_region
    # XXX: http://www.west.net/~brittain/3dsmax2.htm does not mention EXT suffix
    GlFunction(GLregion, "glNewBufferRegion", [(GLenum_region, "type")]),
    GlFunction(Void, "glDeleteBufferRegion", [(GLregion, "region")]),
    GlFunction(Void, "glReadBufferRegion", [(GLregion, "region"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glDrawBufferRegion", [(GLregion, "region"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height"), (GLint, "xDest"), (GLint, "yDest")]),
    GlFunction(GLuint, "glBufferRegionEnabled", [], sideeffects=False),

    # GL_MESA_resize_buffers
    GlFunction(Void, "glResizeBuffersMESA", []),

    # GL_MESA_window_pos
    GlFunction(Void, "glWindowPos2dMESA", [(GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glWindowPos2dvMESA", [(Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glWindowPos2fMESA", [(GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glWindowPos2fvMESA", [(Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glWindowPos2iMESA", [(GLint, "x"), (GLint, "y")]),
    GlFunction(Void, "glWindowPos2ivMESA", [(Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glWindowPos2sMESA", [(GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glWindowPos2svMESA", [(Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glWindowPos3dMESA", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glWindowPos3dvMESA", [(Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glWindowPos3fMESA", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glWindowPos3fvMESA", [(Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glWindowPos3iMESA", [(GLint, "x"), (GLint, "y"), (GLint, "z")]),
    GlFunction(Void, "glWindowPos3ivMESA", [(Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glWindowPos3sMESA", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glWindowPos3svMESA", [(Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glWindowPos4dMESA", [(GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glWindowPos4dvMESA", [(Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glWindowPos4fMESA", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glWindowPos4fvMESA", [(Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glWindowPos4iMESA", [(GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glWindowPos4ivMESA", [(Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glWindowPos4sMESA", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z"), (GLshort, "w")]),
    GlFunction(Void, "glWindowPos4svMESA", [(Array(Const(GLshort), 4), "v")]),

    # GL_NVX_conditional_render
    GlFunction(Void, "glBeginConditionalRenderNVX", [(GLquery, "id")]),
    GlFunction(Void, "glEndConditionalRenderNVX", []),

    # GL_NV_bindless_multi_draw_indirect
    GlFunction(Void, "glMultiDrawArraysIndirectBindlessNV", [(GLenum_mode, "mode"), (GLpointerConst, "indirect"), (GLsizei, "drawCount"), (GLsizei, "stride"), (GLint, "vertexBufferCount")]),
    GlFunction(Void, "glMultiDrawElementsIndirectBindlessNV", [(GLenum_mode, "mode"), (GLenum, "type"), (GLpointerConst, "indirect"), (GLsizei, "drawCount"), (GLsizei, "stride"), (GLint, "vertexBufferCount")]),

    # GL_NV_bindless_texture
    GlFunction(GLtextureHandle, "glGetTextureHandleNV", [(GLtexture, "texture")]),
    GlFunction(GLtextureHandle, "glGetTextureSamplerHandleNV", [(GLtexture, "texture"), (GLsampler, "sampler")]),
    GlFunction(Void, "glMakeTextureHandleResidentNV", [(GLtextureHandle, "handle")]),
    GlFunction(Void, "glMakeTextureHandleNonResidentNV", [(GLtextureHandle, "handle")]),
    GlFunction(GLimageHandle, "glGetImageHandleNV", [(GLtexture, "texture"), (GLint, "level"), (GLboolean, "layered"), (GLint, "layer"), (GLenum, "format")]),
    GlFunction(Void, "glMakeImageHandleResidentNV", [(GLimageHandle, "handle"), (GLenum, "access")]),
    GlFunction(Void, "glMakeImageHandleNonResidentNV", [(GLimageHandle, "handle")]),
    GlFunction(Void, "glUniformHandleui64NV", [(GLlocation, "location"), (GLuint64, "value")]),
    GlFunction(Void, "glUniformHandleui64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count"), "value")]),
    GlFunction(Void, "glProgramUniformHandleui64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64, "value")]),
    GlFunction(Void, "glProgramUniformHandleui64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64), "count"), "values")]),
    GlFunction(GLboolean, "glIsTextureHandleResidentNV", [(GLtextureHandle, "handle")], sideeffects=False),
    GlFunction(GLboolean, "glIsImageHandleResidentNV", [(GLimageHandle, "handle")], sideeffects=False),

    # GL_NV_blend_equation_advanced
    GlFunction(Void, "glBlendParameteriNV", [(GLenum, "pname"), (GLint, "value")]),
    GlFunction(Void, "glBlendBarrierNV", []),

    # GL_NV_conditional_render
    GlFunction(Void, "glBeginConditionalRenderNV", [(GLquery, "id"), (GLenum, "mode")]),
    GlFunction(Void, "glEndConditionalRenderNV", []),

    # GL_NV_copy_image
    GlFunction(Void, "glCopyImageSubDataNV", [(GLtexture, "srcName"), (GLenum, "srcTarget"), (GLint, "srcLevel"), (GLint, "srcX"), (GLint, "srcY"), (GLint, "srcZ"), (GLtexture, "dstName"), (GLenum, "dstTarget"), (GLint, "dstLevel"), (GLint, "dstX"), (GLint, "dstY"), (GLint, "dstZ"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth")]),

    # GL_NV_coverage_sample
    GlFunction(Void, "glCoverageMaskNV", [(GLboolean, "mask")]),
    GlFunction(Void, "glCoverageOperationNV", [(GLenum, "operation")]),

    # GL_NV_depth_buffer_float
    GlFunction(Void, "glDepthRangedNV", [(GLdouble, "zNear"), (GLdouble, "zFar")]),
    GlFunction(Void, "glClearDepthdNV", [(GLdouble, "depth")]),
    GlFunction(Void, "glDepthBoundsdNV", [(GLdouble, "zmin"), (GLdouble, "zmax")]),

    # GL_NV_draw_buffers
    GlFunction(Void, "glDrawBuffersNV", [(GLsizei, "n"), (Array(Const(GLenum), "n"), "bufs")]),

    # GL_NV_draw_texture
    GlFunction(Void, "glDrawTextureNV", [(GLtexture, "texture"), (GLsampler, "sampler"), (GLfloat, "x0"), (GLfloat, "y0"), (GLfloat, "x1"), (GLfloat, "y1"), (GLfloat, "z"), (GLfloat, "s0"), (GLfloat, "t0"), (GLfloat, "s1"), (GLfloat, "t1")]),

    # GL_NV_evaluators
    GlFunction(Void, "glMapControlPointsNV", [(GLenum, "target"), (GLuint, "index"), (GLenum, "type"), (GLsizei, "ustride"), (GLsizei, "vstride"), (GLint, "uorder"), (GLint, "vorder"), (GLboolean, "packed"), (OpaqueBlob(Const(GLvoid), "_glMapControlPointsNV_size(target, uorder, vorder)"), "points")]),
    GlFunction(Void, "glMapParameterivNV", [(GLenum, "target"), (GLenum, "pname"), (OpaqueArray(Const(GLint), "_glMapParameterivNV_size(target, pname)"), "params")]),
    GlFunction(Void, "glMapParameterfvNV", [(GLenum, "target"), (GLenum, "pname"), (OpaqueArray(Const(GLfloat), "_glMapParameterfvNV_size(target, pname)"), "params")]),
    GlFunction(Void, "glGetMapControlPointsNV", [(GLenum, "target"), (GLuint, "index"), (GLenum, "type"), (GLsizei, "ustride"), (GLsizei, "vstride"), (GLboolean, "packed"), Out(OpaqueBlob(GLvoid, "_glGetMapControlPointsNV_size(target)"), "points")], sideeffects=False),
    GlFunction(Void, "glGetMapParameterivNV", [(GLenum, "target"), (GLenum, "pname"), Out(OpaqueArray(GLint, "_glGetMapParameterivNV_size(target, pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMapParameterfvNV", [(GLenum, "target"), (GLenum, "pname"), Out(OpaqueArray(GLfloat, "_glGetMapParameterfvNV_size(target, pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMapAttribParameterivNV", [(GLenum, "target"), (GLuint, "index"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetMapAttribParameterfvNV", [(GLenum, "target"), (GLuint, "index"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glEvalMapsNV", [(GLenum, "target"), (GLenum, "mode")]),

    # GL_NV_explicit_multisample
    GlFunction(Void, "glGetMultisamplefvNV", [(GLenum, "pname"), (GLuint, "index"), Out(Array(GLfloat, 2), "val")], sideeffects=False),
    GlFunction(Void, "glSampleMaskIndexedNV", [(GLuint, "index"), (GLbitfield, "mask")]),
    GlFunction(Void, "glTexRenderbufferNV", [(GLenum, "target"), (GLrenderbuffer, "renderbuffer")]),

    # GL_NV_fence
    GlFunction(Void, "glDeleteFencesNV", [(GLsizei, "n"), (Array(Const(GLfence), "n"), "fences")]),
    GlFunction(Void, "glGenFencesNV", [(GLsizei, "n"), Out(Array(GLfence, "n"), "fences")]),
    GlFunction(GLboolean, "glIsFenceNV", [(GLfence, "fence")], sideeffects=False),
    GlFunction(GLboolean, "glTestFenceNV", [(GLfence, "fence")]),
    GlFunction(Void, "glGetFenceivNV", [(GLfence, "fence"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glFinishFenceNV", [(GLfence, "fence")]),
    GlFunction(Void, "glSetFenceNV", [(GLfence, "fence"), (GLenum, "condition")]),

    # GL_NV_fragment_program
    GlFunction(Void, "glProgramNamedParameter4fNV", [(GLprogramARB, "id"), (GLsizei, "len"), (String(Const(GLubyte), "len"), "name"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glProgramNamedParameter4dNV", [(GLprogramARB, "id"), (GLsizei, "len"), (String(Const(GLubyte), "len"), "name"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glProgramNamedParameter4fvNV", [(GLprogramARB, "id"), (GLsizei, "len"), (String(Const(GLubyte), "len"), "name"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glProgramNamedParameter4dvNV", [(GLprogramARB, "id"), (GLsizei, "len"), (String(Const(GLubyte), "len"), "name"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glGetProgramNamedParameterdvNV", [(GLprogramARB, "id"), (GLsizei, "len"), (String(Const(GLubyte), "len"), "name"), Out(Array(GLdouble, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramNamedParameterfvNV", [(GLprogramARB, "id"), (GLsizei, "len"), (String(Const(GLubyte), "len"), "name"), Out(Array(GLfloat, 4), "params")], sideeffects=False),

    # GL_NV_framebuffer_blit
    GlFunction(Void, "glBlitFramebufferNV", [(GLint, "srcX0"), (GLint, "srcY0"), (GLint, "srcX1"), (GLint, "srcY1"), (GLint, "dstX0"), (GLint, "dstY0"), (GLint, "dstX1"), (GLint, "dstY1"), (GLbitfield_attrib, "mask"), (GLenum, "filter")]),

    # GL_NV_framebuffer_mixed_samples
    GlFunction(Void, "glCoverageModulationTableNV", [(GLsizei, "n"), (Array(Const(GLfloat), "n"), "v")]),
    GlFunction(Void, "glGetCoverageModulationTableNV", [(GLsizei, "bufsize"), Out(Array(GLfloat, "bufsize"), "v")], sideeffects=False),
    GlFunction(Void, "glCoverageModulationNV", [(GLenum, "components")]),

    # GL_NV_framebuffer_multisample_coverage
    GlFunction(Void, "glRenderbufferStorageMultisampleCoverageNV", [(GLenum, "target"), (GLsizei, "coverageSamples"), (GLsizei, "colorSamples"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),

    # GL_NV_geometry_program4
    GlFunction(Void, "glProgramVertexLimitNV", [(GLenum, "target"), (GLint, "limit")]),
    GlFunction(Void, "glFramebufferTextureFaceEXT", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLenum, "face")]),

    # GL_NV_gpu_program4
    GlFunction(Void, "glProgramLocalParameterI4iNV", [(GLenum, "target"), (GLuint, "index"), (GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glProgramLocalParameterI4ivNV", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLint), 4), "params")]),
    GlFunction(Void, "glProgramLocalParametersI4ivNV", [(GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "params")]),
    GlFunction(Void, "glProgramLocalParameterI4uiNV", [(GLenum, "target"), (GLuint, "index"), (GLuint, "x"), (GLuint, "y"), (GLuint, "z"), (GLuint, "w")]),
    GlFunction(Void, "glProgramLocalParameterI4uivNV", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLuint), 4), "params")]),
    GlFunction(Void, "glProgramLocalParametersI4uivNV", [(GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLuint), "count*4"), "params")]),
    GlFunction(Void, "glProgramEnvParameterI4iNV", [(GLenum, "target"), (GLuint, "index"), (GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glProgramEnvParameterI4ivNV", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLint), 4), "params")]),
    GlFunction(Void, "glProgramEnvParametersI4ivNV", [(GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "params")]),
    GlFunction(Void, "glProgramEnvParameterI4uiNV", [(GLenum, "target"), (GLuint, "index"), (GLuint, "x"), (GLuint, "y"), (GLuint, "z"), (GLuint, "w")]),
    GlFunction(Void, "glProgramEnvParameterI4uivNV", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLuint), 4), "params")]),
    GlFunction(Void, "glProgramEnvParametersI4uivNV", [(GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLuint), "count*4"), "params")]),
    GlFunction(Void, "glGetProgramLocalParameterIivNV", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLint, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramLocalParameterIuivNV", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLuint, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramEnvParameterIivNV", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLint, 4), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramEnvParameterIuivNV", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLuint, 4), "params")], sideeffects=False),

    # GL_NV_gpu_program5
    GlFunction(Void, "glProgramSubroutineParametersuivNV", [(GLenum, "target"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "params")]),
    GlFunction(Void, "glGetProgramSubroutineParameteruivNV", [(GLenum, "target"), (GLuint, "index"), Out(Pointer(GLuint), "param")], sideeffects=False),

    # GL_NV_gpu_shader5
    GlFunction(Void, "glUniform1i64NV", [(GLlocation, "location"), (GLint64EXT, "x")]),
    GlFunction(Void, "glUniform2i64NV", [(GLlocation, "location"), (GLint64EXT, "x"), (GLint64EXT, "y")]),
    GlFunction(Void, "glUniform3i64NV", [(GLlocation, "location"), (GLint64EXT, "x"), (GLint64EXT, "y"), (GLint64EXT, "z")]),
    GlFunction(Void, "glUniform4i64NV", [(GLlocation, "location"), (GLint64EXT, "x"), (GLint64EXT, "y"), (GLint64EXT, "z"), (GLint64EXT, "w")]),
    GlFunction(Void, "glUniform1i64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64EXT), "count"), "value")]),
    GlFunction(Void, "glUniform2i64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64EXT), "count*2"), "value")]),
    GlFunction(Void, "glUniform3i64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64EXT), "count*3"), "value")]),
    GlFunction(Void, "glUniform4i64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64EXT), "count*4"), "value")]),
    GlFunction(Void, "glUniform1ui64NV", [(GLlocation, "location"), (GLuint64EXT, "x")]),
    GlFunction(Void, "glUniform2ui64NV", [(GLlocation, "location"), (GLuint64EXT, "x"), (GLuint64EXT, "y")]),
    GlFunction(Void, "glUniform3ui64NV", [(GLlocation, "location"), (GLuint64EXT, "x"), (GLuint64EXT, "y"), (GLuint64EXT, "z")]),
    GlFunction(Void, "glUniform4ui64NV", [(GLlocation, "location"), (GLuint64EXT, "x"), (GLuint64EXT, "y"), (GLuint64EXT, "z"), (GLuint64EXT, "w")]),
    GlFunction(Void, "glUniform1ui64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count"), "value")]),
    GlFunction(Void, "glUniform2ui64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count*2"), "value")]),
    GlFunction(Void, "glUniform3ui64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count*3"), "value")]),
    GlFunction(Void, "glUniform4ui64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count*4"), "value")]),
    GlFunction(Void, "glGetUniformi64vNV", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaqueArray(GLint64EXT, "_glGetUniformi64vNV_size(location)"), "params")], sideeffects=False),
    GlFunction(Void, "glProgramUniform1i64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLint64EXT, "x")]),
    GlFunction(Void, "glProgramUniform2i64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLint64EXT, "x"), (GLint64EXT, "y")]),
    GlFunction(Void, "glProgramUniform3i64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLint64EXT, "x"), (GLint64EXT, "y"), (GLint64EXT, "z")]),
    GlFunction(Void, "glProgramUniform4i64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLint64EXT, "x"), (GLint64EXT, "y"), (GLint64EXT, "z"), (GLint64EXT, "w")]),
    GlFunction(Void, "glProgramUniform1i64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64EXT), "count"), "value")]),
    GlFunction(Void, "glProgramUniform2i64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64EXT), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform3i64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64EXT), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform4i64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLint64EXT), "count*4"), "value")]),
    GlFunction(Void, "glProgramUniform1ui64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64EXT, "x")]),
    GlFunction(Void, "glProgramUniform2ui64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64EXT, "x"), (GLuint64EXT, "y")]),
    GlFunction(Void, "glProgramUniform3ui64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64EXT, "x"), (GLuint64EXT, "y"), (GLuint64EXT, "z")]),
    GlFunction(Void, "glProgramUniform4ui64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64EXT, "x"), (GLuint64EXT, "y"), (GLuint64EXT, "z"), (GLuint64EXT, "w")]),
    GlFunction(Void, "glProgramUniform1ui64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count"), "value")]),
    GlFunction(Void, "glProgramUniform2ui64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count*2"), "value")]),
    GlFunction(Void, "glProgramUniform3ui64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count*3"), "value")]),
    GlFunction(Void, "glProgramUniform4ui64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count*4"), "value")]),

    # GL_NV_half_float
    GlFunction(Void, "glVertex2hNV", [(GLhalfNV, "x"), (GLhalfNV, "y")]),
    GlFunction(Void, "glVertex2hvNV", [(Array(Const(GLhalfNV), 2), "v")]),
    GlFunction(Void, "glVertex3hNV", [(GLhalfNV, "x"), (GLhalfNV, "y"), (GLhalfNV, "z")]),
    GlFunction(Void, "glVertex3hvNV", [(Array(Const(GLhalfNV), 3), "v")]),
    GlFunction(Void, "glVertex4hNV", [(GLhalfNV, "x"), (GLhalfNV, "y"), (GLhalfNV, "z"), (GLhalfNV, "w")]),
    GlFunction(Void, "glVertex4hvNV", [(Array(Const(GLhalfNV), 4), "v")]),
    GlFunction(Void, "glNormal3hNV", [(GLhalfNV, "nx"), (GLhalfNV, "ny"), (GLhalfNV, "nz")]),
    GlFunction(Void, "glNormal3hvNV", [(Array(Const(GLhalfNV), 3), "v")]),
    GlFunction(Void, "glColor3hNV", [(GLhalfNV, "red"), (GLhalfNV, "green"), (GLhalfNV, "blue")]),
    GlFunction(Void, "glColor3hvNV", [(Array(Const(GLhalfNV), 3), "v")]),
    GlFunction(Void, "glColor4hNV", [(GLhalfNV, "red"), (GLhalfNV, "green"), (GLhalfNV, "blue"), (GLhalfNV, "alpha")]),
    GlFunction(Void, "glColor4hvNV", [(Array(Const(GLhalfNV), 4), "v")]),
    GlFunction(Void, "glTexCoord1hNV", [(GLhalfNV, "s")]),
    GlFunction(Void, "glTexCoord1hvNV", [(Pointer(Const(GLhalfNV)), "v")]),
    GlFunction(Void, "glTexCoord2hNV", [(GLhalfNV, "s"), (GLhalfNV, "t")]),
    GlFunction(Void, "glTexCoord2hvNV", [(Array(Const(GLhalfNV), 2), "v")]),
    GlFunction(Void, "glTexCoord3hNV", [(GLhalfNV, "s"), (GLhalfNV, "t"), (GLhalfNV, "r")]),
    GlFunction(Void, "glTexCoord3hvNV", [(Array(Const(GLhalfNV), 3), "v")]),
    GlFunction(Void, "glTexCoord4hNV", [(GLhalfNV, "s"), (GLhalfNV, "t"), (GLhalfNV, "r"), (GLhalfNV, "q")]),
    GlFunction(Void, "glTexCoord4hvNV", [(Array(Const(GLhalfNV), 4), "v")]),
    GlFunction(Void, "glMultiTexCoord1hNV", [(GLenum, "target"), (GLhalfNV, "s")]),
    GlFunction(Void, "glMultiTexCoord1hvNV", [(GLenum, "target"), (Pointer(Const(GLhalfNV)), "v")]),
    GlFunction(Void, "glMultiTexCoord2hNV", [(GLenum, "target"), (GLhalfNV, "s"), (GLhalfNV, "t")]),
    GlFunction(Void, "glMultiTexCoord2hvNV", [(GLenum, "target"), (Array(Const(GLhalfNV), 2), "v")]),
    GlFunction(Void, "glMultiTexCoord3hNV", [(GLenum, "target"), (GLhalfNV, "s"), (GLhalfNV, "t"), (GLhalfNV, "r")]),
    GlFunction(Void, "glMultiTexCoord3hvNV", [(GLenum, "target"), (Array(Const(GLhalfNV), 3), "v")]),
    GlFunction(Void, "glMultiTexCoord4hNV", [(GLenum, "target"), (GLhalfNV, "s"), (GLhalfNV, "t"), (GLhalfNV, "r"), (GLhalfNV, "q")]),
    GlFunction(Void, "glMultiTexCoord4hvNV", [(GLenum, "target"), (Array(Const(GLhalfNV), 4), "v")]),
    GlFunction(Void, "glFogCoordhNV", [(GLhalfNV, "fog")]),
    GlFunction(Void, "glFogCoordhvNV", [(Pointer(Const(GLhalfNV)), "fog")]),
    GlFunction(Void, "glSecondaryColor3hNV", [(GLhalfNV, "red"), (GLhalfNV, "green"), (GLhalfNV, "blue")]),
    GlFunction(Void, "glSecondaryColor3hvNV", [(Array(Const(GLhalfNV), 3), "v")]),
    GlFunction(Void, "glVertexWeighthNV", [(GLhalfNV, "weight")]),
    GlFunction(Void, "glVertexWeighthvNV", [(Pointer(Const(GLhalfNV)), "weight")]),
    GlFunction(Void, "glVertexAttrib1hNV", [(GLuint, "index"), (GLhalfNV, "x")]),
    GlFunction(Void, "glVertexAttrib1hvNV", [(GLuint, "index"), (Pointer(Const(GLhalfNV)), "v")]),
    GlFunction(Void, "glVertexAttrib2hNV", [(GLuint, "index"), (GLhalfNV, "x"), (GLhalfNV, "y")]),
    GlFunction(Void, "glVertexAttrib2hvNV", [(GLuint, "index"), (Array(Const(GLhalfNV), 2), "v")]),
    GlFunction(Void, "glVertexAttrib3hNV", [(GLuint, "index"), (GLhalfNV, "x"), (GLhalfNV, "y"), (GLhalfNV, "z")]),
    GlFunction(Void, "glVertexAttrib3hvNV", [(GLuint, "index"), (Array(Const(GLhalfNV), 3), "v")]),
    GlFunction(Void, "glVertexAttrib4hNV", [(GLuint, "index"), (GLhalfNV, "x"), (GLhalfNV, "y"), (GLhalfNV, "z"), (GLhalfNV, "w")]),
    GlFunction(Void, "glVertexAttrib4hvNV", [(GLuint, "index"), (Array(Const(GLhalfNV), 4), "v")]),
    GlFunction(Void, "glVertexAttribs1hvNV", [(GLuint, "index"), (GLsizei, "n"), (Array(Const(GLhalfNV), "n"), "v")]),
    GlFunction(Void, "glVertexAttribs2hvNV", [(GLuint, "index"), (GLsizei, "n"), (Array(Const(GLhalfNV), "n"), "v")]),
    GlFunction(Void, "glVertexAttribs3hvNV", [(GLuint, "index"), (GLsizei, "n"), (Array(Const(GLhalfNV), "n"), "v")]),
    GlFunction(Void, "glVertexAttribs4hvNV", [(GLuint, "index"), (GLsizei, "n"), (Array(Const(GLhalfNV), "n"), "v")]),

    # GL_NV_occlusion_query
    GlFunction(Void, "glGenOcclusionQueriesNV", [(GLsizei, "n"), Out(Array(GLquery, "n"), "ids")]),
    GlFunction(Void, "glDeleteOcclusionQueriesNV", [(GLsizei, "n"), (Array(Const(GLquery), "n"), "ids")]),
    GlFunction(GLboolean, "glIsOcclusionQueryNV", [(GLquery, "id")], sideeffects=False),
    GlFunction(Void, "glBeginOcclusionQueryNV", [(GLquery, "id")]),
    GlFunction(Void, "glEndOcclusionQueryNV", []),
    GlFunction(Void, "glGetOcclusionQueryivNV", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetOcclusionQueryuivNV", [(GLquery, "id"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_NV_parameter_buffer_object
    GlFunction(Void, "glProgramBufferParametersfvNV", [(GLenum, "target"), (GLbuffer, "buffer"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count"), "params")]),
    GlFunction(Void, "glProgramBufferParametersIivNV", [(GLenum, "target"), (GLbuffer, "buffer"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLint), "count"), "params")]),
    GlFunction(Void, "glProgramBufferParametersIuivNV", [(GLenum, "target"), (GLbuffer, "buffer"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLuint), "count"), "params")]),

    # GL_NV_path_rendering
    GlFunction(GLuint, "glGenPathsNV", [(GLsizei, "range")]),
    GlFunction(Void, "glDeletePathsNV", [(GLuint, "path"), (GLsizei, "range")]),
    GlFunction(GLboolean, "glIsPathNV", [(GLuint, "path")]),
    GlFunction(Void, "glPathCommandsNV", [(GLuint, "path"), (GLsizei, "numCommands"), (Array(Const(GLubyte), "numCommands"), "commands"), (GLsizei, "numCoords"), (GLenum, "coordType"), (Blob(Const(GLvoid), "_glPath_coords_size(numCoords, coordType)"), "coords")]),
    GlFunction(Void, "glPathCoordsNV", [(GLuint, "path"), (GLsizei, "numCoords"), (GLenum, "coordType"), (Blob(Const(GLvoid), "_glPath_coords_size(numCoords, coordType)"), "coords")]),
    GlFunction(Void, "glPathSubCommandsNV", [(GLuint, "path"), (GLsizei, "commandStart"), (GLsizei, "commandsToDelete"), (GLsizei, "numCommands"), (Array(Const(GLubyte), "numCommands"), "commands"), (GLsizei, "numCoords"), (GLenum, "coordType"), (Blob(Const(GLvoid), "_glPath_coords_size(numCoords, coordType)"), "coords")]),
    GlFunction(Void, "glPathSubCoordsNV", [(GLuint, "path"), (GLsizei, "coordStart"), (GLsizei, "numCoords"), (GLenum, "coordType"), (Blob(Const(GLvoid), "_glPath_coords_size(numCoords, coordType)"), "coords")]),
    GlFunction(Void, "glPathStringNV", [(GLuint, "path"), (GLenum, "format"), (GLsizei, "length"), (Blob(Const(GLvoid), "length"), "pathString")]),
    GlFunction(Void, "glPathGlyphsNV", [(GLuint, "firstPathName"), (GLenum, "fontTarget"), (Blob(Const(GLvoid), "_glPath_fontName_size(fontTarget, fontName)"), "fontName"), (GLbitfield_fontStyle, "fontStyle"), (GLsizei, "numGlyphs"), (GLenum, "type"), (Blob(Const(GLvoid), "_glPath_chardcodes_size(numGlyphs, type)"), "charcodes"), (GLenum, "handleMissingGlyphs"), (GLuint, "pathParameterTemplate"), (GLfloat, "emScale")]),
    GlFunction(Void, "glPathGlyphRangeNV", [(GLuint, "firstPathName"), (GLenum, "fontTarget"), (Blob(Const(GLvoid), "_glPath_fontName_size(fontTarget, fontName)"), "fontName"), (GLbitfield_fontStyle, "fontStyle"), (GLuint, "firstGlyph"), (GLsizei, "numGlyphs"), (GLenum, "handleMissingGlyphs"), (GLuint, "pathParameterTemplate"), (GLfloat, "emScale")]),
    GlFunction(Void, "glWeightPathsNV", [(GLuint, "resultPath"), (GLsizei, "numPaths"), (Array(Const(GLuint), "numPaths"), "paths"), (Array(Const(GLfloat), "numPaths"), "weights")]),
    GlFunction(Void, "glCopyPathNV", [(GLuint, "resultPath"), (GLuint, "srcPath")]),
    GlFunction(Void, "glInterpolatePathsNV", [(GLuint, "resultPath"), (GLuint, "pathA"), (GLuint, "pathB"), (GLfloat, "weight")]),
    GlFunction(Void, "glTransformPathNV", [(GLuint, "resultPath"), (GLuint, "srcPath"), (GLenum, "transformType"), (Array(Const(GLfloat), "_gl_transformType_size(transformType)"), "transformValues")]),
    GlFunction(Void, "glPathParameterivNV", [(GLuint, "path"), (GLenum, "pname"), (Array(Const(GLint), "_gl_PathParameter_size(pname)"), "value")]),
    GlFunction(Void, "glPathParameteriNV", [(GLuint, "path"), (GLenum, "pname"), (GLint, "value")]),
    GlFunction(Void, "glPathParameterfvNV", [(GLuint, "path"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_PathParameter_size(pname)"), "value")]),
    GlFunction(Void, "glPathParameterfNV", [(GLuint, "path"), (GLenum, "pname"), (GLfloat, "value")]),
    GlFunction(Void, "glPathDashArrayNV", [(GLuint, "path"), (GLsizei, "dashCount"), (Array(Const(GLfloat), "dashCount"), "dashArray")]),
    GlFunction(Void, "glPathStencilFuncNV", [(GLenum, "func"), (GLint, "ref"), (GLuint, "mask")]),
    GlFunction(Void, "glPathStencilDepthOffsetNV", [(GLfloat, "factor"), (GLfloat, "units")]),
    GlFunction(Void, "glStencilFillPathNV", [(GLuint, "path"), (GLenum, "fillMode"), (GLuint, "mask")]),
    GlFunction(Void, "glStencilStrokePathNV", [(GLuint, "path"), (GLint, "reference"), (GLuint, "mask")]),
    GlFunction(Void, "glStencilFillPathInstancedNV", [(GLsizei, "numPaths"), (GLenum, "pathNameType"), (Blob(Const(GLvoid), "_gl_Paths_size(numPaths, pathNameType, paths)"), "paths"), (GLuint, "pathBase"), (GLenum, "fillMode"), (GLuint, "mask"), (GLenum, "transformType"), (Array(Const(GLfloat), "_gl_transformType_size(numPaths, transformType)"), "transformValues")]),
    GlFunction(Void, "glStencilStrokePathInstancedNV", [(GLsizei, "numPaths"), (GLenum, "pathNameType"), (Blob(Const(GLvoid), "_gl_Paths_size(numPaths, pathNameType, paths)"), "paths"), (GLuint, "pathBase"), (GLint, "reference"), (GLuint, "mask"), (GLenum, "transformType"), (Array(Const(GLfloat), "_gl_transformType_size(numPaths, transformType)"), "transformValues")]),
    GlFunction(Void, "glPathCoverDepthFuncNV", [(GLenum, "func")]),
    GlFunction(Void, "glPathColorGenNV", [(GLenum, "color"), (GLenum, "genMode"), (GLenum, "colorFormat"), (Array(Const(GLfloat), "_gl_PathColorGen_size(genMode, colorFormat)"), "coeffs")]),
    GlFunction(Void, "glPathTexGenNV", [(GLenum, "texCoordSet"), (GLenum, "genMode"), (GLint, "components"), (Array(Const(GLfloat), "_gl_PathTexGen_size(genMode, components)"), "coeffs")]),
    GlFunction(Void, "glPathFogGenNV", [(GLenum, "genMode")]),
    GlFunction(Void, "glCoverFillPathNV", [(GLuint, "path"), (GLenum, "coverMode")]),
    GlFunction(Void, "glCoverStrokePathNV", [(GLuint, "path"), (GLenum, "coverMode")]),
    GlFunction(Void, "glCoverFillPathInstancedNV", [(GLsizei, "numPaths"), (GLenum, "pathNameType"), (Blob(Const(GLvoid), "_gl_Paths_size(numPaths, pathNameType, paths)"), "paths"), (GLuint, "pathBase"), (GLenum, "coverMode"), (GLenum, "transformType"), (Array(Const(GLfloat), "_gl_transformType_size(numPaths, transformType)"), "transformValues")]),
    GlFunction(Void, "glCoverStrokePathInstancedNV", [(GLsizei, "numPaths"), (GLenum, "pathNameType"), (Blob(Const(GLvoid), "_gl_Paths_size(numPaths, pathNameType, paths)"), "paths"), (GLuint, "pathBase"), (GLenum, "coverMode"), (GLenum, "transformType"), (Array(Const(GLfloat), "_gl_transformType_size(numPaths, transformType)"), "transformValues")]),
    GlFunction(Void, "glGetPathParameterivNV", [(GLuint, "path"), (GLenum, "pname"), Out(Array(GLint, "_gl_GetPathParameter_size(pname)"), "value")], sideeffects=False),
    GlFunction(Void, "glGetPathParameterfvNV", [(GLuint, "path"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_GetPathParameter_size(pname)"), "value")], sideeffects=False),
    GlFunction(Void, "glGetPathCommandsNV", [(GLuint, "path"), Out(Pointer(GLubyte), "commands")], sideeffects=False),
    GlFunction(Void, "glGetPathCoordsNV", [(GLuint, "path"), Out(Pointer(GLfloat), "coords")], sideeffects=False),
    GlFunction(Void, "glGetPathDashArrayNV", [(GLuint, "path"), Out(Pointer(GLfloat), "dashArray")], sideeffects=False),
    GlFunction(Void, "glGetPathMetricsNV", [(GLbitfield_metricQueryMask, "metricQueryMask"), (GLsizei, "numPaths"), (GLenum, "pathNameType"), (Blob(Const(GLvoid), "_gl_Paths_size(numPaths, pathNameType, paths)"), "paths"), (GLuint, "pathBase"), (GLsizei, "stride"), Out(Pointer(GLfloat), "metrics")], sideeffects=False),
    GlFunction(Void, "glGetPathMetricRangeNV", [(GLbitfield_metricQueryMask, "metricQueryMask"), (GLuint, "firstPathName"), (GLsizei, "numPaths"), (GLsizei, "stride"), Out(Pointer(GLfloat), "metrics")], sideeffects=False),
    GlFunction(Void, "glGetPathSpacingNV", [(GLenum, "pathListMode"), (GLsizei, "numPaths"), (GLenum, "pathNameType"), (Blob(Const(GLvoid), "_gl_Paths_size(numPaths, pathNameType, paths)"), "paths"), (GLuint, "pathBase"), (GLfloat, "advanceScale"), (GLfloat, "kerningScale"), (GLenum, "transformType"), Out(Array(GLfloat, "_gl_GetPathSpacing(numPaths,transformType)"),  "returnedSpacing")]),
    GlFunction(Void, "glGetPathColorGenivNV", [(GLenum, "color"), (GLenum, "pname"), Out(Pointer(GLint), "value")], sideeffects=False),
    GlFunction(Void, "glGetPathColorGenfvNV", [(GLenum, "color"), (GLenum, "pname"), Out(Pointer(GLfloat), "value")], sideeffects=False),
    GlFunction(Void, "glGetPathTexGenivNV", [(GLenum, "texCoordSet"), (GLenum, "pname"), Out(Pointer(GLint), "value")], sideeffects=False),
    GlFunction(Void, "glGetPathTexGenfvNV", [(GLenum, "texCoordSet"), (GLenum, "pname"), Out(Pointer(GLfloat), "value")], sideeffects=False),
    GlFunction(GLboolean, "glIsPointInFillPathNV", [(GLuint, "path"), (GLuint, "mask"), (GLfloat, "x"), (GLfloat, "y")], sideeffects=False),
    GlFunction(GLboolean, "glIsPointInStrokePathNV", [(GLuint, "path"), (GLfloat, "x"), (GLfloat, "y")], sideeffects=False),
    GlFunction(GLfloat, "glGetPathLengthNV", [(GLuint, "path"), (GLsizei, "startSegment"), (GLsizei, "numSegments")]),
    GlFunction(GLboolean, "glPointAlongPathNV", [(GLuint, "path"), (GLsizei, "startSegment"), (GLsizei, "numSegments"), (GLfloat, "distance"), Out(Array(GLfloat,1), "x"), Out(Array(GLfloat,1), "y"), Out(Array(GLfloat,1), "tangentX"), Out(Array(GLfloat,1), "tangentY")], sideeffects=False),
    GlFunction(Void, "glMatrixLoad3x2fNV", [(GLenum, "matrixMode"), (Array(Const(GLfloat), 6), "m")]),
    GlFunction(Void, "glMatrixLoad3x3fNV", [(GLenum, "matrixMode"), (Array(Const(GLfloat), 9), "m")]),
    GlFunction(Void, "glMatrixLoadTranspose3x3fNV", [(GLenum, "matrixMode"), (Array(Const(GLfloat), 9), "m")]),
    GlFunction(Void, "glMatrixMult3x2fNV", [(GLenum, "matrixMode"), (Array(Const(GLfloat), 6), "m")]),
    GlFunction(Void, "glMatrixMult3x3fNV", [(GLenum, "matrixMode"), (Array(Const(GLfloat), 9), "m")]),
    GlFunction(Void, "glMatrixMultTranspose3x3fNV", [(GLenum, "matrixMode"), (Array(Const(GLfloat), 9), "m")]),
    GlFunction(Void, "glStencilThenCoverFillPathNV", [(GLuint, "path"), (GLenum, "fillMode"), (GLuint, "mask"), (GLenum, "coverMode")]),
    GlFunction(Void, "glStencilThenCoverStrokePathNV", [(GLuint, "path"), (GLint, "reference"), (GLuint, "mask"), (GLenum, "coverMode")]),
    GlFunction(Void, "glStencilThenCoverFillPathInstancedNV", [(GLsizei, "numPaths"), (GLenum, "pathNameType"), (Blob(Const(GLvoid), "_gl_Paths_size(numPaths, pathNameType, paths)"), "paths"), (GLuint, "pathBase"), (GLenum, "fillMode"), (GLuint, "mask"), (GLenum, "coverMode"), (GLenum, "transformType"), (Array(Const(GLfloat), "_gl_transformType_size(numPaths, transformType)"), "transformValues")]),
    GlFunction(Void, "glStencilThenCoverStrokePathInstancedNV", [(GLsizei, "numPaths"), (GLenum, "pathNameType"), (Blob(Const(GLvoid), "_gl_Paths_size(numPaths, pathNameType, paths)"), "paths"), (GLuint, "pathBase"), (GLint, "reference"), (GLuint, "mask"), (GLenum, "coverMode"), (GLenum, "transformType"), (Array(Const(GLfloat), "_gl_transformType_size(numPaths, transformType)"), "transformValues")]),
    GlFunction(GLenum, "glPathGlyphIndexRangeNV", [(GLenum, "fontTarget"), (String(Const(GLvoid)), "fontName"), (GLbitfield, "fontStyle"), (GLuint, "pathParameterTemplate"), (GLfloat, "emScale"), (Array(GLuint, 2), "baseAndCount")]),
    GlFunction(GLenum, "glPathGlyphIndexArrayNV", [(GLuint, "firstPathName"), (GLenum, "fontTarget"), (String(Const(GLvoid)), "fontName"), (GLbitfield, "fontStyle"), (GLuint, "firstGlyphIndex"), (GLsizei, "numGlyphs"), (GLuint, "pathParameterTemplate"), (GLfloat, "emScale")]),
    GlFunction(GLenum, "glPathMemoryGlyphIndexArrayNV", [(GLuint, "firstPathName"), (GLenum, "fontTarget"), (GLsizeiptr, "fontSize"), (Blob(Const(Void), "fontSize"), "fontData"), (GLsizei, "faceIndex"), (GLuint, "firstGlyphIndex"), (GLsizei, "numGlyphs"), (GLuint, "pathParameterTemplate"), (GLfloat, "emScale")]),
    GlFunction(Void, "glProgramPathFragmentInputGenNV", [(GLprogram, "program"), (GLlocation, "location"), (GLenum, "genMode"), (GLint, "components"), (Array(Const(GLfloat), "_gl_PathTexGen_size(genMode, components)"), "coeffs")]),
    GlFunction(Void, "glGetProgramResourcefvNV", [(GLprogram, "program"), (GLenum, "programInterface"), (GLuint, "index"), (GLsizei, "propCount"), (Array(Const(GLenum), "propCount"), "props"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Array(GLfloat, "bufSize"), "params")], sideeffects=False),

    # GL_NV_pixel_data_range
    GlFunction(Void, "glPixelDataRangeNV", [(GLenum, "target"), (GLsizei, "length"), (OpaqueBlob(Const(GLvoid), "length"), "pointer")]),
    GlFunction(Void, "glFlushPixelDataRangeNV", [(GLenum, "target")]),

    # GL_NV_point_sprite
    GlFunction(Void, "glPointParameteriNV", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glPointParameterivNV", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),

    # GL_NV_present_video
    GlFunction(Void, "glPresentFrameKeyedNV", [(GLuint, "video_slot"), (GLuint64EXT, "minPresentTime"), (GLuint, "beginPresentTimeId"), (GLuint, "presentDurationId"), (GLenum, "type"), (GLenum, "target0"), (GLuint, "fill0"), (GLuint, "key0"), (GLenum, "target1"), (GLuint, "fill1"), (GLuint, "key1")]),
    GlFunction(Void, "glPresentFrameDualFillNV", [(GLuint, "video_slot"), (GLuint64EXT, "minPresentTime"), (GLuint, "beginPresentTimeId"), (GLuint, "presentDurationId"), (GLenum, "type"), (GLenum, "target0"), (GLuint, "fill0"), (GLenum, "target1"), (GLuint, "fill1"), (GLenum, "target2"), (GLuint, "fill2"), (GLenum, "target3"), (GLuint, "fill3")]),
    GlFunction(Void, "glGetVideoivNV", [(GLuint, "video_slot"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVideouivNV", [(GLuint, "video_slot"), (GLenum, "pname"), Out(Array(GLuint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVideoi64vNV", [(GLuint, "video_slot"), (GLenum, "pname"), Out(Array(GLint64EXT, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVideoui64vNV", [(GLuint, "video_slot"), (GLenum, "pname"), Out(Array(GLuint64EXT, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_NV_primitive_restart
    GlFunction(Void, "glPrimitiveRestartNV", []),
    GlFunction(Void, "glPrimitiveRestartIndexNV", [(GLuint, "index")]),

    # GL_NV_read_buffer
    GlFunction(Void, "glReadBufferNV", [(GLenum, "mode")]),

    # GL_NV_register_combiners
    GlFunction(Void, "glCombinerParameterfvNV", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glCombinerParameterfNV", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glCombinerParameterivNV", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glCombinerParameteriNV", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glCombinerInputNV", [(GLenum, "stage"), (GLenum, "portion"), (GLenum, "variable"), (GLenum, "input"), (GLenum, "mapping"), (GLenum, "componentUsage")]),
    GlFunction(Void, "glCombinerOutputNV", [(GLenum, "stage"), (GLenum, "portion"), (GLenum, "abOutput"), (GLenum, "cdOutput"), (GLenum, "sumOutput"), (GLenum, "scale"), (GLenum, "bias"), (GLboolean, "abDotProduct"), (GLboolean, "cdDotProduct"), (GLboolean, "muxSum")]),
    GlFunction(Void, "glFinalCombinerInputNV", [(GLenum, "variable"), (GLenum, "input"), (GLenum, "mapping"), (GLenum, "componentUsage")]),
    GlFunction(Void, "glGetCombinerInputParameterfvNV", [(GLenum, "stage"), (GLenum, "portion"), (GLenum, "variable"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetCombinerInputParameterivNV", [(GLenum, "stage"), (GLenum, "portion"), (GLenum, "variable"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetCombinerOutputParameterfvNV", [(GLenum, "stage"), (GLenum, "portion"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetCombinerOutputParameterivNV", [(GLenum, "stage"), (GLenum, "portion"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetFinalCombinerInputParameterfvNV", [(GLenum, "variable"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetFinalCombinerInputParameterivNV", [(GLenum, "variable"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_NV_register_combiners2
    GlFunction(Void, "glCombinerStageParameterfvNV", [(GLenum, "stage"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetCombinerStageParameterfvNV", [(GLenum, "stage"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_NV_shader_buffer_load
    GlFunction(Void, "glMakeBufferResidentNV", [(GLenum, "target"), (GLenum, "access")]),
    GlFunction(Void, "glMakeBufferNonResidentNV", [(GLenum, "target")]),
    GlFunction(GLboolean, "glIsBufferResidentNV", [(GLenum, "target")], sideeffects=False),
    GlFunction(Void, "glMakeNamedBufferResidentNV", [(GLbuffer, "buffer"), (GLenum, "access")]),
    GlFunction(Void, "glMakeNamedBufferNonResidentNV", [(GLbuffer, "buffer")]),
    GlFunction(GLboolean, "glIsNamedBufferResidentNV", [(GLbuffer, "buffer")], sideeffects=False),
    GlFunction(Void, "glGetBufferParameterui64vNV", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLuint64EXT, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetNamedBufferParameterui64vNV", [(GLbuffer, "buffer"), (GLenum, "pname"), Out(Array(GLuint64EXT, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetIntegerui64vNV", [(GLenum, "value"), Out(Array(GLuint64EXT, "_gl_param_size(value)"), "result")], sideeffects=False),
    GlFunction(Void, "glUniformui64NV", [(GLlocation, "location"), (GLuint64EXT, "value")]),
    GlFunction(Void, "glUniformui64vNV", [(GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count"), "value")]),
    GlFunction(Void, "glGetUniformui64vNV", [(GLprogram, "program"), (GLlocation, "location"), Out(OpaqueArray(GLuint64EXT, "_glGetUniformui64vNV_size(program, location)"), "params")], sideeffects=False),
    GlFunction(Void, "glProgramUniformui64NV", [(GLprogram, "program"), (GLlocation, "location"), (GLuint64EXT, "value")]),
    GlFunction(Void, "glProgramUniformui64vNV", [(GLprogram, "program"), (GLlocation, "location"), (GLsizei, "count"), (Array(Const(GLuint64EXT), "count"), "value")]),

    # GL_NV_texture_barrier
    GlFunction(Void, "glTextureBarrierNV", []),

    # GL_NV_texture_multisample
    GlFunction(Void, "glTexImage2DMultisampleCoverageNV", [(GLenum, "target"), (GLsizei, "coverageSamples"), (GLsizei, "colorSamples"), (GLint, "internalFormat"), (GLsizei, "width"), (GLsizei, "height"), (GLboolean, "fixedSampleLocations")]),
    GlFunction(Void, "glTexImage3DMultisampleCoverageNV", [(GLenum, "target"), (GLsizei, "coverageSamples"), (GLsizei, "colorSamples"), (GLint, "internalFormat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "fixedSampleLocations")]),
    GlFunction(Void, "glTextureImage2DMultisampleNV", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "samples"), (GLint, "internalFormat"), (GLsizei, "width"), (GLsizei, "height"), (GLboolean, "fixedSampleLocations")]),
    GlFunction(Void, "glTextureImage3DMultisampleNV", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "samples"), (GLint, "internalFormat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "fixedSampleLocations")]),
    GlFunction(Void, "glTextureImage2DMultisampleCoverageNV", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "coverageSamples"), (GLsizei, "colorSamples"), (GLint, "internalFormat"), (GLsizei, "width"), (GLsizei, "height"), (GLboolean, "fixedSampleLocations")]),
    GlFunction(Void, "glTextureImage3DMultisampleCoverageNV", [(GLtexture, "texture"), (GLenum, "target"), (GLsizei, "coverageSamples"), (GLsizei, "colorSamples"), (GLint, "internalFormat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLboolean, "fixedSampleLocations")]),

    # GL_NV_transform_feedback
    GlFunction(Void, "glBeginTransformFeedbackNV", [(GLenum_mode, "primitiveMode")]),
    GlFunction(Void, "glEndTransformFeedbackNV", []),
    GlFunction(Void, "glTransformFeedbackAttribsNV", [(GLsizei, "count"), (Array(Const(GLint), "count*3"), "attribs"), (GLenum, "bufferMode")]),
    GlFunction(Void, "glBindBufferRangeNV", [(GLenum, "target"), (GLuint, "index"), (GLbuffer, "buffer"), (GLintptr, "offset"), (GLsizeiptr, "size")]),
    GlFunction(Void, "glBindBufferOffsetNV", [(GLenum, "target"), (GLuint, "index"), (GLbuffer, "buffer"), (GLintptr, "offset")]),
    GlFunction(Void, "glBindBufferBaseNV", [(GLenum, "target"), (GLuint, "index"), (GLbuffer, "buffer")]),
    GlFunction(Void, "glTransformFeedbackVaryingsNV", [(GLprogram, "program"), (GLsizei, "count"), (Array(Const(GLint), "count"), "locations"), (GLenum, "bufferMode")]),
    GlFunction(Void, "glActiveVaryingNV", [(GLprogram, "program"), (GLstringConst, "name")]),
    GlFunction(GLlocation, "glGetVaryingLocationNV", [(GLprogram, "program"), (GLstringConst, "name")]),
    GlFunction(Void, "glGetActiveVaryingNV", [(GLprogram, "program"), (GLuint, "index"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLsizei), "size"), Out(Pointer(GLenum), "type"), OutGlString(GLchar, "length", "name")], sideeffects=False),
    GlFunction(Void, "glGetTransformFeedbackVaryingNV", [(GLprogram, "program"), (GLuint, "index"), Out(Pointer(GLlocation), "location")], sideeffects=False),
    GlFunction(Void, "glTransformFeedbackStreamAttribsNV", [(GLsizei, "count"), (Array(Const(GLint), "count"), "attribs"), (GLsizei, "nbuffers"), (Array(Const(GLint), "nbuffers"), "bufstreams"), (GLenum, "bufferMode")]),

    # GL_NV_transform_feedback2
    GlFunction(Void, "glBindTransformFeedbackNV", [(GLenum, "target"), (GLfeedback, "id")]),
    GlFunction(Void, "glDeleteTransformFeedbacksNV", [(GLsizei, "n"), (Array(Const(GLfeedback), "n"), "ids")]),
    GlFunction(Void, "glGenTransformFeedbacksNV", [(GLsizei, "n"), Out(Array(GLfeedback, "n"), "ids")]),
    GlFunction(GLboolean, "glIsTransformFeedbackNV", [(GLfeedback, "id")], sideeffects=False),
    GlFunction(Void, "glPauseTransformFeedbackNV", []),
    GlFunction(Void, "glResumeTransformFeedbackNV", []),
    GlFunction(Void, "glDrawTransformFeedbackNV", [(GLenum_mode, "mode"), (GLfeedback, "id")]),

    # GL_NV_vdpau_interop
    GlFunction(Void, "glVDPAUInitNV", [(OpaquePointer(Const(GLvoid)), "vdpDevice"), (OpaquePointer(Const(GLvoid)), "getProcAddress")]),
    GlFunction(Void, "glVDPAUFiniNV", []),
    GlFunction(GLvdpauSurfaceNV, "glVDPAURegisterVideoSurfaceNV", [(OpaquePointer(Const(GLvoid)), "vdpSurface"), (GLenum, "target"), (GLsizei, "numTextureNames"), (Array(Const(GLtexture), "numTextureNames"), "textureNames")]),
    GlFunction(GLvdpauSurfaceNV, "glVDPAURegisterOutputSurfaceNV", [(OpaquePointer(Const(GLvoid)), "vdpSurface"), (GLenum, "target"), (GLsizei, "numTextureNames"), (Array(Const(GLtexture), "numTextureNames"), "textureNames")]),
    GlFunction(GLboolean, "glVDPAUIsSurfaceNV", [(GLvdpauSurfaceNV, "surface")], sideeffects=False),
    GlFunction(Void, "glVDPAUUnregisterSurfaceNV", [(GLvdpauSurfaceNV, "surface")]),
    GlFunction(Void, "glVDPAUGetSurfaceivNV", [(GLvdpauSurfaceNV, "surface"), (GLenum, "pname"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Array(GLint, "bufSize"), "values")]),
    GlFunction(Void, "glVDPAUSurfaceAccessNV", [(GLvdpauSurfaceNV, "surface"), (GLenum, "access")]),
    GlFunction(Void, "glVDPAUMapSurfacesNV", [(GLsizei, "numSurfaces"), (Array(Const(GLvdpauSurfaceNV), "numSurfaces"), "surfaces")]),
    GlFunction(Void, "glVDPAUUnmapSurfacesNV", [(GLsizei, "numSurface"), (Array(Const(GLvdpauSurfaceNV), "numSurface"), "surfaces")]),

    # GL_NV_vertex_array_range
    GlFunction(Void, "glFlushVertexArrayRangeNV", []),
    GlFunction(Void, "glVertexArrayRangeNV", [(GLsizei, "length"), (GLpointerConst, "pointer")]),

    # GL_NV_vertex_attrib_integer_64bit
    GlFunction(Void, "glVertexAttribL1i64NV", [(GLuint, "index"), (GLint64EXT, "x")]),
    GlFunction(Void, "glVertexAttribL2i64NV", [(GLuint, "index"), (GLint64EXT, "x"), (GLint64EXT, "y")]),
    GlFunction(Void, "glVertexAttribL3i64NV", [(GLuint, "index"), (GLint64EXT, "x"), (GLint64EXT, "y"), (GLint64EXT, "z")]),
    GlFunction(Void, "glVertexAttribL4i64NV", [(GLuint, "index"), (GLint64EXT, "x"), (GLint64EXT, "y"), (GLint64EXT, "z"), (GLint64EXT, "w")]),
    GlFunction(Void, "glVertexAttribL1i64vNV", [(GLuint, "index"), (Pointer(Const(GLint64EXT)), "v")]),
    GlFunction(Void, "glVertexAttribL2i64vNV", [(GLuint, "index"), (Array(Const(GLint64EXT), 2), "v")]),
    GlFunction(Void, "glVertexAttribL3i64vNV", [(GLuint, "index"), (Array(Const(GLint64EXT), 3), "v")]),
    GlFunction(Void, "glVertexAttribL4i64vNV", [(GLuint, "index"), (Array(Const(GLint64EXT), 4), "v")]),
    GlFunction(Void, "glVertexAttribL1ui64NV", [(GLuint, "index"), (GLuint64EXT, "x")]),
    GlFunction(Void, "glVertexAttribL2ui64NV", [(GLuint, "index"), (GLuint64EXT, "x"), (GLuint64EXT, "y")]),
    GlFunction(Void, "glVertexAttribL3ui64NV", [(GLuint, "index"), (GLuint64EXT, "x"), (GLuint64EXT, "y"), (GLuint64EXT, "z")]),
    GlFunction(Void, "glVertexAttribL4ui64NV", [(GLuint, "index"), (GLuint64EXT, "x"), (GLuint64EXT, "y"), (GLuint64EXT, "z"), (GLuint64EXT, "w")]),
    GlFunction(Void, "glVertexAttribL1ui64vNV", [(GLuint, "index"), (Pointer(Const(GLuint64EXT)), "v")]),
    GlFunction(Void, "glVertexAttribL2ui64vNV", [(GLuint, "index"), (Array(Const(GLuint64EXT), 2), "v")]),
    GlFunction(Void, "glVertexAttribL3ui64vNV", [(GLuint, "index"), (Array(Const(GLuint64EXT), 3), "v")]),
    GlFunction(Void, "glVertexAttribL4ui64vNV", [(GLuint, "index"), (Array(Const(GLuint64EXT), 4), "v")]),
    GlFunction(Void, "glGetVertexAttribLi64vNV", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLint64EXT, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribLui64vNV", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLuint64EXT, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glVertexAttribLFormatNV", [(GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride")]),

    # GL_NV_vertex_buffer_unified_memory
    GlFunction(Void, "glBufferAddressRangeNV", [(GLenum, "pname"), (GLuint, "index"), (GLuint64EXT, "address"), (GLsizeiptr, "length")]),
    GlFunction(Void, "glVertexFormatNV", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride")]),
    GlFunction(Void, "glNormalFormatNV", [(GLenum, "type"), (GLsizei, "stride")]),
    GlFunction(Void, "glColorFormatNV", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride")]),
    GlFunction(Void, "glIndexFormatNV", [(GLenum, "type"), (GLsizei, "stride")]),
    GlFunction(Void, "glTexCoordFormatNV", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride")]),
    GlFunction(Void, "glEdgeFlagFormatNV", [(GLsizei, "stride")]),
    GlFunction(Void, "glSecondaryColorFormatNV", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride")]),
    GlFunction(Void, "glFogCoordFormatNV", [(GLenum, "type"), (GLsizei, "stride")]),
    GlFunction(Void, "glVertexAttribFormatNV", [(GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLboolean, "normalized"), (GLsizei, "stride")]),
    GlFunction(Void, "glVertexAttribIFormatNV", [(GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride")]),
    GlFunction(Void, "glGetIntegerui64i_vNV", [(GLenum, "value"), (GLuint, "index"), Out(Array(GLuint64EXT, "_gl_param_size(value)"), "result")], sideeffects=False),

    # GL_NV_vertex_program
    GlFunction(GLboolean, "glAreProgramsResidentNV", [(GLsizei, "n"), (Array(Const(GLprogramARB), "n"), "ids"), Out(Array(GLboolean, "n"), "residences")], sideeffects=False),
    GlFunction(Void, "glBindProgramNV", [(GLenum, "target"), (GLprogramARB, "program")]),
    GlFunction(Void, "glDeleteProgramsNV", [(GLsizei, "n"), (Array(Const(GLprogramARB), "n"), "programs")]),
    GlFunction(Void, "glExecuteProgramNV", [(GLenum, "target"), (GLprogramARB, "id"), (Array(Const(GLfloat), 4), "params")]),
    GlFunction(Void, "glGenProgramsNV", [(GLsizei, "n"), Out(Array(GLprogramARB, "n"), "programs")]),
    GlFunction(Void, "glGetProgramParameterdvNV", [(GLenum, "target"), (GLuint, "index"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramParameterfvNV", [(GLenum, "target"), (GLuint, "index"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramivNV", [(GLprogramARB, "id"), (GLenum, "pname"), Out(Pointer(GLint), "params")], sideeffects=False),
    GlFunction(Void, "glGetProgramStringNV", [(GLprogramARB, "id"), (GLenum, "pname"), Out(Array(GLubyte, "_gl_param_size(pname)"), "program")], sideeffects=False),
    GlFunction(Void, "glGetTrackMatrixivNV", [(GLenum, "target"), (GLuint, "address"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribdvNV", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribfvNV", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribivNV", [(GLuint, "index"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribPointervNV", [(GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLpointer), "pointer")], sideeffects=False),
    GlFunction(GLboolean, "glIsProgramNV", [(GLprogramARB, "program")], sideeffects=False),
    GlFunction(Void, "glLoadProgramNV", [(GLenum, "target"), (GLprogramARB, "id"), (GLsizei, "len"), (String(Const(GLubyte), "len"), "program")]),
    GlFunction(Void, "glProgramParameter4dNV", [(GLenum, "target"), (GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glProgramParameter4dvNV", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glProgramParameter4fNV", [(GLenum, "target"), (GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glProgramParameter4fvNV", [(GLenum, "target"), (GLuint, "index"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glProgramParameters4dvNV", [(GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLdouble), "count*4"), "v")]),
    GlFunction(Void, "glProgramParameters4fvNV", [(GLenum, "target"), (GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "v")]),
    GlFunction(Void, "glRequestResidentProgramsNV", [(GLsizei, "n"), (Array(Const(GLprogramARB), "n"), "programs")]),
    GlFunction(Void, "glTrackMatrixNV", [(GLenum, "target"), (GLuint, "address"), (GLenum, "matrix"), (GLenum, "transform")]),
    GlFunction(Void, "glVertexAttribPointerNV", [(GLuint, "index"), (size_bgra, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glVertexAttrib1dNV", [(GLuint, "index"), (GLdouble, "x")]),
    GlFunction(Void, "glVertexAttrib1dvNV", [(GLuint, "index"), (Pointer(Const(GLdouble)), "v")]),
    GlFunction(Void, "glVertexAttrib1fNV", [(GLuint, "index"), (GLfloat, "x")]),
    GlFunction(Void, "glVertexAttrib1fvNV", [(GLuint, "index"), (Pointer(Const(GLfloat)), "v")]),
    GlFunction(Void, "glVertexAttrib1sNV", [(GLuint, "index"), (GLshort, "x")]),
    GlFunction(Void, "glVertexAttrib1svNV", [(GLuint, "index"), (Pointer(Const(GLshort)), "v")]),
    GlFunction(Void, "glVertexAttrib2dNV", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y")]),
    GlFunction(Void, "glVertexAttrib2dvNV", [(GLuint, "index"), (Array(Const(GLdouble), 2), "v")]),
    GlFunction(Void, "glVertexAttrib2fNV", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glVertexAttrib2fvNV", [(GLuint, "index"), (Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glVertexAttrib2sNV", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y")]),
    GlFunction(Void, "glVertexAttrib2svNV", [(GLuint, "index"), (Array(Const(GLshort), 2), "v")]),
    GlFunction(Void, "glVertexAttrib3dNV", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z")]),
    GlFunction(Void, "glVertexAttrib3dvNV", [(GLuint, "index"), (Array(Const(GLdouble), 3), "v")]),
    GlFunction(Void, "glVertexAttrib3fNV", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glVertexAttrib3fvNV", [(GLuint, "index"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glVertexAttrib3sNV", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y"), (GLshort, "z")]),
    GlFunction(Void, "glVertexAttrib3svNV", [(GLuint, "index"), (Array(Const(GLshort), 3), "v")]),
    GlFunction(Void, "glVertexAttrib4dNV", [(GLuint, "index"), (GLdouble, "x"), (GLdouble, "y"), (GLdouble, "z"), (GLdouble, "w")]),
    GlFunction(Void, "glVertexAttrib4dvNV", [(GLuint, "index"), (Array(Const(GLdouble), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4fNV", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glVertexAttrib4fvNV", [(GLuint, "index"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4sNV", [(GLuint, "index"), (GLshort, "x"), (GLshort, "y"), (GLshort, "z"), (GLshort, "w")]),
    GlFunction(Void, "glVertexAttrib4svNV", [(GLuint, "index"), (Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glVertexAttrib4ubNV", [(GLuint, "index"), (GLubyte, "x"), (GLubyte, "y"), (GLubyte, "z"), (GLubyte, "w")]),
    GlFunction(Void, "glVertexAttrib4ubvNV", [(GLuint, "index"), (Array(Const(GLubyte), 4), "v")]),
    GlFunction(Void, "glVertexAttribs1dvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLdouble), "count"), "v")]),
    GlFunction(Void, "glVertexAttribs1fvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count"), "v")]),
    GlFunction(Void, "glVertexAttribs1svNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLshort), "count"), "v")]),
    GlFunction(Void, "glVertexAttribs2dvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLdouble), "count*2"), "v")]),
    GlFunction(Void, "glVertexAttribs2fvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count*2"), "v")]),
    GlFunction(Void, "glVertexAttribs2svNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLshort), "count*2"), "v")]),
    GlFunction(Void, "glVertexAttribs3dvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLdouble), "count*3"), "v")]),
    GlFunction(Void, "glVertexAttribs3fvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count*3"), "v")]),
    GlFunction(Void, "glVertexAttribs3svNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLshort), "count*3"), "v")]),
    GlFunction(Void, "glVertexAttribs4dvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLdouble), "count*4"), "v")]),
    GlFunction(Void, "glVertexAttribs4fvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "v")]),
    GlFunction(Void, "glVertexAttribs4svNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLshort), "count*4"), "v")]),
    GlFunction(Void, "glVertexAttribs4ubvNV", [(GLuint, "index"), (GLsizei, "count"), (Array(Const(GLubyte), "count*4"), "v")]),

    # GL_NV_vertex_program4
    GlFunction(Void, "glVertexAttribI1iEXT", [(GLuint, "index"), (GLint, "x")]),
    GlFunction(Void, "glVertexAttribI2iEXT", [(GLuint, "index"), (GLint, "x"), (GLint, "y")]),
    GlFunction(Void, "glVertexAttribI3iEXT", [(GLuint, "index"), (GLint, "x"), (GLint, "y"), (GLint, "z")]),
    GlFunction(Void, "glVertexAttribI4iEXT", [(GLuint, "index"), (GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "w")]),
    GlFunction(Void, "glVertexAttribI1uiEXT", [(GLuint, "index"), (GLuint, "x")]),
    GlFunction(Void, "glVertexAttribI2uiEXT", [(GLuint, "index"), (GLuint, "x"), (GLuint, "y")]),
    GlFunction(Void, "glVertexAttribI3uiEXT", [(GLuint, "index"), (GLuint, "x"), (GLuint, "y"), (GLuint, "z")]),
    GlFunction(Void, "glVertexAttribI4uiEXT", [(GLuint, "index"), (GLuint, "x"), (GLuint, "y"), (GLuint, "z"), (GLuint, "w")]),
    GlFunction(Void, "glVertexAttribI1ivEXT", [(GLuint, "index"), (Pointer(Const(GLint)), "v")]),
    GlFunction(Void, "glVertexAttribI2ivEXT", [(GLuint, "index"), (Array(Const(GLint), 2), "v")]),
    GlFunction(Void, "glVertexAttribI3ivEXT", [(GLuint, "index"), (Array(Const(GLint), 3), "v")]),
    GlFunction(Void, "glVertexAttribI4ivEXT", [(GLuint, "index"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glVertexAttribI1uivEXT", [(GLuint, "index"), (Pointer(Const(GLuint)), "v")]),
    GlFunction(Void, "glVertexAttribI2uivEXT", [(GLuint, "index"), (Array(Const(GLuint), 2), "v")]),
    GlFunction(Void, "glVertexAttribI3uivEXT", [(GLuint, "index"), (Array(Const(GLuint), 3), "v")]),
    GlFunction(Void, "glVertexAttribI4uivEXT", [(GLuint, "index"), (Array(Const(GLuint), 4), "v")]),
    GlFunction(Void, "glVertexAttribI4bvEXT", [(GLuint, "index"), (Array(Const(GLbyte), 4), "v")]),
    GlFunction(Void, "glVertexAttribI4svEXT", [(GLuint, "index"), (Array(Const(GLshort), 4), "v")]),
    GlFunction(Void, "glVertexAttribI4ubvEXT", [(GLuint, "index"), (Array(Const(GLubyte), 4), "v")]),
    GlFunction(Void, "glVertexAttribI4usvEXT", [(GLuint, "index"), (Array(Const(GLushort), 4), "v")]),
    GlFunction(Void, "glVertexAttribIPointerEXT", [(GLuint, "index"), (GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glGetVertexAttribIivEXT", [(GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLint), "params")], sideeffects=False),
    GlFunction(Void, "glGetVertexAttribIuivEXT", [(GLuint, "index"), (GLenum, "pname"), Out(Pointer(GLuint), "params")], sideeffects=False),

    # GL_NV_video_capture
    GlFunction(Void, "glBeginVideoCaptureNV", [(GLuint, "video_capture_slot")]),
    GlFunction(Void, "glBindVideoCaptureStreamBufferNV", [(GLuint, "video_capture_slot"), (GLuint, "stream"), (GLenum, "frame_region"), (GLintptrARB, "offset")]),
    GlFunction(Void, "glBindVideoCaptureStreamTextureNV", [(GLuint, "video_capture_slot"), (GLuint, "stream"), (GLenum, "frame_region"), (GLenum, "target"), (GLuint, "texture")]),
    GlFunction(Void, "glEndVideoCaptureNV", [(GLuint, "video_capture_slot")]),
    GlFunction(Void, "glGetVideoCaptureivNV", [(GLuint, "video_capture_slot"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVideoCaptureStreamivNV", [(GLuint, "video_capture_slot"), (GLuint, "stream"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVideoCaptureStreamfvNV", [(GLuint, "video_capture_slot"), (GLuint, "stream"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetVideoCaptureStreamdvNV", [(GLuint, "video_capture_slot"), (GLuint, "stream"), (GLenum, "pname"), Out(Array(GLdouble, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLenum, "glVideoCaptureNV", [(GLuint, "video_capture_slot"), Out(Pointer(GLuint), "sequence_num"), Out(Pointer(GLuint64EXT), "capture_time")]),
    GlFunction(Void, "glVideoCaptureStreamParameterivNV", [(GLuint, "video_capture_slot"), (GLuint, "stream"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glVideoCaptureStreamParameterfvNV", [(GLuint, "video_capture_slot"), (GLuint, "stream"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glVideoCaptureStreamParameterdvNV", [(GLuint, "video_capture_slot"), (GLuint, "stream"), (GLenum, "pname"), (Array(Const(GLdouble), "_gl_param_size(pname)"), "params")]),

    # GL_OES_blend_equation_separate
    GlFunction(Void, "glBlendEquationSeparateOES", [(GLenum, "modeRGB"), (GLenum, "modeAlpha")]),

    # GL_OES_blend_func_separate
    GlFunction(Void, "glBlendFuncSeparateOES", [(GLenum, "sfactorRGB"), (GLenum, "dfactorRGB"), (GLenum, "sfactorAlpha"), (GLenum, "dfactorAlpha")]),

    # GL_OES_blend_subtract
    GlFunction(Void, "glBlendEquationOES", [(GLenum, "mode")]),

    # GL_OES_draw_texture
    GlFunction(Void, "glDrawTexfOES", [(GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "width"), (GLfloat, "height")]),
    GlFunction(Void, "glDrawTexfvOES", [(Array(Const(GLfloat), 4), "coords")]),
    GlFunction(Void, "glDrawTexiOES", [(GLint, "x"), (GLint, "y"), (GLint, "z"), (GLint, "width"), (GLint, "height")]),
    GlFunction(Void, "glDrawTexivOES", [(Array(Const(GLint), 4), "coords")]),
    GlFunction(Void, "glDrawTexsOES", [(GLshort, "x"), (GLshort, "y"), (GLshort, "z"), (GLshort, "width"), (GLshort, "height")]),
    GlFunction(Void, "glDrawTexsvOES", [(Array(Const(GLshort), 4), "coords")]),

    # GL_OES_framebuffer_object
    GlFunction(GLboolean, "glIsRenderbufferOES", [(GLrenderbuffer, "renderbuffer")], sideeffects=False),
    GlFunction(Void, "glBindRenderbufferOES", [(GLenum, "target"), (GLrenderbuffer, "renderbuffer")]),
    GlFunction(Void, "glDeleteRenderbuffersOES", [(GLsizei, "n"), (Array(Const(GLrenderbuffer), "n"), "renderbuffers")]),
    GlFunction(Void, "glGenRenderbuffersOES", [(GLsizei, "n"), Out(Array(GLrenderbuffer, "n"), "renderbuffers")]),
    GlFunction(Void, "glRenderbufferStorageOES", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glGetRenderbufferParameterivOES", [(GLenum, "target"), (GLenum, "pname"), (Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(GLboolean, "glIsFramebufferOES", [(GLframebuffer, "framebuffer")], sideeffects=False),
    GlFunction(Void, "glBindFramebufferOES", [(GLenum, "target"), (GLframebuffer, "framebuffer")]),
    GlFunction(Void, "glDeleteFramebuffersOES", [(GLsizei, "n"), (Array(Const(GLframebuffer), "n"), "framebuffers")]),
    GlFunction(Void, "glGenFramebuffersOES", [(GLsizei, "n"), Out(Array(GLframebuffer, "n"), "framebuffers")]),
    GlFunction(GLenum, "glCheckFramebufferStatusOES", [(GLenum, "target")]),
    GlFunction(Void, "glFramebufferTexture2DOES", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level")]),
    GlFunction(Void, "glFramebufferRenderbufferOES", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "renderbuffertarget"), (GLuint, "renderbuffer")]),
    GlFunction(Void, "glGetFramebufferAttachmentParameterivOES", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGenerateMipmapOES", [(GLenum, "target")]),

    # GL_OES_get_program_binary
    GlFunction(Void, "glGetProgramBinaryOES", [(GLprogram, "program"), (GLsizei, "bufSize"), Out(Pointer(GLsizei), "length"), Out(Pointer(GLenum), "binaryFormat"), Out(OpaqueBlob(GLvoid, "length ? *length : bufSize"), "binary")], sideeffects=False),
    GlFunction(Void, "glProgramBinaryOES", [(GLprogram, "program"), (GLenum, "binaryFormat"), (Blob(Const(GLvoid), "length"), "binary"), (GLsizei, "length")]),

    # GL_OES_mapbuffer
    GlFunction(Void, "glGetBufferPointervOES", [(GLenum, "target"), (GLenum, "pname"), Out(Pointer(GLpointer), "params")], sideeffects=False),
    GlFunction(GLmap, "glMapBufferOES", [(GLenum, "target"), (GLenum, "access")]),
    GlFunction(GLboolean, "glUnmapBufferOES", [(GLenum, "target")]),

    # GL_OES_matrix_palette
    GlFunction(Void, "glCurrentPaletteMatrixOES", [(GLuint, "index")]),
    GlFunction(Void, "glLoadPaletteFromModelViewMatrixOES", []),
    GlFunction(Void, "glMatrixIndexPointerOES", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),
    GlFunction(Void, "glWeightPointerOES", [(GLint, "size"), (GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "pointer")]),

    # GL_OES_point_size_array
    GlFunction(Void, "glPointSizePointerOES", [(GLenum, "type"), (GLsizei, "stride"), (GLpointerConst, "ptr")]),

    # GL_OES_query_matrix
    GlFunction(GLbitfield, "glQueryMatrixxOES", [(Array(GLfixed, 16), "mantissa"), (Array(GLint, 16), "exponent")]),

    # GL_OES_single_precision
    GlFunction(Void, "glClearDepthfOES", [(GLclampf, "depth")]),
    GlFunction(Void, "glClipPlanefOES", [(GLenum, "plane"), (Array(Const(GLfloat), 4), "equation")]),
    GlFunction(Void, "glDepthRangefOES", [(GLclampf, "n"), (GLclampf, "f")]),
    GlFunction(Void, "glFrustumfOES", [(GLfloat, "l"), (GLfloat, "r"), (GLfloat, "b"), (GLfloat, "t"), (GLfloat, "n"), (GLfloat, "f")]),
    GlFunction(Void, "glGetClipPlanefOES", [(GLenum, "plane"), Out(Array(GLfloat, 4), "equation")], sideeffects=False),
    GlFunction(Void, "glOrthofOES", [(GLfloat, "l"), (GLfloat, "r"), (GLfloat, "b"), (GLfloat, "t"), (GLfloat, "n"), (GLfloat, "f")]),

    # GL_OES_texture_3D
    GlFunction(Void, "glTexImage3DOES", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glTexSubImage3DOES", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glTexImage3D_size(format, type, width, height, depth)"), "pixels")]),
    GlFunction(Void, "glCopyTexSubImage3DOES", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glCompressedTexImage3DOES", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLint, "border"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, internalformat, width, height, depth, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glCompressedTexSubImage3DOES", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLenum, "format"), (GLsizei, "imageSize"), (Blob(Const(GLvoid), "writeCompressedTex(data, format, width, height, depth, imageSize, can_unpack_subimage(), {})"), "data")]),
    GlFunction(Void, "glFramebufferTexture3DOES", [(GLenum, "target"), (GLenum, "attachment"), (GLenum, "textarget"), (GLtexture, "texture"), (GLint, "level"), (GLint, "zoffset")]),

    # GL_OES_texture_cube_map
    GlFunction(Void, "glTexGenfOES", [(GLenum, "coord"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glTexGenfvOES", [(GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexGeniOES", [(GLenum, "coord"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glTexGenivOES", [(GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glTexGenxOES", [(GLenum, "coord"), (GLenum, "pname"), (GLfixed, "param")]),
    GlFunction(Void, "glTexGenxvOES", [(GLenum, "coord"), (GLenum, "pname"), (Array(Const(GLfixed), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetTexGenfvOES", [(GLenum, "coord"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexGenivOES", [(GLenum, "coord"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetTexGenxvOES", [(GLenum, "coord"), (GLenum, "pname"), Out(Array(GLfixed, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_OES_vertex_array_object
    GlFunction(Void, "glBindVertexArrayOES", [(GLarray, "array")]),
    GlFunction(Void, "glDeleteVertexArraysOES", [(GLsizei, "n"), (Array(Const(GLarray), "n"), "arrays")]),
    GlFunction(Void, "glGenVertexArraysOES", [(GLsizei, "n"), Out(Array(GLarray, "n"), "arrays")]),
    GlFunction(GLboolean, "glIsVertexArrayOES", [(GLarray, "array")], sideeffects=False),

    # GL_OES_viewport_array
    GlFunction(Void, "glViewportArrayvOES", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLfloat), "count*4"), "v")]),
    GlFunction(Void, "glViewportIndexedfOES", [(GLuint, "index"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "w"), (GLfloat, "h")]),
    GlFunction(Void, "glViewportIndexedfvOES", [(GLuint, "index"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glScissorArrayvOES", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLint), "count*4"), "v")]),
    GlFunction(Void, "glScissorIndexedOES", [(GLuint, "index"), (GLint, "left"), (GLint, "bottom"), (GLsizei, "width"), (GLsizei, "height")]),
    GlFunction(Void, "glScissorIndexedvOES", [(GLuint, "index"), (Array(Const(GLint), 4), "v")]),
    GlFunction(Void, "glDepthRangeArrayfvOES", [(GLuint, "first"), (GLsizei, "count"), (Array(Const(GLfloat), "count*2"), "v")]),
    GlFunction(Void, "glDepthRangeIndexedfOES", [(GLuint, "index"), (GLfloat, "n"), (GLfloat, "f")]),
    GlFunction(Void, "glGetFloati_vOES", [(GLenum, "target"), (GLuint, "index"), Out(Array(GLfloat, "_gl_param_size(target)"), "data")], sideeffects=False),

    # GL_OVR_multiview
    GlFunction(Void, "glFramebufferTextureMultiviewOVR", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLint, "baseViewIndex"), (GLsizei, "numViews")]),
    GlFunction(Void, "glFramebufferTextureMultisampleMultiviewOVR", [(GLenum, "target"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLint, "baseViewIndex"), (GLsizei, "samples"), (GLsizei, "numViews")]),
    GlFunction(Void, "glNamedFramebufferTextureMultiviewOVR", [(GLframebuffer, "framebuffer"), (GLenum, "attachment"), (GLtexture, "texture"), (GLint, "level"), (GLint, "baseViewIndex"), (GLsizei, "numViews")]),
    
    # GL_PGI_misc_hints
    GlFunction(Void, "glHintPGI", [(GLenum, "target"), (GLint, "mode")]),

    # GL_SGIS_detail_texture
    GlFunction(Void, "glDetailTexFuncSGIS", [(GLenum, "target"), (GLsizei, "n"), (Array(Const(GLfloat), "n*2"), "points")]),
    GlFunction(Void, "glGetDetailTexFuncSGIS", [(GLenum, "target"), Out(OpaqueArray(GLfloat, "_glGetDetailTexFuncSGIS_size(target)"), "points")], sideeffects=False),

    # GL_SGIS_fog_function
    GlFunction(Void, "glFogFuncSGIS", [(GLsizei, "n"), (Array(Const(GLfloat), "n*2"), "points")]),
    GlFunction(Void, "glGetFogFuncSGIS", [Out(OpaqueArray(GLfloat, "_glGetFogFuncSGIS_size()"), "points")], sideeffects=False),

    # GL_SGIS_multisample
    GlFunction(Void, "glSampleMaskSGIS", [(GLclampf, "value"), (GLboolean, "invert")]),
    GlFunction(Void, "glSamplePatternSGIS", [(GLenum, "pattern")]),

    # GL_SGIS_pixel_texture
    GlFunction(Void, "glPixelTexGenParameteriSGIS", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glPixelTexGenParameterivSGIS", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glPixelTexGenParameterfSGIS", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glPixelTexGenParameterfvSGIS", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetPixelTexGenParameterivSGIS", [(GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetPixelTexGenParameterfvSGIS", [(GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_SGIS_point_parameters
    GlFunction(Void, "glPointParameterfSGIS", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glPointParameterfvSGIS", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),

    # GL_SGIS_sharpen_texture
    GlFunction(Void, "glSharpenTexFuncSGIS", [(GLenum, "target"), (GLsizei, "n"), (Array(Const(GLfloat), "n*2"), "points")]),
    GlFunction(Void, "glGetSharpenTexFuncSGIS", [(GLenum, "target"), Out(OpaqueArray(GLfloat, "_glGetSharpenTexFuncSGIS_size(target)"), "points")], sideeffects=False),

    # GL_SGIS_texture4D
    GlFunction(Void, "glTexImage4DSGIS", [(GLenum, "target"), (GLint, "level"), (GLenum, "internalformat"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLsizei, "size4d"), (GLint, "border"), (GLenum, "format"), (GLenum, "type"), (OpaqueBlob(Const(GLvoid), "_glTexImage4DSGIS_size(format, type, width, height, depth, size4d)"), "pixels")]),
    GlFunction(Void, "glTexSubImage4DSGIS", [(GLenum, "target"), (GLint, "level"), (GLint, "xoffset"), (GLint, "yoffset"), (GLint, "zoffset"), (GLint, "woffset"), (GLsizei, "width"), (GLsizei, "height"), (GLsizei, "depth"), (GLsizei, "size4d"), (GLenum, "format"), (GLenum, "type"), (OpaqueBlob(Const(GLvoid), "_glTexImage4D_size(format, type, width, height, depth, size4d)"), "pixels")]),

    # GL_SGIS_texture_color_mask
    GlFunction(Void, "glTextureColorMaskSGIS", [(GLboolean, "red"), (GLboolean, "green"), (GLboolean, "blue"), (GLboolean, "alpha")]),

    # GL_SGIS_texture_filter4
    GlFunction(Void, "glGetTexFilterFuncSGIS", [(GLenum, "target"), (GLenum, "filter"), Out(OpaqueArray(GLfloat, "_glGetTexFilterFuncSGIS_size(target, filter)"), "weights")], sideeffects=False),
    GlFunction(Void, "glTexFilterFuncSGIS", [(GLenum, "target"), (GLenum, "filter"), (GLsizei, "n"), (Array(Const(GLfloat), "n"), "weights")]),

    # GL_SGIX_async
    GlFunction(Void, "glAsyncMarkerSGIX", [(GLuint, "marker")]),
    GlFunction(GLint, "glFinishAsyncSGIX", [Out(Pointer(GLuint), "markerp")]),
    GlFunction(GLint, "glPollAsyncSGIX", [Out(Pointer(GLuint), "markerp")]),
    GlFunction(GLuint, "glGenAsyncMarkersSGIX", [(GLsizei, "range")]),
    GlFunction(Void, "glDeleteAsyncMarkersSGIX", [(GLuint, "marker"), (GLsizei, "range")]),
    GlFunction(GLboolean, "glIsAsyncMarkerSGIX", [(GLuint, "marker")], sideeffects=False),

    # GL_SGIX_flush_raster
    GlFunction(Void, "glFlushRasterSGIX", []),

    # GL_SGIX_fragment_lighting
    GlFunction(Void, "glFragmentColorMaterialSGIX", [(GLenum, "face"), (GLenum, "mode")]),
    GlFunction(Void, "glFragmentLightfSGIX", [(GLenum, "light"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glFragmentLightfvSGIX", [(GLenum, "light"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glFragmentLightiSGIX", [(GLenum, "light"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glFragmentLightivSGIX", [(GLenum, "light"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glFragmentLightModelfSGIX", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glFragmentLightModelfvSGIX", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glFragmentLightModeliSGIX", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glFragmentLightModelivSGIX", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glFragmentMaterialfSGIX", [(GLenum, "face"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glFragmentMaterialfvSGIX", [(GLenum, "face"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glFragmentMaterialiSGIX", [(GLenum, "face"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glFragmentMaterialivSGIX", [(GLenum, "face"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glGetFragmentLightfvSGIX", [(GLenum, "light"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetFragmentLightivSGIX", [(GLenum, "light"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetFragmentMaterialfvSGIX", [(GLenum, "face"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetFragmentMaterialivSGIX", [(GLenum, "face"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glLightEnviSGIX", [(GLenum, "pname"), (GLint, "param")]),

    # GL_SGIX_framezoom
    GlFunction(Void, "glFrameZoomSGIX", [(GLint, "factor")]),

    # GL_SGIX_igloo_interface
    GlFunction(Void, "glIglooInterfaceSGIX", [(GLenum, "pname"), (OpaqueBlob(Const(GLvoid), "_glIglooInterfaceSGIX_size(pname)"), "params")]),

    # GL_SGIX_instruments
    GlFunction(GLint, "glGetInstrumentsSGIX", [], sideeffects=False),
    GlFunction(Void, "glInstrumentsBufferSGIX", [(GLsizei, "size"), (OpaqueArray(GLint, "size"), "buffer")]),
    GlFunction(GLint, "glPollInstrumentsSGIX", [Out(Pointer(GLint), "marker_p")]),
    GlFunction(Void, "glReadInstrumentsSGIX", [(GLint, "marker")]),
    GlFunction(Void, "glStartInstrumentsSGIX", []),
    GlFunction(Void, "glStopInstrumentsSGIX", [(GLint, "marker")]),

    # GL_SGIX_list_priority
    GlFunction(Void, "glGetListParameterfvSGIX", [(GLlist, "list"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetListParameterivSGIX", [(GLlist, "list"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glListParameterfSGIX", [(GLlist, "list"), (GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glListParameterfvSGIX", [(GLlist, "list"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glListParameteriSGIX", [(GLlist, "list"), (GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glListParameterivSGIX", [(GLlist, "list"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),

    # GL_SGIX_pixel_texture
    GlFunction(Void, "glPixelTexGenSGIX", [(GLenum, "mode")]),

    # GL_SGIX_polynomial_ffd
    GlFunction(Void, "glDeformationMap3dSGIX", [(GLenum, "target"), (GLdouble, "u1"), (GLdouble, "u2"), (GLint, "ustride"), (GLint, "uorder"), (GLdouble, "v1"), (GLdouble, "v2"), (GLint, "vstride"), (GLint, "vorder"), (GLdouble, "w1"), (GLdouble, "w2"), (GLint, "wstride"), (GLint, "worder"), (OpaqueArray(Const(GLdouble), "_glDeformationMap3dSGIX_size(target, ustride, uorder, vstride, vorder, wstride, worder)"), "points")]),
    GlFunction(Void, "glDeformationMap3fSGIX", [(GLenum, "target"), (GLfloat, "u1"), (GLfloat, "u2"), (GLint, "ustride"), (GLint, "uorder"), (GLfloat, "v1"), (GLfloat, "v2"), (GLint, "vstride"), (GLint, "vorder"), (GLfloat, "w1"), (GLfloat, "w2"), (GLint, "wstride"), (GLint, "worder"), (OpaqueArray(Const(GLfloat), "_glDeformationMap3fSGIX_size(target, ustride, uorder, vstride, vorder, wstride, worder)"), "points")]),
    GlFunction(Void, "glDeformSGIX", [(GLbitfield, "mask")]),
    GlFunction(Void, "glLoadIdentityDeformationMapSGIX", [(GLbitfield, "mask")]),

    # GL_SGIX_reference_plane
    GlFunction(Void, "glReferencePlaneSGIX", [(Array(Const(GLdouble), 4), "equation")]),

    # GL_SGIX_sprite
    GlFunction(Void, "glSpriteParameterfSGIX", [(GLenum, "pname"), (GLfloat, "param")]),
    GlFunction(Void, "glSpriteParameterfvSGIX", [(GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glSpriteParameteriSGIX", [(GLenum, "pname"), (GLint, "param")]),
    GlFunction(Void, "glSpriteParameterivSGIX", [(GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),

    # GL_SGIX_tag_sample_buffer
    GlFunction(Void, "glTagSampleBufferSGIX", []),

    # GL_SGI_color_table
    GlFunction(Void, "glColorTableSGI", [(GLenum, "target"), (GLenum, "internalformat"), (GLsizei, "width"), (GLenum, "format"), (GLenum, "type"), (Blob(Const(GLvoid), "_glColorTable_size(format, type, width)"), "table")]),
    GlFunction(Void, "glColorTableParameterfvSGI", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLfloat), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glColorTableParameterivSGI", [(GLenum, "target"), (GLenum, "pname"), (Array(Const(GLint), "_gl_param_size(pname)"), "params")]),
    GlFunction(Void, "glCopyColorTableSGI", [(GLenum, "target"), (GLenum, "internalformat"), (GLint, "x"), (GLint, "y"), (GLsizei, "width")]),
    GlFunction(Void, "glGetColorTableSGI", [(GLenum, "target"), (GLenum, "format"), (GLenum, "type"), Out(OpaqueBlob(GLvoid, "_glGetColorTableSGI_size(target, format, type)"), "table")], sideeffects=False),
    GlFunction(Void, "glGetColorTableParameterfvSGI", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLfloat, "_gl_param_size(pname)"), "params")], sideeffects=False),
    GlFunction(Void, "glGetColorTableParameterivSGI", [(GLenum, "target"), (GLenum, "pname"), Out(Array(GLint, "_gl_param_size(pname)"), "params")], sideeffects=False),

    # GL_SUNX_constant_data
    GlFunction(Void, "glFinishTextureSUNX", []),

    # GL_SUN_global_alpha
    GlFunction(Void, "glGlobalAlphaFactorbSUN", [(GLbyte, "factor")]),
    GlFunction(Void, "glGlobalAlphaFactorsSUN", [(GLshort, "factor")]),
    GlFunction(Void, "glGlobalAlphaFactoriSUN", [(GLint, "factor")]),
    GlFunction(Void, "glGlobalAlphaFactorfSUN", [(GLfloat, "factor")]),
    GlFunction(Void, "glGlobalAlphaFactordSUN", [(GLdouble, "factor")]),
    GlFunction(Void, "glGlobalAlphaFactorubSUN", [(GLubyte, "factor")]),
    GlFunction(Void, "glGlobalAlphaFactorusSUN", [(GLushort, "factor")]),
    GlFunction(Void, "glGlobalAlphaFactoruiSUN", [(GLuint, "factor")]),

    # GL_SUN_mesh_array
    GlFunction(Void, "glDrawMeshArraysSUN", [(GLenum_mode, "mode"), (GLint, "first"), (GLsizei, "count"), (GLsizei, "width")]),

    # GL_SUN_triangle_list
    GlFunction(Void, "glReplacementCodeuiSUN", [(GLuint, "code")]),
    GlFunction(Void, "glReplacementCodeusSUN", [(GLushort, "code")]),
    GlFunction(Void, "glReplacementCodeubSUN", [(GLubyte, "code")]),
    GlFunction(Void, "glReplacementCodeuivSUN", [(OpaqueArray(Const(GLuint), "_glReplacementCodeuivSUN_size()"), "code")]),
    GlFunction(Void, "glReplacementCodeusvSUN", [(OpaqueArray(Const(GLushort), "_glReplacementCodeusvSUN_size()"), "code")]),
    GlFunction(Void, "glReplacementCodeubvSUN", [(OpaqueArray(Const(GLubyte), "_glReplacementCodeubvSUN_size()"), "code")]),
    GlFunction(Void, "glReplacementCodePointerSUN", [(GLenum, "type"), (GLsizei, "stride"), (OpaquePointer(GLpointerConst), "pointer")]),

    # GL_SUN_vertex
    GlFunction(Void, "glColor4ubVertex2fSUN", [(GLubyte, "r"), (GLubyte, "g"), (GLubyte, "b"), (GLubyte, "a"), (GLfloat, "x"), (GLfloat, "y")]),
    GlFunction(Void, "glColor4ubVertex2fvSUN", [(Array(Const(GLubyte), 4), "c"), (Array(Const(GLfloat), 2), "v")]),
    GlFunction(Void, "glColor4ubVertex3fSUN", [(GLubyte, "r"), (GLubyte, "g"), (GLubyte, "b"), (GLubyte, "a"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glColor4ubVertex3fvSUN", [(Array(Const(GLubyte), 4), "c"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glColor3fVertex3fSUN", [(GLfloat, "r"), (GLfloat, "g"), (GLfloat, "b"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glColor3fVertex3fvSUN", [(Array(Const(GLfloat), 3), "c"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glNormal3fVertex3fSUN", [(GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glNormal3fVertex3fvSUN", [(Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glColor4fNormal3fVertex3fSUN", [(GLfloat, "r"), (GLfloat, "g"), (GLfloat, "b"), (GLfloat, "a"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glColor4fNormal3fVertex3fvSUN", [(Array(Const(GLfloat), 4), "c"), (Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glTexCoord2fVertex3fSUN", [(GLfloat, "s"), (GLfloat, "t"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glTexCoord2fVertex3fvSUN", [(Array(Const(GLfloat), 2), "tc"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glTexCoord4fVertex4fSUN", [(GLfloat, "s"), (GLfloat, "t"), (GLfloat, "p"), (GLfloat, "q"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glTexCoord4fVertex4fvSUN", [(Array(Const(GLfloat), 4), "tc"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glTexCoord2fColor4ubVertex3fSUN", [(GLfloat, "s"), (GLfloat, "t"), (GLubyte, "r"), (GLubyte, "g"), (GLubyte, "b"), (GLubyte, "a"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glTexCoord2fColor4ubVertex3fvSUN", [(Array(Const(GLfloat), 2), "tc"), (Array(Const(GLubyte), 4), "c"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glTexCoord2fColor3fVertex3fSUN", [(GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r"), (GLfloat, "g"), (GLfloat, "b"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glTexCoord2fColor3fVertex3fvSUN", [(Array(Const(GLfloat), 2), "tc"), (Array(Const(GLfloat), 3), "c"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glTexCoord2fNormal3fVertex3fSUN", [(GLfloat, "s"), (GLfloat, "t"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glTexCoord2fNormal3fVertex3fvSUN", [(Array(Const(GLfloat), 2), "tc"), (Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glTexCoord2fColor4fNormal3fVertex3fSUN", [(GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r"), (GLfloat, "g"), (GLfloat, "b"), (GLfloat, "a"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glTexCoord2fColor4fNormal3fVertex3fvSUN", [(Array(Const(GLfloat), 2), "tc"), (Array(Const(GLfloat), 4), "c"), (Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glTexCoord4fColor4fNormal3fVertex4fSUN", [(GLfloat, "s"), (GLfloat, "t"), (GLfloat, "p"), (GLfloat, "q"), (GLfloat, "r"), (GLfloat, "g"), (GLfloat, "b"), (GLfloat, "a"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z"), (GLfloat, "w")]),
    GlFunction(Void, "glTexCoord4fColor4fNormal3fVertex4fvSUN", [(Array(Const(GLfloat), 4), "tc"), (Array(Const(GLfloat), 4), "c"), (Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 4), "v")]),
    GlFunction(Void, "glReplacementCodeuiVertex3fSUN", [(GLuint, "rc"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glReplacementCodeuiVertex3fvSUN", [(Pointer(Const(GLuint)), "rc"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glReplacementCodeuiColor4ubVertex3fSUN", [(GLuint, "rc"), (GLubyte, "r"), (GLubyte, "g"), (GLubyte, "b"), (GLubyte, "a"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glReplacementCodeuiColor4ubVertex3fvSUN", [(Pointer(Const(GLuint)), "rc"), (Array(Const(GLubyte), 4), "c"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glReplacementCodeuiColor3fVertex3fSUN", [(GLuint, "rc"), (GLfloat, "r"), (GLfloat, "g"), (GLfloat, "b"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glReplacementCodeuiColor3fVertex3fvSUN", [(Pointer(Const(GLuint)), "rc"), (Array(Const(GLfloat), 3), "c"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glReplacementCodeuiNormal3fVertex3fSUN", [(GLuint, "rc"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glReplacementCodeuiNormal3fVertex3fvSUN", [(Pointer(Const(GLuint)), "rc"), (Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glReplacementCodeuiColor4fNormal3fVertex3fSUN", [(GLuint, "rc"), (GLfloat, "r"), (GLfloat, "g"), (GLfloat, "b"), (GLfloat, "a"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glReplacementCodeuiColor4fNormal3fVertex3fvSUN", [(Pointer(Const(GLuint)), "rc"), (Array(Const(GLfloat), 4), "c"), (Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glReplacementCodeuiTexCoord2fVertex3fSUN", [(GLuint, "rc"), (GLfloat, "s"), (GLfloat, "t"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glReplacementCodeuiTexCoord2fVertex3fvSUN", [(Pointer(Const(GLuint)), "rc"), (Array(Const(GLfloat), 2), "tc"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glReplacementCodeuiTexCoord2fNormal3fVertex3fSUN", [(GLuint, "rc"), (GLfloat, "s"), (GLfloat, "t"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glReplacementCodeuiTexCoord2fNormal3fVertex3fvSUN", [(Pointer(Const(GLuint)), "rc"), (Array(Const(GLfloat), 2), "tc"), (Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 3), "v")]),
    GlFunction(Void, "glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fSUN", [(GLuint, "rc"), (GLfloat, "s"), (GLfloat, "t"), (GLfloat, "r"), (GLfloat, "g"), (GLfloat, "b"), (GLfloat, "a"), (GLfloat, "nx"), (GLfloat, "ny"), (GLfloat, "nz"), (GLfloat, "x"), (GLfloat, "y"), (GLfloat, "z")]),
    GlFunction(Void, "glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fvSUN", [(Pointer(Const(GLuint)), "rc"), (Array(Const(GLfloat), 2), "tc"), (Array(Const(GLfloat), 4), "c"), (Array(Const(GLfloat), 3), "n"), (Array(Const(GLfloat), 3), "v")]),

    # GL_WIN_swap_hint
    GlFunction(Void, "glAddSwapHintRectWIN", [(GLint, "x"), (GLint, "y"), (GLsizei, "width"), (GLsizei, "height")]),

])
