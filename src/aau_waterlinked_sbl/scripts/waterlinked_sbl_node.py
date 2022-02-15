#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
import json
import rospy
import time
from nav_msgs.msg import Odometry
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PointStamped


def get_data(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException, exc:
        print('Exception occured {}'.format(exc))
        return None

    if r.status_code != requests.codes.ok:
        print('Got error {}: {}'.format(r.status_code, r.text))
        return None

    return r.json()


def get_acoustic_position_filtered(base_url):
    return get_data('{}/api/v1/position/acoustic/filtered'.format(base_url))


def get_acoustic_position_raw(base_url):
    return get_data('{}/api/v1/position/acoustic/raw'.format(base_url))


def get_global_position(base_url):
    return get_data('{}/api/v1/position/global'.format(base_url))


def waterlinked(base_url):
    rospy.init_node('waterlinked', anonymous=True)
    rate = rospy.Rate(40)  # 40hz
    raw_pub = rospy.Publisher('acoustic_position/raw',
                              PointStamped, queue_size=120)
    filtered_pub = rospy.Publisher('acoustic_position/filtered',
                        PointStamped, queue_size=120)
    global_pub = rospy.Publisher('global_position',
                                  NavSatFix, queue_size=120)

    def set_depth(data,args):
        depth = data.pose.pose.position.z
        #rospy.loginfo("Depth: %s",depth)
	payload = dict(depth=depth, temp=6.5) #Depth Fixed temp for now (degC).
	try:
	    r = requests.put("{}/api/v1/external/depth".format(base_url), json=payload, timeout=10)
        except Exception, exc:
            rospy.logerr_throttle(30, "Could not send depth to SBL, possible ethernet connection issue")

    #Skal rettes til i forhold til publisher fra depth sensor.
    rospy.Subscriber("pose",Odometry,set_depth,base_url)


    def publish_raw(data_raw):
        raw_point = PointStamped()
        raw_point.header.frame_id = "/map"
        raw_point.header.stamp = rospy.Time.now()
        raw_point.point.x = data_raw['x']
        raw_point.point.y = data_raw['y']
        raw_point.point.z = data_raw['z']
        raw_pub.publish(raw_point)

    def publish_filtered(data_filtered):
        filtered_point = PointStamped()
        filtered_point.header.frame_id = "/map"
        filtered_point.header.stamp = rospy.Time.now()
        filtered_point.point.x = data_filtered['x']
        filtered_point.point.y = data_filtered['y']
        filtered_point.point.z = data_filtered['z']
        filtered_pub.publish(filtered_point)

    last_raw, last_filtered = None, None

    while not rospy.is_shutdown():
        data_raw = get_acoustic_position_raw(base_url)

	if data_raw is None:
            rospy.logerr_throttle(30, "No data returned from SBL, possible ethernet connection issue")
	else:
	    if last_raw is None:
	        publish_raw(data_raw)
	        last_raw = data_raw
	    else:
	        dist = (data_raw['x'] - last_raw['x']) ** 2 +\
	              (data_raw['y'] - last_raw['y']) ** 2 +\
	              (data_raw['z'] - last_raw['z']) ** 2

		if dist > 1e-10:
	            publish_raw(data_raw)
	            last_raw = data_raw

	        data_filtered = get_acoustic_position_filtered(base_url)

	        if last_filtered is None:
	            publish_filtered(data_filtered)
	            last_filtered = data_filtered
	        else:
	            dist = (data_filtered['x'] - last_filtered['x']) ** 2 +\
	                   (data_filtered['y'] - last_filtered['y']) ** 2 +\
	                   (data_filtered['z'] - last_filtered['z']) ** 2
	            if dist > 1e-10:
	                publish_filtered(data_filtered)
	                last_filtered = data_filtered

	        data_global = get_global_position(base_url)
	        global_point = NavSatFix()
	        global_point.header.stamp = rospy.Time.now()
	        global_point.header.frame_id = "/map"
	        global_point.latitude = data_global['lat']
	        global_point.longitude = data_global['lon']
	        global_pub.publish(global_point)
        rate.sleep()

if __name__ == '__main__':
    try:
        base_url = "http://192.168.2.94"
        #rospy.loginfo("Connecting to: %s",base_url)

        waterlinked(base_url)
    except rospy.ROSInterruptException:
        pass

