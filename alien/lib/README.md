## Wiring

Pin 2 - 5V VCC
Pin 6 - GND

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

## Movement servo values
| Left foot  | Angle | pigpio width |  |Right foot  | Angle | pigpio width |
| :----------- | :-------: | :------: | -- | :----------- | :-------: | :------: |
| up | 10  | 500 | | up | 180  | 2500 |
| straight | 45 | 900 | | straight | 130 | 1944 |
| down | 120 | 1900 | | down | 40 | 944 |

| Left leg  | Angle | pigpio width | | Right leg  | Angle | pigpio width |
| :----------- | :-------: | :------: | -- | :----------- | :-------: | :------: |
| center | 60 | 1066 | | center | 180 | 2500 |
| extreme | 150 | 2166 | | extreme | 90 | 1500 |
