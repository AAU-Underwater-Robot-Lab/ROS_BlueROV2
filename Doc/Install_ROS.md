[Go back](../README.md)

# <b>Install ROS-Melodic</b>
Required Operation System:

* Desktop: Ubuntu 18.04.6 LTS [Download Here](https://releases.ubuntu.com/18.04/)

* Jetson: JetPack 4.6 [Download Here](https://developer.nvidia.com/jetson-nano-sd-card-image)

## <b>Setup your sources.list</b>
`sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`

## <b>Set up your keys</b>
`sudo apt install curl # if you haven't already installed curl`

`curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -`

## <b>Installation</b>
`sudo apt update`

`sudo apt install ros-melodic-desktop-full`

**Troubleshooting: If you get the error: `E: Unable to locate package ros-melodic-desktop-full`, check your Ubuntu Version, it MUST be Ubuntu 18.04 as newer versions does not support ros-melodic-desktop-full version!**

## <b>Environment setup</b>
It's convenient if the ROS environment variables are automatically added to your bash session every time a new shell is launched:

`echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc`

`source ~/.bashrc`


If you have more than one ROS distribution installed, ~/.bashrc must only source the setup.bash for the version you are currently using.
If you just want to change the environment of your current shell, instead of the above you can type:

`source /opt/ros/melodic/setup.bash`

## <b>Dependencies for building packages</b>
Up to now you have installed what you need to run the core ROS packages. To create and manage your own ROS workspaces, there are various tools and requirements that are distributed separately. For example, rosinstall is a frequently used command-line tool that enables you to easily download many source trees for ROS packages with one command.

To install this tool and other dependencies for building ROS packages, run: 

`sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential`

## <b>Initialize rosdep</b>
`sudo apt install python-rosdep`

With the following, you can initialize rosdep. 

`sudo rosdep init`

`rosdep update`

Full Guide can be found [here](http://wiki.ros.org/melodic/Installation/Ubuntu "ROS melodic")

## <b>Install UUV</b>

Beside ROS Melodic, you will also need to install [Unmanned Underwater Vehicle Simulator](https://uuvsimulator.github.io/)
Once ROS is installed, it can be installed by running the following code:

`sudo apt install ros-melodic-uuv-simulator`

<sub>Author: Fredrik Fogh Sørensen [ffso@energy.aau.dk](mailto:ffso@energy.aau.dk)</sub>
