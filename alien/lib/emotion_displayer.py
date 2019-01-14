import logging
import threading
import time
from Adafruit_LED_Backpack import Matrix8x8

from lib.globals import LOGGER_TAG


class Maya(threading.Thread):
    def __init__(self, listen_queue, info_src):
        super(Maya, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.info_src = info_src
        self.q = listen_queue

    def happy_expression(self, t):
        pass

    def sad_expression(self, t):
        pass

    def angry_expression(self, t):
        pass

    def sleepy_expression(self, t):
        pass

    def surprised_expression(self, t):
        pass

    def walking_expression(self, t):
        pass

    def run(self):
        command_map = {"happy" : self.happy_expression,
                       "sad" : self.sad_expression,
                       "angry" : self.angry_expression,
                       "sleepy" : self.sleepy_expression,
                       "surprised" : self.surprised_expression,
                       "walking" : self.walking_expression}
        self.logger.info("Starting off Emotion Manipulator ...")
        while True:
            if self.q.empty():
                time.sleep(1)
            else:
                item = self.q.get()
                self.logger.debug("[Emotioner] Received item : {}".format(item))
                command, times = item
                if command in command_map:
                    command_map[command](t=times)
                else:
                    self.logger.error("Command {} received doesn't match with "
                            "pre-loaded commands, ignoring...".format(command))
