#include <Adafruit_LEDBackpack.h>
#include <Wire.h>
#include <Adafruit_GFX.h>

Adafruit_8x8matrix matrix = Adafruit_8x8matrix();

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  Serial.println("8x8 LED Matrix Test");

  matrix.begin(0x70);  // pass in the address

}

int boot[64][2] = {{0, 0}, {0, 1}, {0, 2}, {0, 3}, {0, 4}, {0, 5}, {0, 6}, {0, 7},
  {1, 0}, {1, 1}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {1, 6}, {1, 7},
  {2, 0}, {2, 1}, {2, 2}, {2, 3}, {2, 4}, {2, 5}, {2, 6}, {2, 7},
  {3, 0}, {3, 1}, {3, 2}, {3, 3}, {3, 4}, {3, 5}, {3, 6}, {3, 7},
  {4, 0}, {4, 1}, {4, 2}, {4, 3}, {4, 4}, {4, 5}, {4, 6}, {4, 7},
  {5, 0}, {5, 1}, {5, 2}, {5, 3}, {5, 4}, {5, 5}, {5, 6}, {5, 7},
  {6, 0}, {6, 1}, {6, 2}, {6, 3}, {6, 4}, {6, 5}, {6, 6}, {6, 7},
  {7, 0}, {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}, {7, 7}
};

int l_boot1[4][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6}};
int l_boot2[2][2] = {{1, 2}, {1, 7}};
int l_boot3[4][2] = {{2, 1}, {2, 4}, {2, 5}, {2, 7}};
int l_boot4[4][2] = {{3, 0}, {3, 4}, {3, 5}, {3, 7}};
int l_boot5[2][2] = {{4, 0}, {4, 7}};
int l_boot6[2][2] = {{5, 0}, {5, 7}};
int l_boot7[2][2] = {{6, 0}, {6, 7}};
int l_boot8[6][2] = {{7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}};

int r_boot1[4][2] = {{0, 1}, {0, 2}, {0, 3}, {0, 4}};
int r_boot2[2][2] = {{1, 0}, {1, 5}};
int r_boot3[4][2] = {{2, 0}, {2, 3}, {2, 4}, {2, 6}};
int r_boot4[4][2] = {{3, 0}, {3, 3}, {3, 4}, {3, 7}};
int r_boot5[2][2] = {{4, 0}, {4, 7}};
int r_boot6[2][2] = {{5, 0}, {5, 7}};
int r_boot7[2][2] = {{6, 0}, {6, 7}};
int r_boot8[6][2] = {{7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}};

int l_normal[26][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6},
  {1, 2}, {1, 7},
  {2, 1}, {2, 4}, {2, 5}, {2, 7},
  {3, 0}, {3, 4}, {3, 5}, {3, 7},
  {4, 0}, {4, 7},
  {5, 0}, {5, 7},
  {6, 0}, {6, 7},
  {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}
};

int l_normal2[26][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6},
  {1, 2}, {1, 7},
  {2, 1}, {2, 3}, {2, 4}, {2, 7},
  {3, 0}, {3, 3}, {3, 4}, {3, 7},
  {4, 0}, {4, 7},
  {5, 0}, {5, 7},
  {6, 0}, {6, 7},
  {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}
};


int l_happy[26][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6},
  {1, 2}, {1, 7},
  {2, 1}, {2, 7},
  {3, 0}, {3, 7},
  {4, 0}, {4, 3}, {4, 4}, {4, 7},
  {5, 0}, {5, 2}, {5, 5}, {5, 7},
  {6, 0}, {6, 7},
  {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}
};


int l_happy2[26][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6},
  {1, 2}, {1, 7},
  {2, 1}, {2, 7},
  {3, 0}, {3, 3}, {3, 4}, {3, 7},
  {4, 0}, {4, 2}, {4, 5}, {4, 7},
  {5, 0}, {5, 7},
  {6, 0}, {6, 7},
  {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}
};


int l_angry[29][2] = {{0, 2},
  {1, 1}, {1, 2}, {1, 3},
  {2, 1}, {2, 2}, {2, 3}, {2, 4},
  {3, 1}, {3, 2}, {3, 3}, {3, 4}, {3, 5},
  {4, 1}, {4, 2}, {4, 3}, {4, 4}, {4, 5}, {4, 6},
  {5, 2}, {5, 3}, {5, 4}, {5, 5}, {5, 6}, {5, 7},
  {6, 3}, {6, 4}, {6, 5}, {6, 6}
};

