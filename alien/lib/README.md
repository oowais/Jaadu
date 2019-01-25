## Wiring

Pin 2 - 5V VCC
Pin 6 - GND

Right eye
Pin 16 - GPIO 23 - SDA
Pin 18 - GPIO 24 - SCL

Left eye
Pin 3 - GPIO 2 / I2C1 SDA - SDA
Pin 5 - GPIO 3 / I2C1 SCL - SCL

Led Strip
Pin 10 - GPIO 15

WALKING_PINS
left_leg   GPIO 16
left_foot  GPIO 20
right_leg  GPIO 25
right_foot GPIO 26

## Movement servo values
| Left foot  | Angle | pigpio width |  |Right foot  | Angle | pigpio width |
| :----------- | :-------: | :------: | -- | :----------- | :-------: | :------: |
| up | 10  | 611 | | up | 180  | 2500 |
| straight | 45 | 1000 | | straight | 130 | 1944 |
| down | 120 | 1833 | | down | 40 | 944 |

| Left leg  | Angle | pigpio width | | Right leg  | Angle | pigpio width |
| :----------- | :-------: | :------: | -- | :----------- | :-------: | :------: |
| center | 60 | 1166 | | center | 180 | 2500 |
| extreme | 150 | 2166 | | extreme | 90 | 1500 |
