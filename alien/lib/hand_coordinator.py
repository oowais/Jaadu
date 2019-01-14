import bluetooth
import logging
import threading
import time

from lib.globals import LOGGER_TAG, HAND_BLUETOOTH_MAC, HAND_BLUETOOTH_PORT


class MargDarshan(threading.Thread):
    def __init__(self, talk_queue):
        super(MargDarshan, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger()
        self.q = talk_queue
        self.module_up = False
        self.hand_blue_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def module_setup(self):
        while not self.module_up:
            try:
                self.hand_blue_sock.connect((HAND_BLUETOOTH_MAC, HAND_BLUETOOTH_PORT))
            except IOError:
                self.logger.error('Unable to connect to {}'.format(HAND_BLUETOOTH_MAC))
                self.module_up = False
            else:
                self.logger.info('Connected to Hand Bluetooth Module..!')
                self.module_up = True
            time.sleep(1)

    def run(self):
        self.logger.info("Starting off Bluetooth instruction receiver thread ...")
        while True:
            if not self.module_up:
                self.module_setup()
            try:
                data = self.hand_blue_sock.recv(1).decode()
            except bluetooth.btcommon.BluetoothError:
                self.module_up = False
                continue

            if data == "f":
                self.q.put("move forward 1")
            elif data == "r":
                self.q.put("move right 1")
            elif data == "l":
                self.q.put("move left 1")
            elif data == "u":
                self.q.put("move up 1")
            elif data == "x":
                self.q.put("move clear")
            else:
                self.logger.warning("Not able to recognize character.. Ignoring..")
