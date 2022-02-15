#!/bin/bash
echo "Setting can0 at 500kbit/s"
ip link set can0 type can bitrate 500000
echo "Starting can0"
ifconfig can0 up
