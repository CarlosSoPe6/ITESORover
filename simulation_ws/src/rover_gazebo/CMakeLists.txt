cmake_minimum_required(VERSION 2.8.3)
project(rover_gazebo)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  urdf
)

catkin_package()

install(
  DIRECTORY models/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/models
)

install(
  DIRECTORY worlds/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/worlds
)

install(
  DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
