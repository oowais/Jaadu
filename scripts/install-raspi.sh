#!/bin/bash

sudo apt-get update -y

# Basic requirements
sudo apt-get install git python3-pip build-essential python3-dev -y

# For Bluetooth
sudo apt-get install libbluetooth3 -y

# For LED Strips
sudo raspi-config nonint do_spi 0

# For LED Matrix
sudo raspi-config nonint do_i2c 0
sudo apt-get install python3-smbus i2c-tools python3-pil -y
git clone http://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack; sudo python3 setup.py install
cd ..; sudo rm -rf Adafruit_Python_LED_Backpack
sudo sed -i "/dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=1/d" /boot/config.txt
sudo sh -c "echo 'dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=1' >> /boot/config.txt"

# For pigpio, controlling servo movements
sudo apt-get install pigpio python3-pigpio
sudo systemctl enable pigpiod

sudo rm -rf /home/pi/brain/

mkdir /home/pi/brain; cd /home/pi/brain
git init; git config core.sparseCheckout true
git remote add -f origin https://github.com/oowais/MCP-Alien.git
echo "alien/*" > .git/info/sparse-checkout
git checkout master

pip3_loc=`which pip3`
python3_loc=`which python3`

cd alien; eval $pip3_loc "install -r requirements.txt"

# Set the I2C address in the code
i2c_addr=`i2cdetect -y 1 | grep -Po " [0-9a-f][0-9a-f]" | tr -d ' ' | head -1`
sed -i "s/EYE_I2C_ADDRESS = 0x70/EYE_I2C_ADDRESS = 0x$i2c_addr/g" lib/globals.py

echo -n "Do you wish to setup backdoor access for Alien [y/n] : "
while read -e -t 0.1; do : ; done
read ans
if [ $ans == "y" ]; then
  echo "Enter users or enter 'exit' (without quotes) to stop ..."
  while :
  do
    echo -e "\nEnter Credentials for USER --- "
    echo -n "User ID : "
    while read -e -t 0.1; do : ; done
    read userid
    if [ $userid == "exit" ]; then
      break
    fi
    echo -n "PassWord : "
    while read -e -t 0.1; do : ; done
    read -s passwd
    salt=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 20 | head -n 1)
    echo -e "\n... Generated a random 20 character salt : $salt"
    hasher=$(echo -n "$salt$userid$passwd" | sha256sum | awk '{print $1}')
    echo "$userid:$salt:$hasher" >> auth_info
  done
fi

echo "[Unit]" > alien.service
echo "Description=Alien" >> alien.service
echo "After=network.target" >> alien.service
echo "" >> alien.service
echo "[Service]" >> alien.service
echo "Type=idle" >> alien.service
echo "Restart=always" >> alien.service
echo "StandardOutput=inherit" >> alien.service
echo "StandardError=inherit" >> alien.service
echo "User=root" >> alien.service
echo "WorkingDirectory=/home/pi/brain/alien" >> alien.service
echo "ExecStart=$python3_loc main.py -s" >> alien.service
echo "" >> alien.service
echo "[Install]" >> alien.service
echo "WantedBy=multi-user.target" >> alien.service

sudo cp alien.service /etc/systemd/system/alien.service
sudo systemctl daemon-reload
sudo systemctl enable alien.service

echo -e "\n... All setup, rebooting the system"

sudo reboot
