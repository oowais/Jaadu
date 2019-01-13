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
        self.hand_blue_sock = None
        self.connect()

    def connect(self):
        self.hand_blue_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            self.hand_blue_sock.connect((HAND_BLUETOOTH_MAC, HAND_BLUETOOTH_PORT))
        except IOError:
            self.logger.error('Unable to connect to {}'.format(HAND_BLUETOOTH_MAC))
            self.hand_blue_sock = None
        else:
            self.logger.info('Connected to Hand Bluetooth Module..!')

    def run(self):
        self.logger.info("Starting off Bluetooth instruction receiver ...")
        while True:
            try:
                if self.hand_blue_sock:
                    data = self.hand_blue_sock.recv(1).decode()
                else:
                    raise bluetooth.btcommon.BluetoothError
            except bluetooth.btcommon.BluetoothError:
                self.hand_blue_sock = None
                self.connect()
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
                
