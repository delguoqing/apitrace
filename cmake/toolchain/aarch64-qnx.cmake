set (CMAKE_SYSTEM_NAME QNX)
set (CMAKE_SYSTEM_PROCESSOR aarch64)

set (TARGET_ARCH "aarch64le")

set (CMAKE_C_COMPILER "$ENV{QNX_HOST}/usr/bin/ntoaarch64-gcc")
set (CMAKE_CXX_COMPILER "$ENV{QNX_HOST}/usr/bin/ntoaarch64-g++")

set (CMAKE_FIND_ROOT_PATH "$ENV{QNX_TARGET}/${TARGET_ARCH}")

set (CMAKE_CROSSCOMPILING TRUE)

# Search for programs in the build host directories.
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM ONLY)
# Search for libraries and headers in the target directories.
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)