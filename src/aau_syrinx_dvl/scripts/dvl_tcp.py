#!/usr/bin/env python
import socket
import rospy
from time import sleep
from aau_syrinx_dvl.msg import DVL
from aau_syrinx_dvl.msg import DVLBeam


def connect():
    global s, TCP_IP, TCP_PORT
    if rospy.is_shutdown():
        exit()    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.settimeout(1)
    except socket.error as err:
        rospy.logerr("No route to host, DVL might be booting? {}".format(err))
        sleep(1)
        connect()


theDVL = DVL()
theDVLBeam = DVLBeam()
beam0 = theDVLBeam
beam1 = theDVLBeam
beam2 = theDVLBeam
beam3 = theDVLBeam

def getData():
    raw_data = ""
    while not '\n' in raw_data:
        try:
            raw_data = s.recv(1024).decode() # Add timeout for that
            if len(raw_data) == 0:
                rospy.logerr("Socket closed by the DVL, reopening")
                connect()
                continue
        except socket.timeout as err:
            rospy.logerr("Lost connection with the DVL, reinitiating the connection: {}".format(err))
            connect()
            continue
    data = raw_data.split(',')
    return data
    

def publisher():
	pub = rospy.Publisher('dvl', DVL, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		data = getData()
		if do_log_raw_data:
			rospy.loginfo(raw_data)
		if(len(data)==11):
			theDVL.header.stamp = rospy.Time.now()
			theDVL.header.frame_id = "dvl_link" 
			stat = data[0].split(";")
			theDVL.status = stat[1]
			t = data[1]
			theDVL.time = float(t[3:])
			vx = data[2]
			theDVL.velocity.x = float(vx[2:])
			vy = data[3]
			theDVL.velocity.y = float(vy[2:])
			vz = data[4]
			theDVL.velocity.z = float(vz[2:])
			jve = data[5]
			theDVL.jve = float(jve[3:])

			B1 = data[6].split(";")
			R1 = B1[0]
			S1 = B1[1]
			beam1.id = 1
			beam1.range = float(R1[3:])
			beam1.status = int(S1[1:])

			B2 = data[7].split(";")
			R2 = B2[0]
			S2 = B2[1]
			beam2.id = 2
			beam2.range = float(R2[3:])
			beam2.status = int(S2[1:])

			B3 = data[8].split(";")
			R3 = B3[0]
			S3 = B3[1]
			beam3.id = 3
			beam3.range = float(R3[3:])
			beam3.status = int(S3[1:])

			B4 = data[9].split(";")
			R4 = B4[0]
			S4 = B4[1]
			beam4.id = 4
			beam4.range = float(R4[3:])
			beam4.status = int(S4[1:])

			theDVL.beams = [beam1, beam2, beam3, beam4]

			sv = data[10]
			theDVL.sv = float(sv[2:])
			pub.publish(theDVL)
		rate.sleep()

if __name__ == '__main__':
    global s, TCP_IP, TCP_PORT, do_log_raw_data
    rospy.init_node('syrinx_dvl', anonymous=False)
    TCP_IP = rospy.get_param("~ip", "192.168.179.200")
    TCP_PORT = rospy.get_param("~port", 4000)
    do_log_raw_data = rospy.get_param("~do_log_raw_data", False)
    connect()
    try:
        publisher()
    except rospy.ROSInterruptException:
        s.close()

