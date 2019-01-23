#include "gateway.h"

Gateway::Gateway(byte echoPin, byte trigPin, byte ledStripPin, byte numLED, Gateway **activatedGateway)
{
  if (0 != echoPin) {
    this->_echoPin = echoPin;
    pinMode(this->_echoPin, INPUT);
  }
  if (0 != trigPin) {
    this->_trigPin = trigPin;
    pinMode(this->_trigPin, OUTPUT);
  }

  this->_strip = Adafruit_NeoPixel(numLED, ledStripPin, NEO_GRB + NEO_KHZ800);
  this->_strip.show();

  this->_activatedGateway = activatedGateway;
}

void Gateway::lightGateway()
{
  if (0 == _strip.getPin())
    return;

  if (NULL == *_activatedGateway) {
    // No gateways are activated at the moment, show blue color
  } else if (this != *_activatedGateway) {
    // We are in deactivated state, show red color
  } else if (this == *_activatedGateway) {
    // We are in activated state, show green color
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
