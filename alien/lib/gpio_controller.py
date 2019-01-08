import RPi.GPIO as GPIO
import time

from lib.globals import MIN_DUTY, MAX_DUTY, CENTER, CHANNEL_FREQ


class GPIOController:
    def __init__(self, pin_info):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.pins_used = {}
        self.pin_setup(pin_info=pin_info)

    def pin_setup(self, pin_info):
        for pin_name, pin_number in pin_info:
            GPIO.setup(pin_number, GPIO.OUT)
            pwm_obj = GPIO.PWM(pin_number, CHANNEL_FREQ)
            self.pins_used[pin_name] = {"obj" : pwm_obj, "started" : False}

    def cleanup(self):
        self.pins_used = {}
        GPIO.cleanup()

    def stop_pwm_pins(self):
        for _, d_pin in self.pins_used.items():
            if d_pin["started"]:
                d_pin["obj"].stop()
                d_pin["started"] = False

    def control_pins(self, control_values, delay=1):
        for name, value in control_values:
            if name not in self.pins_used:
                continue
            elif not self.pins_used[name]["started"]:
                self.pins_used[name]["obj"].start(value)
            else:
                self.pins_used[name]["obj"].ChangeDutyCycle(value)
        time.sleep(delay)

    @staticmethod
    def cnvt_angle_to_dc(angle):
        return (((angle * (MAX_DUTY - MIN_DUTY)) / 180) + MIN_DUTY)
