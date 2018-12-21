/*
  The circuit:
  - analog 1: z-axis
  - analog 2: y-axis
  - analog 3: x-axis
  Possble Case-
  - analog 0/GND: ground
  - analog 4/5V: vcc
*/

//const int groundpin = A0;
//const int powerpin = A4;
const int xPin = A3;
const int yPin = A2;
const int zPin = A1;

int xInit;
int yInit;
int zInit;

int xRead;
int yRead;
int zRead;

void setup() {
  Serial.begin(9600);

  // Provide ground and power by using the analog inputs as normal digital pins.
  // This makes it possible to directly connect the breakout board to the
  // Arduino. If you use the normal 5V and GND pins on the Arduino,
  // you can remove these lines.
  //  pinMode(groundpin, OUTPUT);
  //  pinMode(powerpin, OUTPUT);
  //  digitalWrite(groundpin, LOW);
  //  digitalWrite(powerpin, HIGH);

  //Get initial value of sensors
  xInit = analogRead(xPin);
  yInit = analogRead(yPin);
  zInit = analogRead(zPin);
}

void loop() {

  xRead = analogRead(xPin) ;
  yRead = analogRead(yPin) ;
  zRead = analogRead(zPin) ;

  if (zRead < 330)
    Serial.println("Hand facing up");
  else if (zRead > 400)
    Serial.println("Hand facing down");

  if (xRead > 300 && xRead < 380 && yRead > 290 && yRead < 370)
    Serial.println("Center");
  else {
    if (xRead < 300)
      Serial.println("Left");
    else if (xRead > 380)
      Serial.println("Right");

    if (yRead < 290)
      Serial.println("Back");
    else if (yRead > 370)
      Serial.println("Forward");
  }
  Serial.println();
  delay(300);
}
