#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import FluidPressure, Temperature

data = []
time = 0

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '\u2588', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def calculate(array):
    mean = 0
    total = 0
    for point in array:
        mean += point
    mean /= len(array)
    for point in array:
        total += (point - mean) * (point - mean)
    total /= len(array)
    return total

def pressureMean(msg):
    global time
    data.append(msg.fluid_pressure)
    time += 1
    if time < 2000:
        printProgressBar(time + 1, 2000, prefix = 'Progress:', suffix = 'Complete', length = 50)
    if time >= 2000:
        var = calculate(data)
        print(f"\rTemp: {var:.5f} Pa²", end = "\r")

def main():
    rospy.init_node('ms5837_pressvariance_node')
    while not rospy.is_shutdown():
        rospy.Subscriber('pressure', FluidPressure, pressureMean)
        rospy.spin()

if __name__ == '__main__':
    main()
