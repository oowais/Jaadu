#include <Servo.h>

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
  Left foot             Right foot
  up-       10          up-       180
  straight- 45          straight- 130
  down-     120         down-     40

  Left leg              Right leg
  extreme-  150         extreme-  90
  centre-   60          centre-   180
*/

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
  moveParts(&leftLeg, &rightLeg, 60, 180);
  moveParts(&leftFoot, &rightFoot, 45, 180);
  //  delay(500);

  byte left = 50;
  byte right = 180;

  for (byte i = 0; i < 10 ; i++) {
    left += 7;
    right -= 5;
    moveParts(&leftFoot, &rightFoot, left, right, false, 70);
  }
  for (byte i = 0; i < 10 ; i++) {
    right -= 9;
    movePart(&rightFoot, right, false, 35);
  }
  delay(200);
}

void defaultPosition() {
  moveParts(&leftLeg, &rightLeg, 150, 180);//legs center
  moveParts(&leftFoot, &rightFoot, 120, 40);//feet down
}

void hello() {
  moveParts(&leftFoot, &rightFoot, 45, 180); //left foot straight, right foot up
  for (byte i = 0; i < 6; i++) { // move right leg back and forth
    movePart(&rightLeg, 150, false, 200);
    movePart(&rightLeg, 180, false, 200);
  }
}

void rotateLeft() {
  for (byte i = 0; i < 5; i++) {
    moveParts(&leftFoot, &rightFoot, 45, 130, false, 300); //feet straight
    moveParts(&leftLeg, &rightLeg, 150, 180, false, 300); //left leg extreme right leg centre
    moveParts(&leftFoot, &rightFoot, 120, 40, false, 300); //feet down
    moveParts(&leftLeg, &rightLeg, 60, 90, false, 300); //left leg centre, right leg extreme
  }
  defaultPosition();
  servoDetachAll();
}

void rotateRight() {
  for (byte i = 0; i < 5; i++) {
    moveParts(&leftFoot, &rightFoot, 45, 130, false, 300); //feet straight
    moveParts(&leftLeg, &rightLeg, 60, 90, false, 300); //left leg centre right lef extreme
    moveParts(&leftFoot, &rightFoot, 120, 40, false, 300); //feet down
    moveParts(&leftLeg, &rightLeg, 150, 180, false, 300); //left leg extreme, right leg center
  }
  defaultPosition();
  servoDetachAll();
}

void forward() {
  for (int i = 0; i < 5; i++) {
    moveParts(&leftFoot, &rightFoot, 120, 40, false, 300); //feet down
    moveParts(&leftLeg, &rightLeg, 150, 90, false, 300); //legs extreme
    moveParts(&leftFoot, &rightFoot, 10, 180, false, 300); //feet up
    moveParts(&leftLeg, &rightLeg, 60, 180, false, 300); //legs centre
  }
  defaultPosition();
  servoDetachAll();
}

void setup() {
  Serial.begin(9600);
  //  defaultPosition();
  hello();
  standUp();
  //  forward();
  //  rotateLeft();
  //  rotateRight();
  servoDetachAll();
}

void loop() {

}
