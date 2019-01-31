# Ground Controller

Arduino code used to receive triggers from the Gateways and signal via Bluetooth to the main Alien. The Alien receives the trigger and translates the emotion for the entity in the terrarium corresponding to the Gateway.

Each Gateway has a __LED Strip__ (breathing lights showing Gateway state) and an __UltraSonic sensor__.

## Wiring
* As defined in the [code](./ground.ino)
* For Bluetooth :
  * RX (on bluetooth) :arrow_right: tx_conn (on Arduino)
  * TX (on bluetooth) :arrow_right: rx_conn (on Arduino)
  * VCC connected to 3.3V OUT.

## Gateway States

* __Neutral :__ None of the Gateways are activated. LED Strips display BLUE color.
* __Activated :__  The UltraSonic sensor is triggered when some obstruction is detected in front of the gateway. (10-16 cms range). The LED Strips corresponding to the Gateway turn into GREEN color.
* __Deactivated :__ When one gateway is activated, others are in this state and doesn't trigger even when some object comes in the activation range. The LED Strips corresponding to the Gateway display RED color.

## Before Using

* If Pins used are different than given then have to change the corresponding pin numbers in **ground.ino**
* Each Gateway instance needs a separate character to be provided as uniqueID. These characters should correspond to triggers in the [receiver code](../alien/lib/ground_coordinator.py)
