[Go back](../../README.md)

# ms5837

## Description

Python I2C interface for publishing MS5837 external pressure and tempurature. Based on blue robotics' ms5837 python library.

## Build Instructions 

* `sudo apt-get install python-smbus`

## Topics:
* `pressure`:
  Publishes `sensor_msgs/FluidPressure` with pressure (Pa).
* `temperature/water`:
  Publishes `sensor_msgs/Temperature` with tempurature (&deg;C).

## Parameters/Reconfigs:
*  `oversampling`: This is the parameter that is used to tune the over sampling rate (Greater oversampling increases resolution, but takes longer and increases current consumption)
    * OSR_256
    * OSR_512
    * OSR_1024
    * OSR_2048
    * OSR_4096
    * **OSR_8192 (Default)**
* `press_variance`: The pressure variance (Pa²) can be found by running `rosrun bluerov2_m5837 ms5837_variance_pressure.py`, when the sensor node is running.
* `temp_variance`: The temperature variance (degC²) can be found by running `rosrun bluerov2_m5837 ms5837_variance_temperature.py`, when the sensor node is running.

## Launch Information

Make sure that a MS5837 is plugged in to the Jetson Nano's I2C interface and that the MS5837 has an address of 0x76 using

`sudo i2cdetect -y 1`

Launch using

```
<node type="bluerov2_ms5837.py" pkg="bluerov2_ms5837" name="ms5837_node">
  <param name="oversampling" value="OSR_8192"/>
  <param name="press_variance" value="0.001"/>
  <param name="temp_variance" value="0.001"/>
</node>
```

in a launch file or using

`rosrun bluerov2_ms5837 bluerov2_ms5837.py`

## Troubleshooting

If a an input/output error occurs make sure the I2C bus is operational and the sensor is properly connected:
* `sudo i2cdetect -y 1` to make sure that the bus is operational and that the ms5837 has an address of 0x76

## Contributors 

* Current maintaner: Fredrik Sørensen

## Helpful Resources

* https://github.com/bluerobotics/ms5837-python
