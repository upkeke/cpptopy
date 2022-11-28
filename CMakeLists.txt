cmake_minimum_required(VERSION 3.10)
project(pydll)

set(CMAKE_CXX_STANDARD 11)
set(EXCAPPLIB 
    lib1.h
    lib1.cpp
)

add_library(pydll SHARED ${EXCAPPLIB})