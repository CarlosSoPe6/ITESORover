cmake_minimum_required(VERSION 2.8.3)
project(rover_systems)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
)

catkin_package()

install(PROGRAMS
    scripts/WheelsControler.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(
  DIRECTORY scripts/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/scripts
)