#include <Adafruit_LEDBackpack.h>
/***************************************************
  This is a library for our I2C LED Backpacks

  Designed specifically to work with the Adafruit LED Matrix backpacks
  ----> http://www.adafruit.com/products/872
  ----> http://www.adafruit.com/products/871
  ----> http://www.adafruit.com/products/870

  These displays use I2C to communicate, 2 pins are required to
  interface. There are multiple selectable I2C addresses. For backpacks
  with 2 Address Select pins: 0x70, 0x71, 0x72 or 0x73. For backpacks
  with 3 Address Select pins: 0x70 thru 0x77

  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_GFX.h>

Adafruit_8x8matrix matrix = Adafruit_8x8matrix();

void setup() {
  Serial.begin(9600);
  Serial.println("8x8 LED Matrix Test");

  matrix.begin(0x70);  // pass in the address
}

static const uint8_t PROGMEM
big_smile[] =
{ B00000000,
  B00000000,
  B11111111,
  B11111111,
  B01111110,
  B01111110,
  B00111100,
  B00000000
},
triangular_big_smile_empty[] =
{ B00000000,
  B00000000,
  B11111111,
  B10000001,
  B01000010,
  B00100100,
  B00011000,
  B00000000
},
triangular_big_smile_filled[] =
{ B00000000,
  B00000000,
  B00000000,
  B11111111,
  B01111110,
  B00111100,
  B00011000,
  B00000000
},
surprise_large[] = {
  B00111100,
  B01000010,
  B10000001,
  B10000001,
  B10000001,
  B10000001,
  B01000010,
  B00111100
},
surprise_thick[] = {
  B00111100,
  B01111110,
  B11000011,
  B11000011,
  B11000011,
  B11000011,
  B01111110,
  B00111100
},
surprise_thin[] = {
  B00000000,
  B00111100,
  B01000010,
  B11000011,
  B11000011,
  B11000011,
  B01111110,
  B00111100
},
surprise_teeth[] = {
  B00000000,
  B00111100,
  B01011010,
  B11000011,
  B11000011,
  B11011011,
  B01111110,
  B00111100
}, smile[] = {
  B00000000,
  B00000000,
  B00000000,
  B11000011,
  B11000011,
  B01111110,
  B00111100,
  B00000000
}, sad[] = {
  B00000000,
  B00111100,
  B01111110,
  B11000011,
  B11000011,
  B00000000,
  B00000000,
  B00000000
}, confused[] = {
  B00000000,
  B00000000,
  B00000000,
  B01110001,
  B10011001,
  B10001110,
  B00000000,
  B00000000
}, contempt_1[] = {
  B00000000,
  B00000000,
  B00000000,
  B00000011,
  B01111110,
  B01111100,
  B00000000,
  B00000000
};


void loop() {
  //  delay(500);

  //  matrix.clear();
  //  matrix.drawBitmap(0, 0, surprise_teeth, 8, 8, LED_ON);
  //  matrix.writeDisplay();  // write the changes we just made to the display
  //  delay(500);

  //
    matrix.clear();
  //  matrix.drawRect(0,0, 8,8, LED_ON);
    matrix.fillRect(0,0, 8,8, LED_ON);
    matrix.writeDisplay();  // write the changes we just made to the display
  //  delay(500);
  //
  //  matrix.clear();
  //  matrix.drawCircle(3,3, 3, LED_ON);
  //  matrix.writeDisplay();  // write the changes we just made to the display
  //  delay(500);
  //
  //  matrix.setTextSize(1);
  //  matrix.setTextWrap(false);  // we dont want text to wrap so it scrolls nicely
  //  matrix.setTextColor(LED_ON);
  //  for (int8_t x=0; x>=-36; x--) {
  //    matrix.clear();
  //    matrix.setCursor(x,0);
  //    matrix.print("Hello");
  //    matrix.writeDisplay();
  //    delay(100);
  //  }
  //  matrix.setRotation(3);
  //  for (int8_t x=7; x>=-36; x--) {
  //    matrix.clear();
  //    matrix.setCursor(x,0);
  //    matrix.print("World");
  //    matrix.writeDisplay();
  //    delay(100);
  //  }
  //  matrix.setRotation(0);
}
