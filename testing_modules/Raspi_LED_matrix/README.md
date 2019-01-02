## Prerequisites
Enable i2c and spi interface(if required) in raspi-config from [here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

`sudo apt-get install -y python-smbus`
`sudo apt-get install -y i2c-tools`

testing i2c enabed or not  
`sudo i2cdetect -y 1`

testing spi interface, should see 2 options  
`ls -l /dev/spidev*`



## Using Adafruit library to use Adafruit backpack
[Github Link](https://github.com/adafruit/Adafruit_Python_LED_Backpack) 
```
sudo apt-get update
sudo apt-get install -y git build-essential python-dev python-smbus python-imaging python-pip python-pil


git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack
sudo python setup.py install
```

