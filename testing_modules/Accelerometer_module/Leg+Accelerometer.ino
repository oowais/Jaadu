/*
  The circuit:
  - analog 1: z-axis
  - analog 2: y-axis
  - analog 3: x-axis
  Possble Case-
  - analog 0/GND: ground
  - analog 4/5V: vcc
*/
#include <Servo.h>

//Declaration Leg Variables

const byte leftLegPin = 5;
const byte leftFootPin = 6;
const byte rightLegPin = 10;
const byte rightFootPin = 11;

Servo leftLegS;
Servo rightLegS;
Servo leftFootS;
Servo rightFootS;

typedef struct servoControl {
  byte controlPin;
  Servo *motor;
} sControl;

sControl leftLeg = {leftLegPin, &leftLegS};
sControl rightLeg = {rightLegPin, &rightLegS};
sControl leftFoot = {leftFootPin, &leftFootS};
sControl rightFoot = {rightFootPin, &rightFootS};

//Declaration  Acceleormeter Module

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

// Starting Servo Functions

void servoAttach(sControl *s) {
  if (NULL != s) {
    if (false == (*(s->motor)).attached())
      (*(s->motor)).attach(s->controlPin);
  }
}

void servoDetach(sControl *s) {
  if (NULL != s) {
    if (true == (*(s->motor)).attached())
      (*(s->motor)).detach();
  }
}

void servoDetachAll() {
  servoDetach(&leftLeg);
  servoDetach(&rightLeg);
  servoDetach(&leftFoot);
  servoDetach(&rightFoot);
}

/*
  Foot Assignments:
  Left foot             Right foot
  up-       10          up-       180
  straight- 50          straight- 130
  down-     150         down-     30

  Left leg              Right leg
  extreme-  180         extreme-  90
  centre-   100         centre-   180
*/

//Controlling Foot Functions

void movePart(sControl *which, byte angleDesired = 0, boolean detachAfter = false,
              int delayTime = 1000) {
  servoAttach(which);
  byte angleNow = (*(which->motor)).read();
  boolean stepUp = (angleDesired > angleNow);
  /*while (angleNow != angleDesired) {
    angleNow += (stepUp) ? 1 : -1;
    (*(which->motor)).write(angleNow);
    delay(10);
    }*/
  (*(which->motor)).write(angleDesired);
  delay(delayTime);
  if (true == detachAfter)
    servoDetach(which);
}

void moveParts(sControl *part1, sControl *part2, byte part1DesiredAngle = 0,
               byte part2DesiredAngle = 0, boolean detachAfter = false,
               int delayTime = 1000) {
  servoAttach(part1);
  servoAttach(part2);
  byte angleNowPart1 = (*(part1->motor)).read();
  byte angleNowPart2 = (*(part2->motor)).read();
  (*(part1->motor)).write(part1DesiredAngle);
  (*(part2->motor)).write(part2DesiredAngle);
  delay(delayTime);
  if (true == detachAfter) {
    servoDetach(part1);
    servoDetach(part2);
  }
}

void standUp() {
  moveParts(&leftLeg, &rightLeg, 100, 180);
  moveParts(&leftFoot, &rightFoot, 50, 180);
  //  delay(500);

  byte left = 50;
  byte right = 180;

  for (byte i = 0; i < 10 ; i++) {
    left += 10;
    right -= 5;
    moveParts(&leftFoot, &rightFoot, left, right, false, 70);
  }
  for (byte i = 0; i < 5 ; i++) {
    right -= 20;
    movePart(&rightFoot, right, false, 70);
  }
  delay(200);
}

void defaultPosition() {

  //go till extreme ends, to make sure legs dont get stuck somehow
  //  moveParts(&leftLeg, &rightLeg, 180, 90);

  moveParts(&leftLeg, &rightLeg, 100, 180);//legs center
  moveParts(&leftFoot, &rightFoot, 150, 30);//feet down
}

void hello() {
  moveParts(&leftFoot, &rightFoot, 50, 180); //left foot straight, right foot up
  for (byte i = 0; i < 6; i++) { // move right leg back and forth
    movePart(&rightLeg, 150, false, 200);
    movePart(&rightLeg, 180, false, 200);
  }
}

void rotateLeft() {
  for (byte i = 0; i < 5; i++) {
    moveParts(&leftFoot, &rightFoot, 50, 130, false, 300); //feet straight
    moveParts(&leftLeg, &rightLeg, 180, 180, false, 300); //left leg extreme right leg centre
    moveParts(&leftFoot, &rightFoot, 150, 30, false, 300); //feet down
    moveParts(&leftLeg, &rightLeg, 100, 90, false, 300); //left leg centre, right leg extreme
  }
  defaultPosition();
  servoDetachAll();
}

void rotateRight() {
  for (byte i = 0; i < 5; i++) {
    moveParts(&leftFoot, &rightFoot, 50, 130, false, 300); //feet straight
    moveParts(&leftLeg, &rightLeg, 100, 90, false, 300); //left leg centre right lef extreme
    moveParts(&leftFoot, &rightFoot, 150, 30, false, 300); //feet down
    moveParts(&leftLeg, &rightLeg, 180, 180, false, 300); //left leg extreme, right leg center
  }
  defaultPosition();
  servoDetachAll();
}

void forward() {
  for (int i = 0; i < 5; i++) {
    moveParts(&leftFoot, &rightFoot, 150, 30, false, 300); //feet down
    moveParts(&leftLeg, &rightLeg, 180, 90, false, 300); //legs extreme
    moveParts(&leftFoot, &rightFoot, 10, 180, false, 300); //feet up
    moveParts(&leftLeg, &rightLeg, 100, 180, false, 300); //legs centre
  }
  defaultPosition();
  servoDetachAll();
}

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

  //Get initial value of accelerometer sensors
  xInit = analogRead(xPin);
  yInit = analogRead(yPin);
  zInit = analogRead(zPin);
  
  // Integrating Legs with Accelerometer 
  
  defaultPosition();
  
  delay(300);
  
  if (xRead > 300 && xRead < 380 && yRead > 290 && yRead < 370)
    {   Serial.println("Center");
    standup(); }
  else {
    if (xRead < 300)
      { Serial.println("Left");
      rotateLeft();}
    else if (xRead > 380)
      { Serial.println("Right");
        rotateRight();}
        
    if (yRead < 290)
      { Serial.println("Stay there");
        hello(); }
    else if (yRead > 370)
    {  Serial.println("Forward");
         forward(); }
         
  servoDetachAll();
  
}

void loop() {
  xRead = analogRead(xPin) ;
  yRead = analogRead(yPin) ;
  zRead = analogRead(zPin) ;
}
