## Install BlueROV2 Repository
Setup Github connection to the repository

Fork this repository to your own github account, by pressing **Fork** in the upper right corner.

Open your terminal and run the following code:

`git clone https://github.com/<username>/ROS_BlueROV2.git catkin_ws`

`cd catkin_ws`

`git pull`

`sudo apt-get install python3-catkin-tools`

`catkin build`

`echo "source ~/catkin_ws/devel/setup.sh" >> ~/.bashrc`

`echo "source ~/catkin_ws/.bash_ros" >> ~/.bashrc`

`source ~/.bashrc`

`installrosdep`

The repository is now setup and ready to use.

Next thing is to test all individual rospackages of interest, and after that setup _src/bluerov2_brinup/launch/bluerov2_bringup.launch_ for your project.
