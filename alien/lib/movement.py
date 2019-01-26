import logging
import threading
import time

from lib.globals import LOGGER_TAG
from lib.walk_pigpio_controller import PIGPIOController


class Karma(threading.Thread):
    def __init__(self):
        super(Karma, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.pigpio_control = PIGPIOController()
        self.walking_command = None
        self.current_command = None

    def stop(self):
        self.pigpio_control.cleanup()

    def hello(self):
        self.pigpio_control.control_pins(control_values=[("left_foot", 1000), ("right_foot", 2500)])
        for i in range(3):
            self.pigpio_control.control_pins(control_values=[("right_leg", 2000)], delay=0.3)
            self.pigpio_control.control_pins(control_values=[("right_leg", 2500)], delay=0.3)
        self.default_position()
        if self.walking_command == "hello":
            self.walking_command = None

    def forward(self):
        self.pigpio_control.control_pins(control_values=[("left_foot", 1833), ("right_foot", 944)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_leg", 2166), ("right_leg", 1500)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_foot", 611), ("right_foot", 2500)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_leg", 1166), ("right_leg", 2500)], delay=0.5)
        self.default_position()

    def turn_right(self):
        self.pigpio_control.control_pins(control_values=[("left_foot", 611), ("right_foot", 2500)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_leg", 1166), ("right_leg", 1500)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_foot", 1833), ("right_foot", 944)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_leg", 2166), ("right_leg", 2500)], delay=0.5)
        self.default_position()

    def turn_left(self):
        self.pigpio_control.control_pins(control_values=[("left_foot", 611), ("right_foot", 2500)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_leg", 2166), ("right_leg", 2500)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_foot", 1833), ("right_foot", 944)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_leg", 1166), ("right_leg", 1500)], delay=0.5)
        self.default_position()

    def default_position(self):
        self.pigpio_control.control_pins(control_values=[("left_leg", 1166), ("right_leg", 2500)], delay=0.5)
        self.pigpio_control.control_pins(control_values=[("left_foot", 1833), ("right_foot", 944)], delay=0.5)

    def set_walking_command(self, command):
        if command in ["hello", "forward", "right", "left", "stop"]:
            self.walking_command = command
        if self.current_command != None and self.walking_command != self.current_command:
            self.pigpio_control.stop_pigpio_control()

    def run(self):
        self.logger.info("Starting off Movement Listener ...")
        self.default_position()
        while True:
            if self.walking_command is None:
                self.stop()
                time.sleep(1)
            else:
                self.pigpio_control.pin_setup()
                self.pigpio_control.start_pigpio_control()
                self.current_command = self.walking_command
                command = self.current_command
                self.logger.debug("[Walker] Received command : {}".format(command))
                if command == "hello":
                    self.hello()
                elif command == "forward":
                    self.forward()
                elif command == "right":
                    self.turn_right()
                elif command == "left":
                    self.turn_left()
                elif command == "stop":
                    self.walking_command = None
                    self.default_position()
                else:
                    self.logger.error("Command {} received doesn't match with "
                                      "pre-loaded commands, ignoring...".format(command))
                self.current_command = None
