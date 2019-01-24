import logging
import threading
import time

from lib.globals import LOGGER_TAG
from lib.walk_gpio_controller import GPIOController


class Karma(threading.Thread):
    def __init__(self):
        super(Karma, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.gpio_control = GPIOController()
        self.walking_command = None
        self.current_command = None

    def stop(self):
        self.gpio_control.stop_pwm_pins()
        self.gpio_control.cleanup()

    def hello(self):
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(45)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(180))])
        for i in range(2):
            self.gpio_control.control_pins(control_values=[("right_leg", GPIOController.cnvt_angle_to_dc(150))], delay=0.2)
            self.gpio_control.control_pins(control_values=[("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.2)
        self.default_position()

    def forward(self):
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(120)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(40))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(150)),
                                       ("right_leg", GPIOController.cnvt_angle_to_dc(90))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(10)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(60)),
                                       ("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.default_position()

    def turn_right(self):
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(10)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(60)),
                                       ("right_leg", GPIOController.cnvt_angle_to_dc(90))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(120)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(40))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(150)),
                                       ("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.default_position()

    def turn_left(self):
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(45)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(130))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(150)),
                                       ("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(120)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(40))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(60)),
                                       ("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.default_position()

    def default_position(self):
        self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(60)),
                                       ("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(120)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(40))], delay=0.3)

    def set_walking_command(self, command):
        if command in ["hello", "forward", "right", "left", "stop"]:
            self.walking_command = command
        if self.current_command != None and self.walking_command != self.current_command:
            self.gpio_control.stop_gpio_control()


    def run(self):
        self.logger.info("Starting off Movement Listener ...")
        self.default_position()
        while True:
            if self.walking_command == None:
                self.stop()
                time.sleep(1)
            else:
                self.gpio_control.pin_setup()
                self.gpio_control.start_gpio_control()
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
