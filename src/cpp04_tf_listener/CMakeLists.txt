cmake_minimum_required(VERSION 3.8)
project(cpp04_tf_listener)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(message_filters REQUIRED)

add_executable(demo01_tf_listener src/demo01_tf_listener.cpp)
add_executable(demo02_msg_filter src/demo02_msg_filter.cpp)

target_include_directories(demo01_tf_listener PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(demo01_tf_listener PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  demo01_tf_listener
  "rclcpp"
  "tf2"
  "tf2_ros"
  "geometry_msgs"
)
ament_target_dependencies(
        demo02_msg_filter
        "rclcpp"
        "tf2"
        "tf2_ros"
        "geometry_msgs"
        "tf2_geometry_msgs"
        "message_filters"
)
install(TARGETS demo01_tf_listener demo02_msg_filter
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
