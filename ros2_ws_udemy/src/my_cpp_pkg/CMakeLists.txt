cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED) # Added dependency

add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(robot_news_station src/robot_news_station.cpp) # New executable
ament_target_dependencies(robot_news_station rclcpp example_interfaces) # Added dependency

add_executable(smartphone src/smartphone.cpp) # New executable
ament_target_dependencies(smartphone rclcpp example_interfaces) # Added dependency

install(TARGETS
  cpp_node
  robot_news_station # New executable
  smartphone # New executable
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
