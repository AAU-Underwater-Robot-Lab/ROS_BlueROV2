#!/bin/bash
export ROS_MASTER_URI=http://192.168.2.10:11311
export ROS_IP=$(hostname -I | grep -o '192.168.2....' | tr -d [:blank:])
roslaunch bluerov2_teleop joy_velocity_direct.launch
