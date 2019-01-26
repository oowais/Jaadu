import logging
import threading
import time

from lib.globals import LOGGER_TAG
import lib.emotions_library


class EmotionsDisplayer(threading.Thread):
    def __init__(self, name):
        super(EmotionsDisplayer, self).__init__(name=name)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.execute_command = None
        self.current_command = None
        self.module_up = False
        self.command_mappings = {"startup": self.startup,
                                 "normal": self.normal,
                                 "happy": self.happy,
                                 "sad": self.sad,
                                 "angry": self.angry,
                                 "sleepy": self.sleepy,
                                 "surprised": self.surprised,
                                 "lowpower": self.low_power,
                                 "hungry" : self.angry,
                                 "relaxed" : self.happy,
                                 "neutral" : self.sleepy,
                                 "scan" : self.scan,
                                 "peaceful" : self.sleepy
                                 }

    def set_emotion_command(self, command):
        if command in self.command_mappings.keys():
            self.execute_command = command
            self.logger.debug("Changing to emotion : {}".format(command))

    def execute_emotion(self, commands_loop):
        while True:
            for item in commands_loop:
                if self.execute_command == self.current_command:
                    eval(item)
                else:
                    return

    def run(self):
        while True:
            if not self.module_up:
                self.module_setup()
            else:
                self.current_command = self.execute_command
                self.command_mappings.get(self.current_command)()

    # Methods below hould be overriden in derived class
    def module_setup(self):
        pass

    def startup(self):
        pass

    def normal(self):
        pass

    def happy(self):
        pass

    def sad(self):
        pass

    def angry(self):
        pass

    def sleepy(self):
        pass

    def surprised(self):
        pass

    def low_power(self):
        pass

    def scan(self):
        pass
