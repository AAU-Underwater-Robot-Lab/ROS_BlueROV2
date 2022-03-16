[Go back](../README.md)

# Start Thruster Manager

## <b>Description</b>

This package has yet to be described... Feel free to put a description here.

## Build Instructions/Requirements

* Requires the folder *config/<model_name>/* containing *TAM.yaml* and *thruster_manager.yaml*. 

**Both BlueROV2 and BlueROV2 Heavy configuration is prebuild for this package. However the might have to be updated to apply for your ROV.**

## Topics:
### Published:

* `thrusters/i/input`: Publishes `uuv_gazebo_ros_plugins_msgs/FloatStamped` with the input for thruster i, which is used by the Arduino to generate a PWM signal to the thrusters Electrical Speed Controller (ESC).

### Subscribed:
* `thruster_manager/input`: Subscribes `geometry_msgs/Wrench` which is the force in Newton and torque in Newton meter.

* `thruster_manager/input_stamped`: Subscribes `geometry_msgs/WrenchStamped` which is the force in Newton and torque in Newton meter including a header stamp.

**Only one of the subcribed topics should be used.**

## Parameters/Reconfigs:
*  `model_name`: The robot used (there must be a folder within config with the same name):
    * **bluerov2 (Default)**
    * bluerov2_heavy
* `ns_name`: Name of the name space, this is the prefix for all topics and nodes. The name space is normally bluerov2.

## Messeages:
* `ThrusterCmd`:
    * std_msgs/Header header
        * uint32 seq
        * time stamp
        * string frame_id
    * float64 data


## Launch Information

Launch using

```
<include file="$(find bluerov2_thruster)/launch/start_thruster_manager.launch">
  <arg name="model_name" value="bluerov2"/>
  <arg name="ns_name" value="bluerov2"/>
</include>
```

in a launch file or using

`roslaunch bluerov2_thruster start_thruster_manager.launch`

## Troubleshooting

No known issues...

If you find an issue, please report it in [Teams](https://teams.microsoft.com/l/entity/com.microsoft.teamspace.tab.wiki/tab::954da529-209e-4c94-9cec-638758d828a2?context=%7B%22subEntityId%22%3A%22%7B%5C%22pageId%5C%22%3A3%2C%5C%22sectionId%5C%22%3A4%2C%5C%22origin%5C%22%3A2%7D%22%2C%22channelId%22%3A%2219%3Ab26708e74f304c11b9a9aa93bff67cda%40thread.tacv2%22%7D&tenantId=f5dbba49-ce06-496f-ac3e-0cf14361d934).

## Contributors 

* Current maintaner: FirstName LastName (contact:email@aau.dk)

## Helpful Resources

* No Usefull links.<!-- http://www.google.com -->
