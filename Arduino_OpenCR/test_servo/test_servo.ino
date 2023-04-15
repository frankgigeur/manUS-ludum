#include "define.h"
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

void roche();
void papier();
void ciseau();
void cold_stop();
void initial();

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
  cold_stop();
  delay(3000);  
}


void loop() {

  recvWithStartEndMarkers();
  replyToUi();
  //  roche();
  //  delay(3000);  
  //  initial();
  //  delay(3000);  
  //  papier();
  //  delay(3000);  
  //  initial();
  //  delay(3000);
  //  ciseau();
  //  delay(3000);  
  //  initial();
  //  delay(3000);
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
          case 'I':
            initial();
            Serial.println("<initial>");
            break;
          case 'R':
            roche();
            Serial.println("<roche>");
            break;
          case 'C':
            ciseau();
            Serial.println("<ciseaux>");  
            break;
          case 'P':
            papier();
            Serial.println("<papier>");
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

void initial()
{
  pwm.setPWM(ID_petitdoigt, 0, HS422_pd_inc_init);
  pwm.setPWM(ID_annulaire, 0, HS422_an_inc_init);
  pwm.setPWM(ID_majeur, 0, HS422_ma_inc_init);
  pwm.setPWM(ID_index, 0, HS422_in_inc_init);
  pwm.setPWM(ID_pouce, 0, HS422_po_inc_init);
}

void roche()
{
  pwm.setPWM(ID_pouce, 0, HS422_po_inc_comp);
  delay(30);
  pwm.setPWM(ID_petitdoigt, 0, HS422_pd_inc_comp);
  pwm.setPWM(ID_annulaire, 0, HS422_an_inc_comp);
  pwm.setPWM(ID_majeur, 0, HS422_ma_inc_comp);
  pwm.setPWM(ID_index, 0, HS422_in_inc_comp);
 
}

void papier()
{
  pwm.setPWM(ID_petitdoigt, 0, HS422_pd_ext_comp);
  pwm.setPWM(ID_annulaire, 0, HS422_an_ext_comp);
  pwm.setPWM(ID_majeur, 0, HS422_ma_ext_comp);
  pwm.setPWM(ID_index, 0, HS422_in_ext_comp);
  pwm.setPWM(ID_pouce, 0, HS422_po_ext_comp);
}

void ciseau()
{
  pwm.setPWM(ID_petitdoigt, 0, HS422_pd_inc_comp);
  pwm.setPWM(ID_annulaire, 0, HS422_an_inc_comp);
  pwm.setPWM(ID_majeur, 0, HS422_ma_ext_comp);
  pwm.setPWM(ID_index, 0, HS422_in_ext_comp);
  pwm.setPWM(ID_pouce, 0, HS422_po_inc_comp);
}

void cold_stop()
{
  pwm.setPWM(ID_petitdoigt, 0, 0);
  pwm.setPWM(ID_annulaire, 0, 0);
  pwm.setPWM(ID_majeur, 0, 0);
  pwm.setPWM(ID_index, 0, 0);
  pwm.setPWM(ID_pouce, 0, 0);
}
