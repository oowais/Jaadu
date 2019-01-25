import time
import pigpio

from lib.globals import WALKING_PINS


class PIGPIOController:
    def __init__(self):
        self.pins_used = {}
        self.module_status = False
        self.ignore_control_values = False
        self.pi = None

    def stop_pigpio_control(self):
        self.ignore_control_values = True

    def start_pigpio_control(self):
        self.ignore_control_values = False

    def pin_setup(self):
        if not self.module_status:
            for name, pin in WALKING_PINS:
                self.pins_used[name] = pin
            self.pi = pigpio.pi()
            self.module_status = True

    def cleanup(self):
        if self.module_status:
            for _, pin in self.pins_used.items():
                self.pi.set_servo_pulsewidth(pin, 0)
            self.pi.stop()
            self.pins_used = {}
            self.module_status = False

    def control_pins(self, control_values, delay=1):
        for name, value in control_values:
            if self.ignore_control_values:
                return
            elif name not in self.pins_used:
                continue
            else:
                self.pi.set_servo_pulsewidth(self.pins_used.get(name), value)
        time.sleep(delay)
