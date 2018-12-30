import logging
import threading
import time

from lib.globals import LOGGER_TAG


class Emotioner(threading.Thread):
    def __init__(self, listen_queue, info_src):
        super(Emotioner, self).__init__()
        self.logger = logging.getLogger(LOGGER_TAG)
        self.info_src = info_src
        self.q = listen_queue

    def run(self):
        self.logger.info("Starting off Emotion Manipulator ...")
        while True:
            if self.q.empty():
                time.sleep(1)
            else:
                item = self.q.get()
                self.logger.debug("[Emotioner] Received item : {}".format(item))
