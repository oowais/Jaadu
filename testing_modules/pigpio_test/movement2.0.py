import time
import pigpio
import threading
import time

WALKING_PINS = [("left_leg", 16), ("left_foot", 20), ("right_leg", 25), ("right_foot", 26)]


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


class Karma(threading.Thread):
    def __init__(self):
        super(Karma, self).__init__(name=type(self).__name__)
        self.pigpio_control = PIGPIOController()
        self.pigpio_control.pin_setup()
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

    def forward(self):
        self.pigpio_control.control_pins(control_values=[("left_foot", 1833), ("right_foot", 944)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_leg", 2166), ("right_leg", 1500)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_foot", 611), ("right_foot", 2500)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_leg", 1166), ("right_leg", 2500)], delay=0.3)
        self.default_position()

    def turn_right(self):
        self.pigpio_control.control_pins(control_values=[("left_foot", 611), ("right_foot", 2500)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_leg", 1166), ("right_leg", 1500)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_foot", 1833), ("right_foot", 944)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_leg", 2166), ("right_leg", 2500)], delay=0.3)
        self.default_position()

    def turn_left(self):
        self.pigpio_control.control_pins(control_values=[("left_foot", 1000), ("right_foot", 1944)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_leg", 2166), ("right_leg", 2500)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_foot", 1833), ("right_foot", 944)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_leg", 1166), ("right_leg", 2500)], delay=0.3)
        self.default_position()

    def default_position(self):
        self.pigpio_control.control_pins(control_values=[("left_leg", 1166), ("right_leg", 2500)], delay=0.3)
        self.pigpio_control.control_pins(control_values=[("left_foot", 1833), ("right_foot", 944)], delay=0.3)

    def set_walking_command(self, command):
        if command in ["hello", "forward", "right", "left", "stop"]:
            self.walking_command = command
        if self.current_command != None and self.walking_command != self.current_command:
            self.pigpio_control.stop_pigpio_control()

    def run(self):
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
                self.current_command = None
                
if __name__ == '__main__':
    control = Karma()
    control.forward()
