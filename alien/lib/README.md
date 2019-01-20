## Eye emotions 
### Enable busnum 3 for 2nd LED
[Reference](https://www.instructables.com/id/Raspberry-PI-Multiple-I2c-Devices/)
```
cd /boot
sudo nano config.txt
dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=1
```
Save config.txt and reboot Raspi


It will create an aditional i2c bus (bus 3) on GPIO 23 as SDA and GPIO 24 as SCL (GPIO 23 and 24 is defaults)
