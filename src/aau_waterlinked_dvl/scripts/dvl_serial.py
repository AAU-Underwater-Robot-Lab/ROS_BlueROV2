#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import String
from aau_waterlinked_dvl.msg import DVL_Serial

ser = serial.Serial(
	port='/dev/ttyUSB0',\
	baudrate=115200,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
	timeout=0)

theDVL = DVL_Serial()

def resetDeadReck():
    ser.write("wcr\n".encode()) #reset DVL

def darkMode():
    ser.write("wcs,,,,y\n".encode()) #Set Darkmode

def getData():
    global oldJson, s
    raw_data = ""

    while not '\n' in raw_data:
	rec = ser.read()
        raw_data = raw_data + rec
    return raw_data

def DVL_pub():
    rospy.init_node('DVL_Waterlinked', anonymous=True)
    pub_raw = rospy.Publisher('dvl/raw_string', String, queue_size=10)
    pub = rospy.Publisher('DVL', DVL_Serial, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    line = []
    while not rospy.is_shutdown():
	raw_data = getData()
	pub_raw.publish(raw_data)
	DVL_entries = raw_data.split(',')
	if(DVL_entries[0] == 'wrz'): #Velocity report
		if(len(DVL_entries) == 12):
			if(DVL_entries[4] == 'y'):
				theDVL.header.stamp = rospy.Time.now()
				theDVL.header.frame_id = "dvl_link" 
				theDVL.velocity.x = float(DVL_entries[1])
				theDVL.velocity.y = float(DVL_entries[2])
				theDVL.velocity.z = float(DVL_entries[3])
				theDVL.velocity_valid = bool('y'==DVL_entries[4])
				theDVL.altitude = float(DVL_entries[5])
				theDVL.fom = float(DVL_entries[6])
				cov_array = []
				DVL_cov = DVL_entries[7].split(';')
				for cov	in DVL_cov:
				    cov_array.append(float(cov))
				theDVL.covariance = cov_array
				theDVL.time = float(DVL_entries[10])
				status = DVL_entries[11].split('*')
				theDVL.status = int(status[0])
				pub.publish(theDVL)


	if(DVL_entries[0] == 'wrp'): #Dead reckoning report
		pass
		#x 	Distance in X direction (m)
		#y 	Distance in Y direction (m)
		#z 	Distance in downward direction (m)
		#pos_std 	Standard deviation (Figure of merit) for position (m)
		#roll 	Rotation around X axis (degrees)
		#pitch 	Rotation around Y axis (degrees)
		#yaw 	Rotation around Z axis, i.e. heading (degrees)
		#status 	Reports if there are any issues with the DVL (0 if no errors, 1 otherwise)
	rate.sleep()

if __name__ == '__main__':
    try:
	DVL_pub()
    except rospy.ROSInterruptException:
	ser.close()
	
