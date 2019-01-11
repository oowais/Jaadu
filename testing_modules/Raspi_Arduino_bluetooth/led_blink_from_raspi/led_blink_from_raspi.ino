#include <SoftwareSerial.h> //Serial library

/**
   Arduino connection HC-05 connection:
   HC-05  | Arduino
   TX     | 5
   RX     | 6
*/
// Here, we exchange them -
SoftwareSerial bt (5, 6); //RX, TX (Switched on the Bluetooth - RX -> TX | TX -> RX)
int LEDPin = 13; //LED PIN on Arduino
int btdata;

void setup() {
  bt.begin(9600);
  bt.print("Bluetooth ON. Press 1 or 0 to blink LED..");
  pinMode (LEDPin, OUTPUT);
}

void loop() {

  if (bt.available()) {
    btdata = bt.read();
    //    blinkLED(btdata)/;
    if (btdata == '1') {
      //if 1
      digitalWrite (LEDPin, HIGH);
      bt.print("LED ON!");
      bt.print("\n");
    }
    if (btdata == '0') {
      //if 0
      digitalWrite (LEDPin, LOW);
      bt.print("LED OFF!");
      bt.print("\n");
    }
  }
  delay (100); //prepare for data
}
