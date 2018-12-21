/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

#include<Servo.h>

int ledPin = 11;
int buttonPin = 2;

int buttonState = 0;
int val = 0;
Servo servo;
int state = 0;

void setup() {
  servo.attach(9);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  resetServo();
  digitalWrite(ledPin, HIGH);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {
    blinkLed(20);
    moveForward(0, 90, 1);
    delay(1000);
    moveForward(90, 180, 0);
    delay(5000);
    digitalWrite(ledPin, HIGH);
    delay(1000);
    resetServo();
  }
  delay(10);
}

void moveForward(int startPos, int endPos, int isBlink) {
  for (val = startPos; val < endPos; val += 1) {
    servo.write(val);
    if (isBlink == 1 && val % 5 == 0) {
      blinkLed(1);
    }
    delay(1);
  }
}

void resetServo() {
  for (val = 180; val >= 0; val -= 1) {
    servo.write(val);
    delay(1);
  }
}

void blinkLed(int num) {
  for (int i = 0; i < num; i++) {
    digitalWrite(ledPin, HIGH);
    delay(50);
    digitalWrite(ledPin, LOW);
    delay(50);
  }
}
