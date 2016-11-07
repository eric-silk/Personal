cmake_minimum_required(VERSION 2.6)

project(main)

file(GLOB_RECURSE SOURCES src/*.cpp)

add_executable(main ${SOURCES})
