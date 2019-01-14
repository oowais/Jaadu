import RPi.GPIO as GPIO
import time

from lib.globals import MIN_DUTY, MAX_DUTY, CENTER, CHANNEL_FREQ, WALKING_PINS


class GPIOController:
    def __init__(self):
        self.pins_used = {}
        self.module_status = False
        self.ignore_control_values = False

    def stop_gpio_control(self):
        self.ignore_control_values = True

    def start_gpio_control(self):
        self.ignore_control_values = False

    def pin_setup(self):
        if self.module_status == False:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            for pin_name, pin_number in WALKING_PINS:
                GPIO.setup(pin_number, GPIO.OUT)
                pwm_obj = GPIO.PWM(pin_number, CHANNEL_FREQ)
                self.pins_used[pin_name] = {"obj" : pwm_obj, "started" : False, "value" : None}
            self.module_status = True

    def cleanup(self):
        if self.module_status == True:
            GPIO.cleanup()
            self.pins_used = {}
            self.module_status = False

    def stop_pwm_pins(self):
        for _, d_pin in self.pins_used.items():
            if d_pin["started"]:
                d_pin["obj"].stop()
                d_pin["started"] = False

    def control_pins(self, control_values, delay=1):
        for name, value in control_values:
            if self.ignore_control_values == True:
                return
            elif name not in self.pins_used:
                continue
            elif self.pins_used[name]["value"] == value:
                continue
            elif not self.pins_used[name]["started"]:
                self.pins_used[name]["obj"].start(value)
                self.pins_used[name]["value"] = value
            else:
                self.pins_used[name]["obj"].ChangeDutyCycle(value)
                self.pins_used[name]["value"] = value
        time.sleep(delay)

    @staticmethod
    def cnvt_angle_to_dc(angle):
        return (((angle * (MAX_DUTY - MIN_DUTY)) / 180) + MIN_DUTY)
