## Install BlueROV2 Repository
Setup Github connection to the repository

`git clone https://github.com/AAU-Underwater-Robot-Lab/ROS_BlueROV2.git ROS_BlueROV2`

`cd ROS_BlueROV2`

`git pull`

`catkin build`

`source ~/ROS_BlueROV2/devel/setup.sh`

`source ~/ROS_BlueROV2/.bash_ros`

`installrosdep`

`git checkout -b ＜new-branch＞`

**_Note: Use your projectgroup-name as the new branch name eg. OES1-F21:_
 `git checkout -b OES1-F21`**

(Once setup, groupmembers should use  `git checkout <new-branch>`, where `<new-branch>` is once again your projectgroup-name)

:exclamation: DO NOT MERGE WITH THE MAIN BRANCH WITHOUT TALKING WITH STAFF FIRST

The repository is now setup and ready to use.

Next thing is to setup _src/bluerov2_brinup/launch/bluerov2_bringup.launch_ for your project.