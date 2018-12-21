#include <Servo.h>

/*
The circuit:

VCC -> 3.3V
GND -> GND
TXD -> RX
RXD -> TX

*/
Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(8);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    char data = Serial.read(); // reading the data received from the bluetooth module
    switch (data)
    {
      case 'a': myservo.write(50); break; // when a is pressed on the app on your smart phone
      case 'd': myservo.write(150); break; // when d is pressed on the app on your smart phone
      default : break;
    }
    Serial.println(data);
  }
  delay(50);
}
