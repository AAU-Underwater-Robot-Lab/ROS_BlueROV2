#!/usr/bin/env python

import rospy
from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped

def pwm_view(data,pub):
	msg = FloatStamped()	
	msg.header.stamp = rospy.Time.now()
	msg.data = 1500+400*data.data
	pub.publish(msg)

if __name__ == '__main__':
	rospy.init_node('pwm_viewer',anonymous=True)
	model_name = rospy.get_param("~model_name","bluerov2")
	pubInput0 = rospy.Publisher('bluerov2/thrusters/0/pwm',FloatStamped,queue_size=10)
	pubInput1 = rospy.Publisher('bluerov2/thrusters/1/pwm',FloatStamped,queue_size=10)
	pubInput2 = rospy.Publisher('bluerov2/thrusters/2/pwm',FloatStamped,queue_size=10)
	pubInput3 = rospy.Publisher('bluerov2/thrusters/3/pwm',FloatStamped,queue_size=10)
	pubInput4 = rospy.Publisher('bluerov2/thrusters/4/pwm',FloatStamped,queue_size=10)
	pubInput5 = rospy.Publisher('bluerov2/thrusters/5/pwm',FloatStamped,queue_size=10)
	if(model_name == "bluerov2_heavy"):
		pubInput6 = rospy.Publisher('bluerov2/thrusters/6/pwm',FloatStamped,queue_size=10)
		pubInput7 = rospy.Publisher('bluerov2/thrusters/7/pwm',FloatStamped,queue_size=10)

	rospy.Subscriber('bluerov2/thrusters/0/input',FloatStamped,pwm_view,pubInput0)
	rospy.Subscriber('bluerov2/thrusters/1/input',FloatStamped,pwm_view,pubInput1)
	rospy.Subscriber('bluerov2/thrusters/2/input',FloatStamped,pwm_view,pubInput2)
	rospy.Subscriber('bluerov2/thrusters/3/input',FloatStamped,pwm_view,pubInput3)
	rospy.Subscriber('bluerov2/thrusters/4/input',FloatStamped,pwm_view,pubInput4)
	rospy.Subscriber('bluerov2/thrusters/5/input',FloatStamped,pwm_view,pubInput5)
	if(model_name == "bluerov2_heavy"):
		rospy.Subscriber('bluerov2/thrusters/6/input',FloatStamped,pwm_view,pubInput6)
		rospy.Subscriber('bluerov2/thrusters/7/input',FloatStamped,pwm_view,pubInput7)
	rospy.spin()
