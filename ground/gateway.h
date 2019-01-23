#ifndef Gateway_h
#define Gateway_h

#include "Arduino.h"
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define RANGE_MIN 10
#define RANGE_MAX 12

class Gateway
{
  private:
    byte _echoPin;
    byte _trigPin;
    Adafruit_NeoPixel _strip;
    Gateway **_activatedGateway;
  public:
    Gateway(byte echoPin = 0, byte trigPin = 0, byte ledStripPin = 0, byte numLED = 0, Gateway **activatedGateway = NULL);
    void lightGateway();
    void getDistanceTrigger();
};

#endif
