#ifndef Gateway_h
#define Gateway_h

#include "Arduino.h"
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define RANGE_MIN 10
#define RANGE_MAX 16

class Gateway
{
  private:
    byte _echoPin;
    byte _trigPin;
    Adafruit_NeoPixel _strip;
    Gateway **_activatedGateway;
    char _uniqueID;
    unsigned int _breathCount;
    void _breatheLEDs(byte r, byte g, byte b);
  public:
    Gateway(char uniqueID, byte echoPin = 0, byte trigPin = 0, byte ledStripPin = 0,
            byte numLED = 0, Gateway **activatedGateway = NULL);
    void setup();
    char getUniqueCharID();
    void lightGateway();
    void getDistanceTrigger();
};

#endif
