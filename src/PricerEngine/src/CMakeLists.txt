cmake_minimum_required(VERSION 3.15)

project(PricerEngine C CXX)

# Release or Debug
if (NOT CMAKE_BUILD_TYPE)
    message(STATUS "Setting build type to 'Debug' as none was specified.")
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "Choose the type of build." FORCE)
endif ()

list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")


# Find Protobuf installation
option(protobuf_MODULE_COMPATIBLE TRUE)
find_package(Protobuf CONFIG REQUIRED)

# ligne ajouée
set(PROTOBUF_INCLUDE_DIR "/home/mohameml/.local/include") # changer ceci avec le chemin vers protoc runtime 
include_directories(${PROTOBUF_INCLUDE_DIR})
message(STATUS "Using protobuf ${Protobuf_VERSION}")


set(_PROTOBUF_LIBPROTOBUF protobuf::libprotobuf)
set(_REFLECTION gRPC::grpc++_reflection)
set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)

# Find gRPC installation
# Looks for gRPCConfig.cmake file installed by gRPC's cmake installation.
find_package(gRPC CONFIG REQUIRED)
message(STATUS "Using gRPC ${gRPC_VERSION}")

set(_GRPC_GRPCPP gRPC::grpc++)
set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)

# Proto file
get_filename_component(pricer_proto "pricing.proto" ABSOLUTE)
get_filename_component(pricer_proto_path "${pricer_proto}" PATH)

# Generated sources
set(pricer_proto_srcs "${CMAKE_CURRENT_BINARY_DIR}/pricing.pb.cc")
set(pricer_proto_hdrs "${CMAKE_CURRENT_BINARY_DIR}/pricing.pb.h")
set(pricer_grpc_srcs "${CMAKE_CURRENT_BINARY_DIR}/pricing.grpc.pb.cc")
set(pricer_grpc_hdrs "${CMAKE_CURRENT_BINARY_DIR}/pricing.grpc.pb.h")
add_custom_command(
    OUTPUT "${pricer_proto_srcs}" "${pricer_proto_hdrs}" "${pricer_grpc_srcs}" "${pricer_grpc_hdrs}"
    COMMAND ${_PROTOBUF_PROTOC}
    ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}"
    --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
    -I "${pricer_proto_path}"
    --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
    "${pricer_proto}"
    DEPENDS "${pricer_proto}"
)

# Find Pnl
find_package(Pnl REQUIRED)
set(LIBS ${LIBS} ${PNL_LIBRARIES})
include_directories(${PNL_INCLUDE_DIRS})
if(${CMAKE_BUILD_TYPE} STREQUAL "Release")
    add_definitions(-DPNL_RANGE_CHECK_OFF)
endif()

# Find nlohmann_json to parse json files
# Add nlohmann_json::nlohmann_json to target_link_libraries

# find_package(nlohmann_json REQUIRED)

# Include generated *.pb.h files
include_directories("${CMAKE_CURRENT_BINARY_DIR}")

# pricer_grpc_proto
add_library(pricer_grpc_proto
    ${pricer_grpc_srcs}
    ${pricer_grpc_hdrs}
    ${pricer_proto_srcs}
    ${pricer_proto_hdrs}
)
target_link_libraries(pricer_grpc_proto
    ${_REFLECTION}
    ${_GRPC_GRPCPP}
    ${_PROTOBUF_LIBPROTOBUF}
)


# my_lib  :
file(GLOB SRC_FILES ./*.cpp)
add_library(my_lib ${SRC_FILES})


add_executable(pricing_server pricing_server.cpp )
target_link_libraries(pricing_server
    my_lib
    pricer_grpc_proto
    ${_REFLECTION}
    ${_GRPC_GRPCPP}
    ${_PROTOBUF_LIBPROTOBUF}
    ${PNL_LIBRARIES}
)
pnl_add_postbuild(pricing_server)


# Ajout d'un exécutable pour tester GlobalModel
add_executable(test_global_model test.cpp)
target_link_libraries(test_global_model
    my_lib
    pricer_grpc_proto
    ${_REFLECTION}
    ${_GRPC_GRPCPP}
    ${_PROTOBUF_LIBPROTOBUF}
    ${PNL_LIBRARIES}
)
pnl_add_postbuild(test_global_model)
























# Ajout d'un exécutable pour tester le pricer
# add_executable(test_pricer test_pricer.cpp pricer.cpp json_reader.cpp BlackScholesModel.cpp ConditionalBasketOption.cpp ConditionalMaxOption.cpp Option.cpp)
# target_link_libraries(test_pricer
#     ${PNL_LIBRARIES}
#     nlohmann_json::nlohmann_json
# )
# pnl_add_postbuild(test_pricer)


# add_executable(test_json_reader json_reader.cpp test_json_reader.cpp)
# target_link_libraries(test_json_reader
#     ${PNL_LIBRARIES}
#     nlohmann_json::nlohmann_json
# )
# pnl_add_postbuild(test_json_reader)



















# cmake_minimum_required(VERSION 3.10)
# project(OptionPricing)

# # Release or Debug
# if (NOT CMAKE_BUILD_TYPE)
#     message(STATUS "Setting build type to 'Debug' as none was specified.")
#     set(CMAKE_BUILD_TYPE Debug CACHE STRING "Choose the type of build." FORCE)
# endif ()


# set(CMAKE_CXX_STANDARD 17)
# set(CMAKE_CXX_STANDARD_REQUIRED True)

# # Ajoute le flag pour le debug si nécessaire
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic")

# # Détection de la bibliothèque PNL
# # Find Pnl
# find_package(Pnl REQUIRED)
# set(LIBS ${LIBS} ${PNL_LIBRARIES})
# include_directories(${PNL_INCLUDE_DIRS})
# if(${CMAKE_BUILD_TYPE} STREQUAL "Release")
#     add_definitions(-DPNL_RANGE_CHECK_OFF)
# endif()

# # Ajout des fichiers sources
# add_executable(option_pricing main.cpp Option.cpp InterestRateModel.cpp TimeGrid.cpp)

# # Inclusion des répertoires d'en-têtes
# target_include_directories(option_pricing PRIVATE ${PNL_INCLUDE_DIRS})

# # Liaison avec la bibliothèque PNL
# target_link_libraries(option_pricing ${PNL_LIBRARIES})
