# <b>Underwater Robots ROS - Aalborg University</b>
Software Repo for Underwater Robots using Ros

If you havn't installed ROS on your local pc, a guide can found [here](Doc/Install_ROS.md).

## <b>Get Repository</b>
[Fork Repository](Doc/Get_Repository.md)

## <b>Share wireless internet through ethernet</b>
[Setup wireless internet sharing](Doc/SetupInternetSharing.md)

## <b>Sensors Found in this Repository:</b>
[WaterLinked DVL](src/aau_waterlinked_dvl/README.md) - package: aau_waterlinked_dvl

[WaterLinked SBL](src/aau_waterlinked_sbl/README.md) - package: aau_waterlinked_sbl

[MS5837 Pressure Sensor](src/bluerov2_ms5837/README.md) - package: bluerov2_ms5837

SydDynamic TM200 (No documentation yet) - package: bluerov2_tm200

## <b>Thruster Setup:</b>
[Configure Arduino Board](Doc/Config_Arduino.md) - package: bluerov2_arduino

[Configure Thruster Manager](src/bluerov2_thruster/README.md) - package: bluerov2_thruster

# <b>Startup of robot</b>
Robot contains Jetson board runnning Ubuntu

## <b>Robot roslaunch</b>
SSH to robot Jetson by:

`ssh 192.168.3.10 -l jetson`

Using password: `jetson`

Also useable is SSH:
`ssh jetson@192.168.3.10`

**If nano is not the username on the Jetson board, it must be replaced with the actual username!** 

Run command

`roslaunch bluerov2_bringup bluerov2_bringup.launch`

## <b>Joystick teleop</b> 
Open terminal on teleoperation PC (eg. laptop)

Run command

`rosrun bluerov2_teleop bluerov2_teleop.sh`

**This command will set the ROS_IP and ROS_MASTER_URI enviroment variables, which will affect the ability to run local rosmaster and nodes!**

# <b>Setting up static IP on Topside computer</b>
The topside computer must have a static IP:
192.168.2.50/90

When running the command `rosrun bluerov2_teleop bluerov2_teleop.sh`, your static IP is auto detected and set.

If you want to access rostopics etc. run

`source ~/catkin_ws/Topside.sh`

**This command will set the ROS_IP and ROS_MASTER_URI enviroment variables, which will affect the ability to run local rosmaster and nodes!**

# <b>Alias Commands</b>
Often used commands for BlueROV2 is made to aliases, to make them easy to call and remember.

## <b>Setup aliases</b>
run

`echo 'source ~/catkin_ws/.bash_ros' >> ~/.bashrc`

**This command only has to be called once, as it will add .bash_ros to .bashrc, which is called on every terminal startup!**

Restart terminal or run

`source ~/bashrc`

## <b>Alias List</b>

The Alias list is divided into two categories <b>User</b> and <b>Developer</b>.

### <b>User Commands:</b>
| `Command` | Description |
| :------------ | -----------: |
| ~~`launchbluerov2`~~ | Robot Roslaunch |
| ~~`launchtopside`~~ | Launches Joystick |

### <b>Developber Commands</b>
| `Command` | Description |
| :------------ | -----------: |
| `rostopside` | Set the ROS_IP and ROS_MASTER_URI enviroment variables for communication with the robot |
| `roslocal` | Unset the ROS_IP and ROS_MASTER_URI enviroment variables to be able to use local rosmaster |
| ~~`sshbluerov2`~~ | SSH into the Jetson on the robot|
| ~~`simjoystick`~~ | Launches Link between Joystick and Simulink |
| ~~`getrosbags <DISTINATION/FOLDER/LOCATION>`~~ | Get rosbags from the robot using scp to a desired location |
