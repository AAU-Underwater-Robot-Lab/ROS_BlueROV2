#include "ros/ros.h"
#include "TMSerial.h"

// TM200 Interface:
EasyObjectDictionary eOD;
EasyProfile          eP(&eOD);

//Define the serial port here:
#define         DEVICE_PORT             "/dev/ttyS0"

TMSerial::TMSerial()
{
  serialib1 = new serialib;
}

TMSerial::~TMSerial()
{
}

char TMSerial::Serialport_Open()
{
    int Ret;
    Ret=serialib1->Open(DEVICE_PORT,115200);                                // Open serial link at 115200 bauds
    if (Ret!=1) {                                                           // If an error occured...
        printf ("Error while opening port. Permission problem ?\n");        // ... display a message ...
        return Ret;                                                         // ... quit the application
    }
    printf ("Serial port opened successfully !\n");
    return 1;
}

//----------------------------------------------------------------------------------------
// Serial Receive Data Example
void TMSerial::On_SerialRX(bluerov2_tm200::Imu *msg_imu){
    char serialBuffer[128];
    serialib1->Read(serialBuffer,128,NULL);                      // Step 1: read the received data buffer of the Serial Port
    char*  rxData = serialBuffer;                                //         and then convert it to data types acceptable by the
    int    rxSize = sizeof(serialBuffer);                        //         Communication Abstraction Layer (CAL).

    Ep_Header header;
    if(EP_SUCC_ == eP.On_RecvPkg(rxData, rxSize, &header)){    // Step 2: Tell the CAL that new data has arrived.
                                                               //         It does not matter if the new data only contains a fraction
                                                               //         of a complete package, nor does it matter if the data is broken
                                                               //         during the transmission. On_RecvPkg() will only return EP_SUCC_
                                                               //         when a complete and correct package has arrived.

        // Example Reading of the Short ID of the device who send the data:
        uint32 fromId = header.fromId;                         // Step 3.1:  Now we are able to read the received payload data.
                                                               //            header.fromId tells us from which Motion Module the data comes.

        //Supress "parameter unused" complier warning:
        (void)fromId;

        switch (header.cmd) {                                  // Step 3.2: header.cmd tells what kind of data is inside the payload.
        case EP_CMD_ACK_:{                                     //           We can use a switch() as demonstrated here to do different
            Ep_Ack ep_Ack;                                     //           tasks for different types of data.
            if(EP_SUCC_ == eOD.Read_Ep_Ack(&ep_Ack)){

            }
        }break;
        case EP_CMD_STATUS_:{
            Ep_Status ep_Status;
            if(EP_SUCC_ == eOD.Read_Ep_Status(&ep_Status)){
		
            }
        }break;
        case EP_CMD_Raw_GYRO_ACC_MAG_:{
            Ep_Raw_GyroAccMag ep_Raw_GyroAccMag;
            if(EP_SUCC_ == eOD.Read_Ep_Raw_GyroAccMag(&ep_Raw_GyroAccMag)){
		float accX = ep_Raw_GyroAccMag.acc[0];
                float accY = ep_Raw_GyroAccMag.acc[1];
                float accZ = ep_Raw_GyroAccMag.acc[2];
                float gyroX = ep_Raw_GyroAccMag.gyro[0];
                float gyroY = ep_Raw_GyroAccMag.gyro[1];
                float gyroZ = ep_Raw_GyroAccMag.gyro[2];

                msg_imu->linear_acceleration.x = accX;
                msg_imu->linear_acceleration.y = accY;
                msg_imu->linear_acceleration.z = accZ;
                msg_imu->angular_velocity.x = gyroX;
                msg_imu->angular_velocity.y = gyroY;
                msg_imu->angular_velocity.z = gyroZ;

            }
        }break;
        case EP_CMD_Q_S1_S_:{
            Ep_Q_s1_s ep_Q_s1_s;
            if(EP_SUCC_ == eOD.Read_Ep_Q_s1_s(&ep_Q_s1_s)){

            }
        }break;
        case EP_CMD_Q_S1_E_:{
            Ep_Q_s1_e ep_Q_s1_e;
            if(EP_SUCC_ == eOD.Read_Ep_Q_s1_e(&ep_Q_s1_e)){ // Step 3.3: If we decided that the received Quaternion should be used,
                                                            //           Here is an example of how to access the Quaternion data.
                float q1 = ep_Q_s1_e.q[0];
                float q2 = ep_Q_s1_e.q[1];
                float q3 = ep_Q_s1_e.q[2];
                float q4 = ep_Q_s1_e.q[3];
                uint32 timeStamp = ep_Q_s1_e.timeStamp;     //           TimeStamp indicates the time point (since the Module has been powered on),
                                                            //           when this particular set of Quaternion was calculated. (Unit: uS)
                                                            //           Note that overflow will occure when the uint32 type reaches its maximum value.
                uint32 deviceId  = ep_Q_s1_e.header.fromId; //           The ID indicates the device Short ID telling which Motion Module the data comes from.

                msg_imu->orientation.x = q1;
                msg_imu->orientation.y = q2;
                msg_imu->orientation.z = q3;
                msg_imu->orientation.w = q4;
            }
        }break;
        case EP_CMD_EULER_S1_S_:{
            Ep_Euler_s1_s ep_Euler_s1_s;
            if(EP_SUCC_ == eOD.Read_Ep_Euler_s1_s(&ep_Euler_s1_s)){

            }
        }break;
        case EP_CMD_EULER_S1_E_:{
            Ep_Euler_s1_e ep_Euler_s1_e;
            if(EP_SUCC_ == eOD.Read_Ep_Euler_s1_e(&ep_Euler_s1_e)){

            }
        }break;
        case EP_CMD_RPY_:{
            Ep_RPY ep_RPY;
            if(EP_SUCC_ == eOD.Read_Ep_RPY(&ep_RPY)){     //           Another Example reading of the received Roll Pitch and Yaw
                float roll  = ep_RPY.roll;
                float pitch = ep_RPY.pitch;
                float yaw   = ep_RPY.yaw;
                uint32 timeStamp = ep_RPY.timeStamp;      //           TimeStamp indicates the time point (since the Module has been powered on),
                                                          //           when this particular set of Roll-Pitch-Yaw was calculated. (Unit: uS)
                                                          //           Note that overflow will occure when the uint32 type reaches its maximum value.
                uint32 deviceId  = ep_RPY.header.fromId;  //           The ID indicates from wich IMU Module the data comes from.

                //std::printf("Orientation: %4.2f \n", roll);
                msg_imu->pitch = pitch;
                msg_imu->roll = roll;
                msg_imu->yaw = yaw;

            }
        }break;
        case EP_CMD_GRAVITY_:{
            Ep_Gravity ep_Gravity;
            if(EP_SUCC_ == eOD.Read_Ep_Gravity(&ep_Gravity)){

            }
        }break;
        }

    }
}
// Serial Receive Data Example
//----------------------------------------------------------------------------------------



int main(int argc, char **argv)
{
    TMSerial tmSerial1;
    // Open serial port
    tmSerial1.Serialport_Open();

    ros::init(argc, argv, "tmSerial");
    ros::NodeHandle nh;
    bluerov2_tm200::Imu msg_imu;
    ros::Publisher TM200_pub = nh.advertise<bluerov2_tm200::Imu>("TM200", 1000);

    ros::Rate loop_rate(100);
    while (ros::ok())
    {
      tmSerial1.On_SerialRX(&msg_imu);
      TM200_pub.publish(msg_imu);

      //ros::spinOnce();
      loop_rate.sleep();
    }

    return 0;
}
