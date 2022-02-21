## Install BlueROV2 Repository
Setup Github connection to the repository

`git clone https://github.com/EsbenAAUEnergy/ROS_BlueROV2.git catkin_ws`

`cd catkin_ws`

`git pull`

`sudo apt-get install python3-catkin-tools`

`catkin build`

`source ~/catkin_ws/devel/setup.sh`

`source ~/catkin_ws/.bash_ros`

`installrosdep`

The repository is now setup and ready to use.

Next thing is to setup _src/bluerov2_brinup/launch/bluerov2_bringup.launch_ for your project.
