#include <SoftwareSerial.h>
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define PIN 4
/*
  The circuit:
  - analog 7: z-axis
  - analog 6: y-axis
  - analog 5: x-axis
  Possble Case-
  - analog 0/GND: VCC
  - analog 4/5V: GND
*/

/*
  Wires:
  Red: A0/VCC
  Grey: A4/GND
  Yellow: X_OUT A1
  Purple: Y_OUT A2
  Orange: Z_OUT A3

*/
Adafruit_NeoPixel strip = Adafruit_NeoPixel(10, PIN, NEO_GRB + NEO_KHZ800);
SoftwareSerial bt (5, 6);
char expression;
char motion;

const int groundpin = A4;
const int powerpin = A0;
const int xPin = A1;
const int yPin = A2;
const int zPin = A3;

int xInit;
int yInit;
int zInit;

int xRead;
int yRead;
int zRead;

void setup() {
  pinMode(groundpin, OUTPUT);
  pinMode(powerpin, OUTPUT);
  digitalWrite(groundpin, LOW);
  digitalWrite(powerpin, HIGH);

  strip.begin();
  strip.show();

  bt.begin(9600);
  Serial.begin(9600);
  Serial.print("Bluetooth ON!");
}

void loop() {

  xRead = analogRead(xPin);
  yRead = analogRead(yPin);
  zRead = analogRead(zPin);

  //if (zRead < 330) //Hand face up
  //else if (zRead > 400) //Hand face down

  if (xRead > 310 && xRead < 380 && yRead > 290 && yRead < 370) //stop
    motion = 's';

  else {
    //if (yRead < 290) //Back
    if (yRead > 370) //Forward
      motion = 'f';

    if (xRead < 310) //Left
      motion = 'l';
    else if (xRead > 380) //Right
      motion = 'r';
  }
  bt.print(motion);
  if (bt.available()) {
    expression = bt.read();
    if (expression == 'h')
      //Serial.println("Happy");
      fill(strip.Color(0, 255, 0));
    else if (expression == 's')
      //Serial.println("Sad");
      fill(strip.Color(0, 0, 255));
    else if (expression == 'a')
      //Serial.println("Angry");
      fill(strip.Color(255, 0, 0));
    else if (expression == 'z')
      Serial.println("Sleepy");
    //theaterChaseRainbow(50);

  }
  delay(1000);
}

void fill(uint32_t c) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
  }
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
  //undo the colors
  for (uint16_t i = strip.numPixels(); i > 0; i--) {
    strip.setPixelColor(i, strip.Color(0, 0, 0));
    strip.show();
    delay(wait);
  }
}

void rainbow(uint8_t wait) {
  uint16_t i, j;

  for (j = 0; j < 256; j++) {
    for (i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for (j = 0; j < 256 * 5; j++) { // 5 cycles of all colors on wheel
    for (i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

//Theatre-style crawling lights.
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j = 0; j < 10; j++) { //do 10 cycles of chasing
    for (int q = 0; q < 3; q++) {
      for (uint16_t i = 0; i < strip.numPixels(); i = i + 3) {
        strip.setPixelColor(i + q, c);  //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (uint16_t i = 0; i < strip.numPixels(); i = i + 3) {
        strip.setPixelColor(i + q, 0);      //turn every third pixel off
      }
    }
  }
}

//Theatre-style crawling lights with rainbow effect
void theaterChaseRainbow(uint8_t wait) {
  for (int j = 0; j < 256; j++) {   // cycle all 256 colors in the wheel
    for (int q = 0; q < 3; q++) {
      for (uint16_t i = 0; i < strip.numPixels(); i = i + 3) {
        strip.setPixelColor(i + q, Wheel( (i + j) % 255)); //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (uint16_t i = 0; i < strip.numPixels(); i = i + 3) {
        strip.setPixelColor(i + q, 0);      //turn every third pixel off
      }
    }
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if (WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if (WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}
