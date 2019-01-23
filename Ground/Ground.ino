#include <Arduino_FreeRTOS.h>
#include <SoftwareSerial.h>
#include "Gateway.h"

// FreeRTOS tasks
void TaskUltraSonicSensorOneRead(void *pvParameters);
void TaskUltraSonicSensorTwoRead(void *pvParameters);
void TaskLEDStripOneDisplay(void *pvParameters);
void TaskLEDStripTwoDisplay(void *pvParameters);
void TaskBluetoothComm(void *pvParameters);

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
Gateway crocodile;
Gateway plant;

Gateway *activatedGateway;

void setup() {
  Serial.begin(9600);

  activatedGateway = NULL;

  SoftwareSerial neelaDanth(rx_conn, tx_conn);
  neelaDanth.begin(9600);

  crocodile = Gateway(crocodile_us_echo, crocodile_us_trigger, crocodile_led_din, 2, &activatedGateway);
  plant = Gateway(plant_us_echo, plant_us_trigger, plant_led_din, 2, &activatedGateway);

  xTaskCreate(TaskUltraSonicSensorOneRead, (const portCHAR *) "USonicReadOne", 128, NULL, 1, NULL);
  xTaskCreate(TaskUltraSonicSensorTwoRead, (const portCHAR *) "USonicReadTwo", 128, NULL, 1, NULL);
  xTaskCreate(TaskLEDStripOneDisplay, (const portCHAR *) "LEDStripLightOne", 128, NULL, 1, NULL);
  xTaskCreate(TaskLEDStripTwoDisplay, (const portCHAR *) "LEDStripLightTwo", 128, NULL, 1, NULL);
  xTaskCreate(TaskBluetoothComm, (const portCHAR *) "BluetoothComm", 128, NULL, 1, NULL);
}

void loop() {}

void TaskUltraSonicSensorOneRead( void *pvParameters __attribute__((unused)) )
{
  for (;;) {
    crocodile.getDistanceTrigger();
    vTaskDelay(1);
  }
}

void TaskUltraSonicSensorTwoRead( void *pvParameters __attribute__((unused)) )
{
  for (;;) {
    plant.getDistanceTrigger();
    vTaskDelay(1);
  }
}

void TaskLEDStripOneDisplay( void *pvParameters __attribute__((unused)) )
{
  for (;;) {
    crocodile.lightGateway();
    vTaskDelay(1);
  }
}

void TaskLEDStripTwoDisplay( void *pvParameters __attribute__((unused)) )
{
  for (;;) {
    plant.lightGateway();
    vTaskDelay(1);
  }
}

void TaskBluetoothComm( void *pvParameters __attribute__((unused)) )
{
  Gateway *lastWeKnow = NULL;
  for (;;) {
    byte c;
    if (neelaDanth.available() > 0) {
      c = neelaDanth.read();
      if (c == "s") {
        if (activatedGateway == NULL) {
          neelaDanth.print("1");
        } else {
          neelaDanth.print("0");
        }
      }

    } else if (lastWeKnow != activatedGateway) {
      lastWeKnow = activatedGateway;
      if (&crocodile == *activatedGateway)
        neelaDanth.print("c");
      else if (&plant == *activatedGateway)
        neelaDanth.print("p");
    }
    vTaskDelay(1);
  }
}
