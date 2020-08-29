cmake_minimum_required(VERSION 3.4.1)

#
# Flags
#
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic -Werror")

#
# Sources
#
add_subdirectory(src)
