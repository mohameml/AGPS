cmake_minimum_required(VERSION 3.10)
project(OptionPricing)

# Release or Debug
if (NOT CMAKE_BUILD_TYPE)
    message(STATUS "Setting build type to 'Debug' as none was specified.")
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "Choose the type of build." FORCE)
endif ()


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Ajoute le flag pour le debug si nécessaire
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic")

# Détection de la bibliothèque PNL
# Find Pnl
find_package(Pnl REQUIRED)
set(LIBS ${LIBS} ${PNL_LIBRARIES})
include_directories(${PNL_INCLUDE_DIRS})
if(${CMAKE_BUILD_TYPE} STREQUAL "Release")
    add_definitions(-DPNL_RANGE_CHECK_OFF)
endif()

# Ajout des fichiers sources
add_executable(option_pricing main.cpp Option.cpp InterestRateModel.cpp TimeGrid.cpp)

# Inclusion des répertoires d'en-têtes
target_include_directories(option_pricing PRIVATE ${PNL_INCLUDE_DIRS})

# Liaison avec la bibliothèque PNL
target_link_libraries(option_pricing ${PNL_LIBRARIES})
