#include "define.h"
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include "define.h"

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
  Serial.println("<Arduino is ready>");

  pwm.begin();
  pwm.setOscillatorFrequency(PCA9685_OSC_FREQ);
  pwm.setPWMFreq(HS422_SERVO_FREQ);

}


void loop() {

  recvWithStartEndMarkers();
  replyToUi();

}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();
        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string                recvInProgress = false;
                Serial.println("receivedendmarker");
                ndx = 0;
                newData = true;
            }
        }
        else if (rc == startMarker) {
            Serial.println("receivedstartmarker");
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
