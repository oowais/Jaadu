## Prerequisites
Enable i2c and spi interface(if required) in raspi-config from [here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

> spi not required for Adafruit library(as of now).


Then install the following:
`sudo apt-get install -y python-smbus`
`sudo apt-get install -y i2c-tools`

Test if i2c is enabled or not  
`sudo i2cdetect -y 1`

Test if spi interface  
`ls -l /dev/spidev*`

> Should see 2 devices


## Using Adafruit library to use Adafruit backpack
[Github Link](https://github.com/adafruit/Adafruit_Python_LED_Backpack) 
```
sudo apt-get update
sudo apt-get install -y git build-essential python3-dev python3-smbus python-imaging python3-pip python3-pil


git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack
sudo python3 setup.py install
```
Then run eye.py using  
supo python3 eye.py

> More eye expression to be added.

