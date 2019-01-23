#include <SoftwareSerial.h>
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define PIN 10
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
  Red: A4/VCC
  Grey: A0/GND
  Yellow: X_OUT A3
  Purple: Y_OUT A2
  Orange: Z_OUT A1

*/
Adafruit_NeoPixel strip = Adafruit_NeoPixel(18, PIN, NEO_GRB + NEO_KHZ800);
SoftwareSerial bt (5, 6);
char expression;
char motion;

const int buttonPin = 9;
const int groundpin = A0;
const int powerpin = A4;
const int zPin = A1;
const int yPin = A2;
const int xPin = A3;

const uint32_t lemon = strip.Color(255, 165, 0); //surprise
const uint32_t red = strip.Color(255, 0, 0); //angry
const uint32_t green = strip.Color(0, 255, 0); //happy
const uint32_t blue = strip.Color(0, 0, 255); //sad
const uint32_t greenishBlue = strip.Color(0, 127, 34); //sending data
const uint32_t cyan = strip.Color(0, 255, 255); //sleepy
const uint32_t off = strip.Color(0, 0, 0);

int xInit;
int yInit;
int zInit;

int xRead;
int yRead;
int zRead;

int buttonState = 0;

void setup() {
  pinMode(groundpin, OUTPUT);
  pinMode(powerpin, OUTPUT);
  pinMode(buttonPin, INPUT);
  digitalWrite(groundpin, LOW);
  digitalWrite(powerpin, HIGH);

  strip.begin();
  strip.show();

  bt.begin(9600);
  Serial.begin(9600);
  Serial.print("Bluetooth ON!");
}

void loop() {
  buttonState = digitalRead(buttonPin);
  while (buttonState == LOW) {
    motion = getDataFromGyro();
    if (motion != 's') {
      sendDataToRaspi(motion);
      Serial.println(motion);
    }

    if (motion == 'l')
      leftLed(greenishBlue, 50);
    else if (motion == 'r')
      rightLed(greenishBlue, 50);
    else if (motion == 'f' or motion =='u')
      blinkLed(greenishBlue, 100);
    clearStrip();
    delay(300);
    buttonState = digitalRead(buttonPin);
    if (buttonState == HIGH) {
      sendDataToRaspi('x');
    }
  }
  if (buttonState == HIGH) {
    rainbow(30);
    //getExpressionFromRaspiNShow();
  }
  delay(50);
}

char getDataFromGyro() {
  char data = 's';
  xRead = analogRead(xPin);
  yRead = analogRead(yPin);
  zRead = analogRead(zPin);

  //if (zRead < 330) //Hand face up
  //else if (zRead > 400) //Hand face down

  if (xRead > 320 && xRead < 380 && yRead > 310 && yRead < 380) //stop
    data = 's';

  else {
    if (yRead >= 380) //Forward
      data = 'f';
    else if (yRead <= 310)
      data = 'u'; //Back, get expression from Squid

    if (xRead <= 320) //Left
      data = 'l';
    else if (xRead >= 380) //Right
      data = 'r';
  }
  return data;
}

void sendDataToRaspi(char data) {
  bt.print(data);
}

void blinkLed(uint32_t c, uint8_t wait) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
  }
  strip.show();
  delay(wait);

  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, off);
  }
  strip.show();
  delay(wait);
}

void leftLed(uint32_t c, uint8_t wait) {
  strip.setPixelColor(9, c);
  strip.setPixelColor(8, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(9, off);
  strip.setPixelColor(8, off);
  strip.setPixelColor(10, c);
  strip.setPixelColor(7, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(10, off);
  strip.setPixelColor(7, off);
  strip.setPixelColor(11, c);
  strip.setPixelColor(6, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(11, off);
  strip.setPixelColor(6, off);
  strip.setPixelColor(12, c);
  strip.setPixelColor(5, c);
  strip.setPixelColor(0, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(12, off);
  strip.setPixelColor(5, off);
  strip.setPixelColor(0, off);
  strip.setPixelColor(13, c);
  strip.setPixelColor(4, c);
  strip.setPixelColor(1, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(13, off);
  strip.setPixelColor(4, off);
  strip.setPixelColor(1, off);
  strip.setPixelColor(14, c);
  strip.setPixelColor(3, c);
  strip.setPixelColor(2, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(14, off);
  strip.setPixelColor(3, off);
  strip.setPixelColor(2, off);
  strip.setPixelColor(15, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(15, off);
  strip.setPixelColor(16, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(16, off);
  strip.setPixelColor(17, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(16, off);
  strip.setPixelColor(17, c);
  strip.show();
  delay(wait);
  strip.setPixelColor(17, off);
  strip.show();
}

void rightLed(uint32_t c, uint8_t wait) {
  strip.setPixelColor(17, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(17, off);
  strip.setPixelColor(16, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(16, off);
  strip.setPixelColor(15, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(15, off);
  strip.setPixelColor(14, c);
  strip.setPixelColor(3, c);
  strip.setPixelColor(2, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(14, off);
  strip.setPixelColor(3, off);
  strip.setPixelColor(2, off);
  strip.setPixelColor(13, c);
  strip.setPixelColor(4, c);
  strip.setPixelColor(1, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(13, off);
  strip.setPixelColor(4, off);
  strip.setPixelColor(1, off);
  strip.setPixelColor(12, c);
  strip.setPixelColor(5, c);
  strip.setPixelColor(0, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(12, off);
  strip.setPixelColor(5, off);
  strip.setPixelColor(0, off);
  strip.setPixelColor(11, c);
  strip.setPixelColor(6, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(11, off);
  strip.setPixelColor(6, off);
  strip.setPixelColor(10, c);
  strip.setPixelColor(7, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(10, off);
  strip.setPixelColor(7, off);
  strip.setPixelColor(9, c);
  strip.setPixelColor(8, c);
  strip.show();
  delay(wait);

  strip.setPixelColor(9, off);
  strip.setPixelColor(8, off);
  strip.show();
}

void leftLedTop(uint32_t c, uint8_t wait) {
  for (uint16_t i = 9; i < 18; i++) {
    if (i > 9)
      strip.setPixelColor(i - 1, off);
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}

void rightLedTop(uint32_t c, uint8_t wait) {
  for (uint16_t i = 17; i > 8; i--) {
    if (i < 17)
      strip.setPixelColor(i + 1, off);
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}

void rainbow(uint8_t wait) {
  uint16_t i, j;

  for (j = 0; j < 256; j++) {
    for (i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i + j) & 255));
      buttonState = digitalRead(buttonPin);
      if (buttonState == LOW)
        return;
    }
    strip.show();
    delay(wait);
  }
}

void getExpressionFromRaspiNShow() {
  if (bt.available()) {
    expression = bt.read();
    if (expression == 'h')
      //Serial.println("Happy");
      fill(green);
    else if (expression == 's')
      //Serial.println("Sad");
      fill(blue);
    else if (expression == 'a')
      //Serial.println("Angry");
      fill(red);
    else if (expression == 'z')
      fill(cyan);
    //Serial.println("Sleepy");
    //theaterChaseRainbow(50);
  }
}

void fillOdd(uint32_t c) {
  for (uint16_t i = 1; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    i++;
  }
}

void fillEven(uint32_t c) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    i++;
  }
}

void clearStrip() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, off);
    strip.show();
  }
}

void fill(uint32_t c) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
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
