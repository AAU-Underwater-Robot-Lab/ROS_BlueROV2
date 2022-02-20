#include <ros.h>
#include <bluerov2_thruster/ThrusterCmd.h>
//#include <std_msgs/Time.h>
//#include <sensor_msgs/Temperature.h>
//#include <std_srvs/Trigger.h>
#include <Servo.h>

/*
class NewHardware : public ArduinoHardware
{
  public:
  NewHardware():ArduinoHardware(&Serial, 115200){};
};
*/

//Init servos and callbacks
Servo servos[8];

float T200controlmap(float speedRad)
{
  return 0.9133 * speedRad + 1500.0;
}

//T200
void t0( const bluerov2_thruster::ThrusterCmd& msg){
  servos[0].writeMicroseconds(T200controlmap(msg.data));
}
//T200
void t1( const bluerov2_thruster::ThrusterCmd& msg){
  servos[1].writeMicroseconds(T200controlmap(msg.data));
}
//T200
void t2( const bluerov2_thruster::ThrusterCmd& msg){
  servos[2].writeMicroseconds(T200controlmap(msg.data));
}
//T200
void t3( const bluerov2_thruster::ThrusterCmd& msg){
  servos[3].writeMicroseconds(T200controlmap(msg.data));
}
//T200
void t4( const bluerov2_thruster::ThrusterCmd& msg){
  servos[4].writeMicroseconds(T200controlmap(msg.data));
}
//T200
void t5( const bluerov2_thruster::ThrusterCmd& msg){
  servos[5].writeMicroseconds(T200controlmap(msg.data));
}

void t6( const bluerov2_thruster::ThrusterCmd& msg){
  servos[6].writeMicroseconds(T200controlmap(msg.data));
}

void t7( const bluerov2_thruster::ThrusterCmd& msg){
  servos[7].writeMicroseconds(T200controlmap(msg.data));
}

//Init rosserial node
//ros::ServiceServer<std_srvs::TriggerRequest, std_srvs::TriggerResponse> server("arm_esc",&svcCallback);
ros::NodeHandle nh;

void setup()
{
  ros::Subscriber<bluerov2_thruster::ThrusterCmd> s0("thrusters/0/input", &t0);
  ros::Subscriber<bluerov2_thruster::ThrusterCmd> s1("thrusters/1/input", &t1);
  ros::Subscriber<bluerov2_thruster::ThrusterCmd> s2("thrusters/2/input", &t2);
  ros::Subscriber<bluerov2_thruster::ThrusterCmd> s3("thrusters/3/input", &t3);
  ros::Subscriber<bluerov2_thruster::ThrusterCmd> s4("thrusters/4/input", &t4);
  ros::Subscriber<bluerov2_thruster::ThrusterCmd> s5("thrusters/5/input", &t5);
  ros::Subscriber<bluerov2_thruster::ThrusterCmd> s6("thrusters/6/input", &t6);
  ros::Subscriber<bluerov2_thruster::ThrusterCmd> s7("thrusters/7/input", &t7);

  nh.getHardware()->setBaud(250000);

  nh.initNode();

  nh.subscribe(s0);
  nh.subscribe(s1);
  nh.subscribe(s2);
  nh.subscribe(s3);
  nh.subscribe(s4);
  nh.subscribe(s5);
  nh.subscribe(s6);
  nh.subscribe(s7);
  
  //nh.advertiseService(server);
  servos[0].attach(2, 1100, 1900); //Thrust 1
  servos[1].attach(3, 1100, 1900);//Thrust 2
  servos[2].attach(4, 1100, 1900);//Thrust 3
  servos[3].attach(5, 1100, 1900);//Thrust 4
  servos[4].attach(6, 1100, 1900); //Thrust 5
  servos[5].attach(7, 1100, 1900); //Thrust 6
  servos[6].attach(8, 1100, 1900); //Thrust 7
  servos[7].attach(9, 1100, 1900); //Thrust 8

  //Attempt at arming sequence
  for(int i = 0; i < 8; i += 1) //Zero signala
  { 
    servos[i].writeMicroseconds(1500);
  }
  delay(3000);
}

void loop()
{
  nh.spinOnce();
}
