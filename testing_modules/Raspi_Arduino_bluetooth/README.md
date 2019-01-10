# pybluez installation
sudo apt-get install bluetooth libbluetooth-dev
sudo python3 -m pip install pybluez

# Ignore the below things, they are a part of old testing

# nothing happened with this i guess: sudo apt-get install -y bluez-obexd
# bluetooth control commands to connect to a new device
sudo bluetoothctl # use of sudo is must
agent on
pairable on
scan on
# find the BT thing you want, copy its address
scan off
pair <physical-addr>
# input pin
trust <physical-addr>
connect <physical-addr>
exit

# after restart
echo -e "connect 98:D3:31:F5:B9:E7\nquit" | bluetoothctl



# installing bluez in raspi
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.49.tar.xz
tar xvf bluez-5.49.tar.xz
cd bluez-5.49
./configure
        # for dependency errors: 
        sudo apt-get install libglib2.0-dev libdbus-1-dev libudev-dev libical-dev libreadline-dev
make
sudo make install
sudo reboot


