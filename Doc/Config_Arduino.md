[Go back](../README.md)

# <b>Configure Arduino with thruster script</b>

## <b>Requriements:</b>
Laptop with following:
* Ubuntu 18.04.6 LTS
* ROS-Melodic - [How to install](Install_ROS.md)
* [BlueROV2 repository](https://github.com/AAU-Underwater-Robot-Lab/ROS_BlueROV2)

## <b>Install ROS libraries:</b>

`sudo apt-get install ros-melodic-rosserial-arduino`

`sudo apt-get install ros-melodic-rosserial`

## <b>Setup Arduino IDE</b>
Install the Arduino IDE on you PC, you can either get it from Ubuntu Software or download it here: [Arduino Software](https://www.arduino.cc/en/software)

When the <b>Arduino IDE</b> is fully installed, find the path of the Arduino library and run the following commands:

`cd ~/catkin_ws`

`rosrun rosserial_arduino make_libraries.py <ARDUINO_LIBRARY_PATH>` (ex. ~/Arduino/libraries)

## <b>Setup Arduino Board</b>
Open the <b>Arduino IDE</b>

Choose one of the 2 different Step 1, depending on thruster configuration.

### <b>Step 1: BlueROV2 standard configuration:</b>
Open file:

~/catkin_ws/src/bluerov2_arduino/src/ardu_due_thruster/ardu_due_thruster.ino

Upload to board

### <b>Step 1: BlueROV2 heavy configuration:</b>
Open file:

~/catkin_ws/src/bluerov2_arduino/src/ardu_heavy_thruster/ardu_heavy_thruster.ino

Upload to board

### <b>Step 2:</b>
Connect signal pins from ESCs to Arduino board.

Connect Arduino board to Jetson board.

Done.
