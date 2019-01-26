import bluetooth
import logging
import threading
import time

from lib.globals import LOGGER_TAG, HAND_BLUETOOTH_MAC, HAND_BLUETOOTH_PORT


class MargDarshan(threading.Thread):
    def __init__(self, talk_queue):
        super(MargDarshan, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.q = talk_queue
        self.module_up = False
        self.hand_blue_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def module_setup(self):
        while not self.module_up:
            try:
                self.hand_blue_sock.connect((HAND_BLUETOOTH_MAC, HAND_BLUETOOTH_PORT))
            except (IOError, bluetooth.btcommon.BluetoothError):
                self.logger.error('Unable to connect to Hand Bluetooth, Module not up ...')
                self.module_up = False
                self.hand_blue_sock.close()
                time.sleep(1)
            else:
                self.logger.info('Connected to Hand Bluetooth Module..!')
                self.module_up = True

    def run(self):
        self.logger.info("Starting off Bluetooth instruction receiver thread ...")
        while True:
            if not self.module_up:
                self.module_setup()
            try:
                data = self.hand_blue_sock.recv(1).decode()
            except bluetooth.btcommon.BluetoothError:
                self.module_up = False
                self.hand_blue_sock.close()
                continue

            if data == "f":
                self.q.put("hand forward")
            elif data == "r":
                self.q.put("hand right")
            elif data == "l":
                self.q.put("hand left")
            elif data == "u":
                self.q.put("hand look_up")
            elif data == "x":
                self.q.put("hand clear")
            else:
                self.logger.warning("Not able to recognize character.. Ignoring..")
