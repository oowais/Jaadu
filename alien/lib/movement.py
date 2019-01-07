import logging
import threading
import time

from lib.globals import LOGGER_TAG


class Karma(threading.Thread):
    def __init__(self, listen_queue):
        super(Karma, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.q = listen_queue

    def run(self):
        self.logger.info("Starting off Movement Listener ...")
        while True:
            if self.q.empty():
                time.sleep(1)
            else:
                item = self.q.get()
                self.logger.debug("[Walker] Received item : {}".format(item))
