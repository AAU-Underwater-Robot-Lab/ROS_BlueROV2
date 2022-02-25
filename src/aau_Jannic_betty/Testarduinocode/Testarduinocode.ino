#include <avr/io.h> 
class SSDisplay
{
  int digit;//number represented
  byte sseg;//representation in 7 segments
  public:
    SSDisplay(){};
    void initDisp(int n);//initialize 7segs representation
    void displayDigit();//display the digit on 7segs display
};

void initializePorts();

void initSegs(SSDisplay sseg[], int size);

int main()
{
  init();
  int number=0;
  initializePorts();
  SSDisplay ssg[10];
  initSegs(ssg,10);
  
  while(true)
  {   
     ssg[number].displayDigit();//display digit on 7segs
    
     if ((PIND & 0x04)==LOW)//pushbutton is pressed
     {  
         number++;//increase the number
         number %= 10;//cycle back the number to 0 if is >= 10 
         _delay_ms(5);//make a delay
          while ((PIND & 0x04)==LOW){};
         _delay_ms(5);//make a delay
     }
  }
}

void initializePorts()
{
  //Output Pin 0 -> segment a 
  //Output Pin 1 -> segment b
  //Input Pin 2 to push button
  //Output Pin 3 -> segment c 
  //Output Pin 4 -> segment d 
  //Output Pin 5 -> segment e
  //Output Pin 6 -> segment f 
  //Output Pin 7 -> segment g
  DDRD = 0xfb;//DDRD, pin 2 as input, the rest as outputs
  PORTD = 0x04;//use internal pull up resistor for pin 2
}
void initSegs(SSDisplay sseg[], int size)
{
  for (int i=0; i < size; i++)
      sseg[i].initDisp(i);
}

void SSDisplay::initDisp(int n)
{
    digit=n;
	switch (digit)
    {
      case 0: 
      	sseg=0x7b;
        break;
      case 1:
      	sseg=0x0a;
      	break;
      case 2:
        sseg=0xb3;
        break;
      case 3:
       sseg=0x9b;
      	break;
      case 4: 
        sseg=0xca;
        break;
      case 5:
        sseg=0xd9;
      	break;
      case 6: 
        sseg=0xf9;
        break;
      case 7:
        sseg=0x0b;
      	break;
      case 8: 
        sseg=0xfb;
        break;
      case 9:
        sseg=0xcb;
      	break;
      default:
       	sseg=0x7b;
    }
}

void SSDisplay::displayDigit()
{
  PORTD=sseg | 0x04; //leave pin 2 with same value
}
