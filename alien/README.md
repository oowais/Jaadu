# Alien

The central controller for all the different individual components.

## Wiring

Pin 2 - 5V VCC

Pin 6, Pin 30 - GND

#### Right eye
Pin 16 - GPIO 23 - SDA

Pin 18 - GPIO 24 - SCL

#### Left eye
Pin 3 - GPIO 2 / I2C1 SDA - SDA

Pin 5 - GPIO 3 / I2C1 SCL - SCL

#### Led Strip
Pin 12 - GPIO 18

#### Walking Pins
left_leg - pin 36 -  GPIO 16

left_foot - pin 38 -  GPIO 20

right_leg  - pin 22 - GPIO 25

right_foot - pin 37 - GPIO 26

## Installation
Run the [script](../scripts/) to complete installation of the alien package inside RasPI.
Starts the Alien program automatically as a service on the RasPI.

## Some things to take care
Changes in __lib/globals.py : __
* __EXTERNAL_BROKER_HOST__ needs to point to the IP address of the MQTT Broker.
* __EXTERNAL_BROKER_PORT__ needs to be changed if the Broker listens at a different port (1883 is default)
* __WALKING_PINS__ are RasPI GPIO pin numbers and need to be changed if the connection is made different from as given.
* __MOVE_CONTROL_VALUES__ are experimental values. The exact values change depending on how the Alien legs are screwed in.
Experiments can be done using [this](../testing_modules/pigpio_test/servo_demo.py).
* __WALKING_PINS__ has GPIO pin numbers. Need to be changed if using different connection.
* __HAND_BLUETOOTH_MAC__ according to the MAC of the powerhand Bluetooth device.
* __GROUND_BLUETOOTH_MAC__ according to the MAC of the ground connected Bluetooth device.
* __LED_STRIP_PIN__ is the GPIO pin number. Change if using different connections.
* __NUM_PIXELS_USED__ change according to number of LEDs in the strip used in Alien.


Changes in __mqtt_topic_mappings.json : __

Change the topic on which the emotions are sent by the other entities in the terrarium and unique key we will be using to track those emotions.
