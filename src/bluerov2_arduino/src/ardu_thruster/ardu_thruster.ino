/* 
 * rosserial::std_msgs::Float64 Test
 * Receives a Float64 input, subtracts 1.0, and publishes it
 
#define USBCON
#define USE_USBCON */
#include <ros.h>
#include <bluerov2_thruster/ThrusterCmd.h>
#include <std_msgs/Time.h>
#include <sensor_msgs/Temperature.h>
#include <std_srvs/Trigger.h>
#include <Servo.h>
// Include the libraries we need for temperature
//#include <OneWire.h>
//#include <DallasTemperature.h>

// Data wire is plugged into port 2 on the Arduino
//#define ONE_WIRE_BUS 20

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
//OneWire oneWire(ONE_WIRE_BUS);
// Pass our oneWire reference to Dallas Temperature. 
//DallasTemperature sensors(&oneWire);

class NewHardware : public ArduinoHardware
{
  public:
  NewHardware():ArduinoHardware(&Serial3, 250000){};
};

//Init servos and callbacks
Servo servos[8];

float T200controlmap(float speedRad)
{
  return 0.9133 * speedRad + 1500.0;
}

float T500controlmap(float speedRad)
{
  return 1.21 * speedRad + 1500.0;
}

//T500
void thruster0Cb( const bluerov2_thruster::ThrusterCmd& msg){
  servos[0].writeMicroseconds(T500controlmap(msg.data));
}
//T200 cluster
void thruster1Cb( const bluerov2_thruster::ThrusterCmd& msg){
  servos[1].writeMicroseconds(T200controlmap(msg.data));
}
//T500
void thruster2Cb( const bluerov2_thruster::ThrusterCmd& msg){
  servos[2].writeMicroseconds(T500controlmap(msg.data));
}
//T200 cluster
void thruster3Cb( const bluerov2_thruster::ThrusterCmd& msg){
  servos[3].writeMicroseconds(T200controlmap(msg.data));
}
//T500
void thruster4Cb( const bluerov2_thruster::ThrusterCmd& msg){
  servos[4].writeMicroseconds(T500controlmap(msg.data));
}
//T200 cluster
void thruster5Cb( const bluerov2_thruster::ThrusterCmd& msg){
  servos[5].writeMicroseconds(T200controlmap(msg.data));
}
//T500
void thruster6Cb( const bluerov2_thruster::ThrusterCmd& msg){
  servos[6].writeMicroseconds(T500controlmap(msg.data));
}
//T200 cluster
void thruster7Cb( const bluerov2_thruster::ThrusterCmd& msg){
  servos[7].writeMicroseconds(T200controlmap(msg.data));
}

//int i = 0;
//void svcCallback(const std_srvs::TriggerRequest & req, std_srvs::TriggerResponse & res){
//        if((i++)%2)
//                res.message = "hello";
//        else
//                res.message = "ros";
//        res.success = true; 
//        //printf("Service request message: \"%s\" received, responding with: %s\n", req.input, res.output);
//}

//Init rosserial node
ros::NodeHandle_<NewHardware> nh;
sensor_msgs::Temperature test;
ros::Subscriber<bluerov2_thruster::ThrusterCmd> s0("thrusters/0/input", &thruster0Cb);
ros::Subscriber<bluerov2_thruster::ThrusterCmd> s1("thrusters/1/input", &thruster1Cb);
ros::Subscriber<bluerov2_thruster::ThrusterCmd> s2("thrusters/2/input", &thruster2Cb);
ros::Subscriber<bluerov2_thruster::ThrusterCmd> s3("thrusters/3/input", &thruster3Cb);
ros::Subscriber<bluerov2_thruster::ThrusterCmd> s4("thrusters/4/input", &thruster4Cb);
ros::Subscriber<bluerov2_thruster::ThrusterCmd> s5("thrusters/5/input", &thruster5Cb);
ros::Subscriber<bluerov2_thruster::ThrusterCmd> s6("thrusters/6/input", &thruster6Cb);
ros::Subscriber<bluerov2_thruster::ThrusterCmd> s7("thrusters/7/input", &thruster7Cb);
ros::Publisher p("powerbottle_temp", &test);
//ros::ServiceServer<std_srvs::TriggerRequest, std_srvs::TriggerResponse> server("arm_esc",&svcCallback);

void setup()
{
  SerialUSB.begin(9600);
  nh.getHardware()->setBaud(250000);
  nh.initNode();
  nh.advertise(p);
  nh.subscribe(s0);
  nh.subscribe(s1);
  nh.subscribe(s2);
  nh.subscribe(s3);
  nh.subscribe(s4);
  nh.subscribe(s5);
  nh.subscribe(s6);
  nh.subscribe(s7);

  // Start up the temperature library
  //sensors.begin();
  
  //nh.advertiseService(server);
  servos[7].attach(6, 1100, 1900); //Thrust 0
  servos[5].attach(7, 1100, 1900); //Thrust 1
  servos[0].attach(8, 1100, 1900); //Thrust 2
  servos[4].attach(9, 1100, 1900); //Thrust 3
  servos[2].attach(10, 1100, 1900);//Thrust 4
  servos[3].attach(11, 1100, 1900);//Thrust 5
  servos[1].attach(12, 1100, 1900);//Thrust 6
  servos[6].attach(13, 1100, 1900);//Thrust 7

  //Attempt at arming sequence
  for(int i = 0; i < 8; i += 1) //Zero signala
  { 
    servos[i].writeMicroseconds(1500);
  }
  delay(3000);
}

int i = 0;

float trans = 3.3/4096;
float offset = 0.8;
float factor = 0.00265;
int fixtemp = 10;

float temperatur() 
{
  uint32_t ulValue = 0;
  uint32_t ulChannel;
  
  // Enable the corresponding channel
  adc_enable_channel(ADC, ADC_TEMPERATURE_SENSOR);

  // Enable the temperature sensor
  adc_enable_ts(ADC);

  // Start the ADC
  adc_start(ADC);

  // Wait for end of conversion
  while ((adc_get_status(ADC) & ADC_ISR_DRDY) != ADC_ISR_DRDY);

  // Read the value
  ulValue = adc_get_latest_value(ADC);

  // Disable the corresponding channel
  adc_disable_channel(ADC, ADC_TEMPERATURE_SENSOR);

  float treal = fixtemp + (( trans * ulValue ) - offset ) / factor;

  return treal;
}



void loop()
{
  i++;
  nh.spinOnce();
  if(i >= 100000)
  {
    float tempint = temperatur();
    //SerialUSB.print("Temperature for the device is approx: ");
    SerialUSB.println(tempint);
    test.header.stamp = nh.now(); 
    test.temperature = tempint;
    p.publish( &test );
    i = 0;
  }
/*
  if(i >= 100)
  {
      //Add DS18B20
      // call sensors.requestTemperatures() to issue a global temperature 
      // request to all devices on the bus
      SerialUSB.print("Requesting temperatures...");
      sensors.requestTemperatures(); // Send the command to get temperatures
      //SerialUSB.println("DONE");
      // After we got the temperatures, we can print them here.
      // We use the function ByIndex, and as an example get the temperature from the first sensor only.
      float tempC = sensors.getTempCByIndex(0);
    
      // Check if reading was successful
      if(tempC != DEVICE_DISCONNECTED_C) 
      {

        //SerialUSB.print("Temperature for the device 1 (index 0) is: ");
        //SerialUSB.println(tempC);
      } 
      else
      {
        //SerialUSB.println("Error: Could not read temperature data");
      }
      i = 0;
  }*/
}
