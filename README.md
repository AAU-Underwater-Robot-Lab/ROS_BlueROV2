# Underwater Robots ROS - Aalborg University
Software Repo for Underwater Robots using Ros

If you havn't installed ROS on your local pc, a guide can found [here](Install_ROS.md).

## Sensors Found in this GitHub:
[WaterLinked DVL](src/aau_waterlinked_dvl/README.md)

[WaterLinked SBL](src/aau_waterlinked_dvl/README.md)

# Startup of robot
Robot contains Jetson board runnning Ubuntu

## Robot roslaunch
SSH to robot Jetson by:
`ssh 192.168.2.10 -l nvidia`

Run command
`roslaunch bluerov2_bringup bluerov2_bringup.launch`

## Joystick teleop 
Open terminal on teleoperation PC (eg. laptop)

Run command
`rosrun bluerov2_teleop bluerov2_teleop.sh`

**This command will set the ROS_IP and ROS_MASTER_URI enviroment variables, which will affect the ability to run local rosmaster and nodes!**

# Setting up static IP on Topside computer
The topside computer must have a static IP:
192.168.2.50/90

When running the command
`rosrun bluerov2_teleop bluerov2_teleop.sh`, your static IP is auto detected and set.

If you want to access rostopics etc. run `source ~/catkin_ws/Topside.sh`

**This command will set the ROS_IP and ROS_MASTER_URI enviroment variables, which will affect the ability to run local rosmaster and nodes!**

# Alias Commands
Often used commands for BlueROV2 is made to aliases, to make them easy to call and remember.

## Setup aliases
run `echo 'source ~/catkin_ws/.bash_ros' >> ~/.bashrc`

**This command only has to be called once, as it will add .bash_ros to .bashrc, which is called on every terminal startup!**

Restart terminal or run `source ~/bashrc`

## Alias List

The Alias list is divided into two categories <b>User</b> and <b>Developer</b>.

### User Commands:
| `Command` | Description |
| :------------ | -----------: |
| `launchbluerov2` | Robot Roslaunch |
| `launchtopside` | Launches Joystick |

### Developber Commands
| `Command` | Description |
| :------------ | -----------: |
| `rostopside` | Set the ROS_IP and ROS_MASTER_URI enviroment variables for communication with the robot |
| `roslocal` | Unset the ROS_IP and ROS_MASTER_URI enviroment variables to be able to use local rosmaster |
| `sshbluerov2` | SSH into the Jetson on the robot|
| `simjoystick` | Launches Link between Joystick and Simulink |
| `getrosbags <DISTINATION/FOLDER/LOCATION>` | Get rosbags from the robot using scp to a desired location |
