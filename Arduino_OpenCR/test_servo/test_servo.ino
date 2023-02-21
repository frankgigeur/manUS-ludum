#include "define.h"
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include "define.h"

#define finger1_ID 7                // moteur ID du doigt 1
#define angle_traction 59           // angle en deg pour plier
#define cnt_SERVO_reach 235         // reach
#define cnt_SERVO_half_reach 170    // half reach 

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

void setup() {
  Serial.begin(9600);
  Serial.println("8 channel Servo test!");

  pwm.begin();
  pwm.setOscillatorFrequency(PCA9685_OSC_FREQ);
  pwm.setPWMFreq(HS422_SERVO_FREQ);
 
  pwm.setPWM(finger1_ID, 0, HS422_CNT_SERVO_MIN);
  pwm.setPWM(6, 0, HS422_CNT_SERVO_MIN);
  delay(2000);
  pwm.setPWM(finger1_ID, 0, cnt_SERVO_reach);
  pwm.setPWM(6, 0, cnt_SERVO_reach);
}


void loop() {

  delay(2000);
  pwm.setPWM(finger1_ID, 0, HS422_CNT_SERVO_MIN);
  delay(2000);
  pwm.setPWM(finger1_ID, 0, cnt_SERVO_reach);

}