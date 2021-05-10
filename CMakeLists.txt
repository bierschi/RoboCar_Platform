cmake_minimum_required(VERSION 3.10.2)
project(RoboCar_Platform VERSION "1.0")

# set c++11 as standard
set(CMAKE_CXX_STANDARD 11)

# set binary output path
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})

# add the header files
include_directories(include)

# add the source files
file(GLOB_RECURSE SOURCE_FILES "${CMAKE_SOURCE_DIR}/src/*.cpp")

add_executable(robocar ${SOURCE_FILES})