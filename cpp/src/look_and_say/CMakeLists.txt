project(look_and_say)

#
# Sources
#
set(SOURCES
        common/look_and_say.cpp
        cosmo/look_and_say.cpp
        )

#
# Library
#
add_library(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PUBLIC .)
