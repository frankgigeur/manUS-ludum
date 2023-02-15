#include "define.h"
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include "define.h"

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

void setup() {
  Serial.begin(9600);
  Serial.println("8 channel Servo test!");

  pwm.begin();
  pwm.setOscillatorFrequency(PCA9685_OSC_FREQ);
  pwm.setPWMFreq(HS422_SERVO_FREQ);
 
  delay(10);
}


void loop() {
  delay(2000);
  pwm.setPWM(6, 0, HS422_CNT_SERVO_MAX);
  pwm.setPWM(7, 0, HS422_CNT_SERVO_MAX);
  delay(2000);
  pwm.setPWM(6, 0, HS422_CNT_SERVO_MIN);
  pwm.setPWM(7, 0, HS422_CNT_SERVO_MIN);
}