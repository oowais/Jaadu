import board
import neopixel
import threading
import time

from lib.globals import (LOGGER_TAG, SHOW_EMOTION_FOR_TIME, NUM_PIXELS_USED, PIXEL_BRIGHTNESS)


class IllusionaryBrain:
    def __init__(self):
        super(IllusionaryBrain, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.execute_emotion = None
        self.current_command = None
        self.pixels = None
        self.module_up = False
        self.command_mappings = {"startup" : self.startup,
                                 "normal" : self.normal,
                                 "happy" : self.happy,
                                 "sad" : self.sad,
                                 "angry" : self.angry,
                                 "sleepy" : self.sleepy,
                                 "surprised" : self.surprised}

    def module_setup(self):
        if not self.module_up:
            self.pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS_USED,
                                            brightness=PIXEL_BRIGHTNESS,
                                            auto_write=False,
                                            pixel_order=neopixel.GRB)
            self.module_up = True
            self.set_emotion_command(command="startup")
        self.logger.info("Successfully setup the Brain Display Module to display emotions ...")

    def set_emotion_command(self, command):
        if command in self.command_mappings.keys():
            self.execute_emotion = command
            self.logger.debug("Changing to emotion : {}".format(command))
