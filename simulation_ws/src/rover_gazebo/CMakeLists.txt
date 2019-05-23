cmake_minimum_required(VERSION 2.8.3)
project(rover_gazebo)

find_package(catkin REQUIRED COMPONENTS
  gazebo
  gazebo_plugins
  gazebo_ros
  gazebo_ros_control
  tf
  urdf
)

catkin_package()

install(
  DIRECTORY models
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(
  DIRECTORY worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(
  DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
