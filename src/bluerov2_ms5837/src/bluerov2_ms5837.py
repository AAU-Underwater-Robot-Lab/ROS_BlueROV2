#!/usr/bin/env python

import ms5837_driver as ms5837
import rospy
import time
import numpy as np
from sensor_msgs.msg import FluidPressure, Temperature

if __name__ == '__main__':
    try:
        # set up ros stuff
        rospy.init_node('ms5837_node')
        bus = rospy.get_param('~bus', '1')
        osrate = rospy.get_param('~oversampling', 'OSR_8192')
        press_variance = rospy.get_param('~press_variance', 0.001)
        temp_variance = rospy.get_param('~temp_variance', 0.001)

        if(osrate == 'OSR_256'):
            osr = ms5837.OSR_256
        elif(osrate == 'OSR_512'):
            osr = ms5837.OSR_512
        elif(osrate == 'OSR_1024'):
            osr = ms5837.OSR_1024
        elif(osrate == 'OSR_2048'):
            osr = ms5837.OSR_2048
        elif(osrate == 'OSR_4096'):
            osr = ms5837.OSR_4096
        elif(osrate == 'OSR_8192'):
            osr = ms5837.OSR_8192
        else:
            osr = ms5837.OSR_8192

        pubPress = rospy.Publisher('pressure',FluidPressure, queue_size=1)
        pubTemp = rospy.Publisher('temperature/water',Temperature, queue_size=1)
        rate = rospy.Rate(100)  # 100Hz data read
        sensor = ms5837.MS5837_30BA(int(bus))  # Default I2C bus is 1 (Raspberry Pi 3)

        # sensor.init must run immediately after installation of ms5837 object
        sensor.init()

        while not rospy.is_shutdown():
            sensor.read(oversampling=osr)  # maximum read rate of ~90Hz
            pressPa = sensor.pressure(ms5837.UNITS_Pa)
            tempC = sensor.temperature(ms5837.UNITS_Centigrade)
            
            # update messages
            press_msg = FluidPressure()
            press_msg.header.stamp = rospy.Time.now()
            press_msg.header.frame_id = 'pressure_data'
            press_msg.fluid_pressure = float(pressPa)
            press_msg.variance = float(press_variance)
            pubPress.publish(press_msg)

            temp_msg = Temperature()
            temp_msg.header.stamp = rospy.Time.now()
            temp_msg.header.frame_id = 'pressure_data'
            temp_msg.temperature = float(tempC)
            temp_msg.variance = float(temp_variance)
            pubTemp.publish(temp_msg)


            rate.sleep()

    except rospy.ROSInterruptException:
        pass
