#!/bin/bash

sudo apt-get update -y
sudo apt-get install git python3-pip mosquitto libbluetooth-dev -y

sudo rm -rf /home/pi/brain/

mkdir /home/pi/brain; cd /home/pi/brain
git init; git config core.sparseCheckout true
git remote add -f origin https://github.com/oowais/MCP-Alien.git
echo "alien/*" > .git/info/sparse-checkout
git checkout master

pip3_loc=`which pip3`
python3_loc=`which python3`

cd alien; eval $pip3_loc "install -r requirements.txt"

echo -n "Do you wish to setup backdoor access for Alien [y/n] : "
read ans
if [ $ans == "y" ]
then
  echo "Enter users or press ctrl+c to stop ..."
  while :
  do
    echo -e "\nEnter Credentials for USER --- "
    echo -n "User ID : "
    read userid
    echo -n "PassWord : "
    read -s passwd
    salt=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 20 | head -n 1)
    echo "Generated a random 20 character salt : $salt"
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
echo "User=pi" >> alien.service
echo "WorkingDirectory=/home/pi/brain/alien" >> alien.service
echo "ExecStart=$python3_loc atman.py -s -lf alien.logs" >> alien.service
echo "" >> alien.service
echo "[Install]" >> alien.service
echo "WantedBy=multi-user.target" >> alien.service

sudo cp alien.service /etc/systemd/system/alien.service
sudo systemctl daemon-reload
sudo systemctl enable alien.service

sudo reboot
