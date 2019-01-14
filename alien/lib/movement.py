import logging
import threading
import time

from lib.globals import LOGGER_TAG, WALKING_PINS
from lib.gpio_controller import GPIOController


class Karma(threading.Thread):
    def __init__(self, listen_queue):
        super(Karma, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.q = listen_queue
        self.gpio_control = GPIOController(pin_info=WALKING_PINS)

    def stop(self):
        self.gpio_control.stop_pwm_pins()

    def hello(self, n):
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(50)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(180))])
        for i in range(n):
            self.gpio_control.control_pins(control_values=[("right_leg", GPIOController.cnvt_angle_to_dc(150))], delay=0.2)
            self.gpio_control.control_pins(control_values=[("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.2)

    def forward(self, n):
        for i in range(n):
            self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(150)),
                                           ("right_foot", GPIOController.cnvt_angle_to_dc(30))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(180)),
                                           ("right_leg", GPIOController.cnvt_angle_to_dc(90))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(10)),
                                           ("right_foot", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(100)),
                                           ("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.default_position()

    def turn_right(self, n):
        for i in range(n):
            self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(50)),
                                           ("right_foot", GPIOController.cnvt_angle_to_dc(130))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(100)),
                                           ("right_leg", GPIOController.cnvt_angle_to_dc(90))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(150)),
                                           ("right_foot", GPIOController.cnvt_angle_to_dc(30))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(180)),
                                           ("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
        self.default_position()

    def turn_left(self, n):
        for i in range(n):
            self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(50)),
                                           ("right_foot", GPIOController.cnvt_angle_to_dc(130))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(180)),
                                           ("right_leg", GPIOController.cnvt_angle_to_dc(180))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(150)),
                                           ("right_foot", GPIOController.cnvt_angle_to_dc(30))], delay=0.3)
            self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(100)),
                                           ("right_leg", GPIOController.cnvt_angle_to_dc(90))], delay=0.3)
        self.default_position()

    def default_position(self):
        self.gpio_control.control_pins(control_values=[("left_leg", GPIOController.cnvt_angle_to_dc(100)),
                                       ("right_leg", GPIOController.cnvt_angle_to_dc(180))])
        self.gpio_control.control_pins(control_values=[("left_foot", GPIOController.cnvt_angle_to_dc(150)),
                                       ("right_foot", GPIOController.cnvt_angle_to_dc(30))])

    def run(self):
        self.logger.info("Starting off Movement Listener ...")
        self.default_position()
        while True:
            if self.q.empty():
                time.sleep(1)
            else:
                item = self.q.get()
                self.logger.debug("[Walker] Received item : {}".format(item))
                command, times = item
                if command == "hello":
                    self.hello(n=times)
                elif command == "forward":
                    self.forward(n=times)
                elif command == "right":
                    self.turn_right(n=times)
                elif command == "left":
                    self.turn_left(n=times)
                else:
                    self.logger.error("Command {} received doesn't match with "
                            "pre-loaded commands, ignoring...".format(command))
            self.stop()
