project(look_and_say_tests)

#
# Dependency
#
hunter_add_package(GTest)
find_package(GTest CONFIG REQUIRED)


#
# Sources
#
set(SOURCES
        main.cpp
        look_and_say_tests.cpp
        )

#
# Application
#
add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} GTest::gtest look_and_say)
