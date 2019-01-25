#include "gateway.h"
#include "Arduino.h"

Gateway::Gateway(char uniqueID, byte echoPin, byte trigPin, byte ledStripPin,
                 byte numLED, Gateway **activatedGateway)
{
  this->_uniqueID = uniqueID;
  this->_echoPin = echoPin;
  this->_trigPin = trigPin;
  this->_activatedGateway = activatedGateway;
  this->_breathCount = 0;
  this->_strip = Adafruit_NeoPixel(numLED, ledStripPin, NEO_GRB + NEO_KHZ800);
}

void Gateway::setup() {
  if (0 != _echoPin) {
    pinMode(this->_echoPin, INPUT);
  }
  if (0 != _trigPin) {
    pinMode(this->_trigPin, OUTPUT);
  }

  this->_strip.begin();
  this->_strip.show();
}

void Gateway::_breatheLEDs(byte r, byte g, byte b)
{
  float MaximumBrightness = 255;
  float SpeedFactor = 0.01;

  if (_breathCount == 65536) {
    _breathCount = 0;
  }
  
  float intensity = MaximumBrightness /2.0 * (1.0 + sin(SpeedFactor * _breathCount));
  _strip.setBrightness(intensity);
  for (int l = 0; l < _strip.numPixels(); l++) {
    _strip.setPixelColor(l, r, g, b);
  }
  _strip.show();
  delay(5);
  
  _breathCount++;
}

char Gateway::getUniqueCharID()
{
  return _uniqueID;
}

void Gateway::lightGateway()
{
  if (0 == _strip.getPin())
    return;

  if (NULL == *_activatedGateway) {
    // No gateways are activated at the moment, show blue color
    _breatheLEDs(0, 0, 255);
  } else if (this != *_activatedGateway) {
    // We are in deactivated state, show red color
    _breatheLEDs(255, 0, 0);
  } else if (this == *_activatedGateway) {
    // We are in activated state, show green color
    _breatheLEDs(0, 255, 0);
  }
}

void Gateway::getDistanceTrigger()
{
  if (0 == _echoPin && 0 == _trigPin)
    return;

  if (NULL != *_activatedGateway && this != *_activatedGateway)
    return;

  int distance, duration;
  digitalWrite(_trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(_trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(_trigPin, LOW);
  duration = pulseIn(_echoPin, HIGH);
  distance = duration * 0.034 / 2;
  if (distance >= RANGE_MIN && distance <= RANGE_MAX) {
    if (NULL == *_activatedGateway)
      *_activatedGateway = this;
  } else if (*_activatedGateway == this) {
    *_activatedGateway = NULL;
  }
}
