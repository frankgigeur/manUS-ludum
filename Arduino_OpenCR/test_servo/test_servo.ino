#include "define.h"
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

void roche();
void papier();
void ciseau();
void cold_stop();
// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

const byte numChars = 64;
char receivedChars[numChars];
bool newData = false;
void replyToUi();
void recvWithStartEndMarkers() ;

void setup() {

  Serial.begin(115200);
  //Serial.println("<Arduino is ready>");

  pwm.begin();
  pwm.setOscillatorFrequency(PCA9685_OSC_FREQ);
  pwm.setPWMFreq(HS422_SERVO_FREQ);

}


void loop() {

  recvWithStartEndMarkers();
  replyToUi();

  //pwm.setPWM(finger1_ID, 0, HS422_CNT_SERVO_MIN);
  //delay(1000);  
  //pwm.setPWM(finger1_ID, 0, cnt_SERVO_reach);
  //(1000);  
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char lastReadChar;
    while (Serial.available() > 0 && newData == false) {
        lastReadChar = Serial.read();
        if (recvInProgress) {
            if (lastReadChar != endMarker) {
                receivedChars[ndx] = lastReadChar;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }
        else if (lastReadChar == startMarker) {
            recvInProgress = true;
        }
    }
}
void replyToUi(){
  if(newData){
        switch(receivedChars[0])
        {
          case 'R':
            Serial.println("<roche>");
            roche();
            break;
          case 'C':
            Serial.println("<ciseaux>");  
            ciseau();
            break;
          case 'P':
            Serial.println("<papier>");
            papier();
            break;
          case 'A':
            Serial.println("<arret>");
            cold_stop();
            break;
          default:
            break;
        }
        newData = false;
      }
}

void roche()
{
  pwm.setPWM(finger1_ID, 0, cnt_SERVO_reach);
}

void papier()
{
  pwm.setPWM(finger1_ID, 0, HS422_CNT_SERVO_MIN);
}

void ciseau()
{
  pwm.setPWM(finger1_ID, 0, HS422_CNT_SERVO_MIN);
}

void cold_stop()
{
  pwm.setPWM(finger1_ID, 0, 0);
}