int l_angry2[18][2] = {{0, 2},
  {1, 1}, {1, 3},
  {2, 1}, {2, 4},
  {3, 1}, {3, 3}, {3, 5},
  {4, 1}, {4, 3}, {4, 4}, {4, 6},
  {5, 2}, {5, 7},
  {6, 3}, {6, 4}, {6, 5}, {6, 6}
};

int l_sleepy[32][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6},
  {1, 2}, {1, 7},
  {2, 1}, {2, 3}, {2, 3}, {2, 4}, {2, 5}, {2, 7},
  {3, 0}, {3, 4}, {3, 7},
  {4, 0}, {4, 3}, {4, 7},
  {5, 0}, {5, 2}, {5, 3}, {5, 4}, {5, 5}, {5, 7},
  {6, 0}, {6, 7},
  {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}
};

int l_sad[32][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6},
  {1, 2}, {1, 7},
  {2, 1}, {2, 7},
  {3, 0}, {3, 2}, {3, 3}, {3, 4}, {3, 5}, {3, 7},
  {4, 0}, {4, 3}, {4, 4}, {4, 7},
  {5, 0}, {5, 3}, {5, 4}, {5, 7},
  {6, 0}, {6, 3}, {6, 4}, {6, 7},
  {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}
};


int l_surprised[30][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6},
  {1, 2}, {1, 7},
  {2, 1}, {2, 3}, {2, 4}, {2, 7},
  {3, 0}, {3, 2}, {3, 5}, {3, 7},
  {4, 0}, {4, 2}, {4, 5}, {4, 7},
  {5, 0}, {5, 3}, {5, 4}, {5, 7},
  {6, 0}, {6, 7},
  {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}
};


int l_surprised2[26][2] = {{0, 3}, {0, 4}, {0, 5}, {0, 6},
  {1, 2}, {1, 7},
  {2, 1}, {2, 7},
  {3, 0}, {3, 3}, {3, 4}, {3, 7},
  {4, 0}, {4, 3}, {4, 4}, {4, 7},
  {5, 0}, {5, 7},
  {6, 0}, {6, 7},
  {7, 1}, {7, 2}, {7, 3}, {7, 4}, {7, 5}, {7, 6}
};


void loop() {
  // put your main code here, to run repeatedly
  normal();
  normal();
  normal();
  normal();
  normal();
  normal();
  normal();
  
  happy();
  happy();
  happy();
  happy();
  happy();
  happy();
  happy();
  
  angry();
  angry();
  angry();
  angry();
  angry();
  angry();
  angry();

  sleepy();
  sleepy();
  sleepy();
  sleepy();
  sleepy();

  sad();
  sad();
  sad();
  sad();
  sad();
  sad();
  
  surprised();
  surprised();
  surprised();
  surprised();
  surprised();
  surprised();
  
}

void surprised() {
  for (int i = 0; i < 30; i++) {
    matrix.drawPixel(l_surprised[i][0], l_surprised[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
  for (int i = 0; i < 26; i++) {
    matrix.drawPixel(l_surprised2[i][0], l_surprised2[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
}

void sad() {
  for (int i = 0; i < 32; i++) {
    matrix.drawPixel(l_sad[i][0], l_sad[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
}

void sleepy() {
  for (int i = 0; i < 32; i++) {
    matrix.drawPixel(l_sleepy[i][0], l_sleepy[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
}

void angry() {
  for (int i = 0; i < 29; i++) {
    matrix.drawPixel(l_angry[i][0], l_angry[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
  for (int i = 0; i < 18; i++) {
    matrix.drawPixel(l_angry2[i][0], l_angry2[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
}

void happy() {
  for (int i = 0; i < 26; i++) {
    matrix.drawPixel(l_happy[i][0], l_happy[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
  for (int i = 0; i < 26; i++) {
    matrix.drawPixel(l_happy2[i][0], l_happy2[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
}

void normal() {
  for (int i = 0; i < 26; i++) {
    matrix.drawPixel(l_normal[i][0], l_normal[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
  for (int i = 0; i < 26; i++) {
    matrix.drawPixel(l_normal2[i][0], l_normal2[i][1], LED_ON);
  }
  matrix.writeDisplay();
  delay(500);
  matrix.clear();
}


void set_pixel() {
  matrix.drawPixel(0, 0, LED_ON);
  matrix.writeDisplay();  // write the changes we just made to the display
  delay(500);
}
