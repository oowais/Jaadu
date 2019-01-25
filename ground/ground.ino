#include <SoftwareSerial.h>
#include "gateway.h"

// All connections
// Crocodile
byte crocodile_us_trigger = 7;
byte crocodile_us_echo = 8;
byte crocodile_led_din = 9;
// Plant
byte plant_us_trigger = 2;
byte plant_us_echo = 3;
byte plant_led_din = 4;
// Bluetooth
byte rx_conn = 5;
byte tx_conn = 6;

// Gateways to Monitor
Gateway *activatedGateway = NULL;
Gateway *lastWeKnow = NULL;
Gateway crocodile = Gateway('c', crocodile_us_echo, crocodile_us_trigger, crocodile_led_din, 8, &activatedGateway);
Gateway plant = Gateway('p', plant_us_echo, plant_us_trigger, plant_led_din, 8, &activatedGateway);

SoftwareSerial neelaDanth(rx_conn, tx_conn);

void setup() {
  Serial.begin(9600);
  while (!Serial) {;}

  neelaDanth.begin(9600);
  crocodile.setup();
  plant.setup();
}

void loop()
{
  crocodile.getDistanceTrigger();
  plant.getDistanceTrigger();
  crocodile.lightGateway();
  plant.lightGateway();
  if (lastWeKnow != activatedGateway) {
    lastWeKnow = activatedGateway;
    if (&crocodile == activatedGateway) {
      // Send signal for crocodile gate trigger
      neelaDanth.print(crocodile.getUniqueCharID());
    } else if (&plant == activatedGateway) {
      // Send signal for plant gate trigger
      neelaDanth.print(plant.getUniqueCharID());
    } else if (NULL == activatedGateway) {
      // Signifying nothing triggered signal
      neelaDanth.print("x");
    }
  }
}
