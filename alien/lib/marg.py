import logging
import threading
import time

from lib.globals import LOGGER_TAG


class HandCoordinator(threading.Thread):
    def __init__(self, talk_queue):
        super(HandCoordinator, self).__init__()
        self.logger = logging.getLogger()
        self.q = talk_queue

    def run(self):
        self.logger.info("Starting off BLE instruction receiver ...")
        while True:
            pass
