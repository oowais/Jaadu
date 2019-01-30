import board
import math
import neopixel
import threading
import time

from lib.display_emotions import EmotionsDisplayer
from lib.globals import NUM_PIXELS_USED, LED_STRIP_PIN


class IllusionaryBrain(EmotionsDisplayer):
    def __init__(self):
        super(IllusionaryBrain, self).__init__(name=type(self).__name__)
        self.pixels = None
        self.rainbow_cycle_index = 0
        self.breathing_index = 0
        self.scan_iter = 0

    def module_setup(self):
        if not self.module_up:
            self.pixels = neopixel.NeoPixel(eval(LED_STRIP_PIN), NUM_PIXELS_USED,
                                            auto_write=False, pixel_order=neopixel.GRB)
            self.module_up = True
            self.set_emotion_command(command="startup")
        self.logger.info("Successfully setup the Brain Module to display emotions ...")

    def startup(self):
        startup_loop = [
            "self.pixels.fill(color=(255, 0, 0))",
            "self.pixels.show()",
            "time.sleep(2)",
            "self.pixels.fill(color=(0, 255, 0))",
            "self.pixels.show()",
            "time.sleep(2)",
            "self.pixels.fill(color=(0, 0, 255))",
            "self.pixels.show()",
            "time.sleep(2)"
        ]
        self.pixels.brightness = 1
        self.execute_emotion(commands_loop=startup_loop)

    def normal(self):
        normal_loop = [
            "self.rainbow_cycle()",
            "self.pixels.show()",
            "time.sleep(0.001)"
        ]
        self.pixels.brightness = 1
        self.execute_emotion(commands_loop=normal_loop)

    def happy(self):
        happy_loop = [
            "self.pixels.fill(color=(0, 255, 0))",
            "self.pixels.show()",
            "time.sleep(1)",
            "self.pixels.fill(color=(0, 0, 0))",
            "self.pixels.show()",
            "time.sleep(1)"
        ]
        self.pixels.brightness = 1
        self.execute_emotion(commands_loop=happy_loop)

    def sad(self):
        sad_loop = [
            "self.pixels.fill(color=(0, 0, 255))",
            "self.breathing_effect()",
            "self.pixels.show()",
            "time.sleep(0.001)"
        ]
        self.execute_emotion(commands_loop=sad_loop)

    def angry(self):
        angry_loop = [
            "self.pixels.fill(color=(255, 0, 0))",
            "self.pixels.show()",
            "time.sleep(1)",
            "self.pixels.fill(color=(0, 0, 0))",
            "self.pixels.show()",
            "time.sleep(1)"
        ]
        self.pixels.brightness = 1
        self.execute_emotion(commands_loop=angry_loop)

    def sleepy(self):
        sleepy_loop = [
            "self.pixels.fill(color=(0, 255, 255))",
            "self.breathing_effect()",
            "self.pixels.show()",
            "time.sleep(0.001)"
        ]
        self.execute_emotion(commands_loop=sleepy_loop)

    def surprised(self):
        surprised_loop = [
            "self.pixels.fill(color=(255, 165, 0))",
            "self.pixels.show()",
            "time.sleep(1)",
            "self.pixels.fill(color=(0, 0, 0))",
            "self.pixels.show()",
            "time.sleep(1)"
        ]
        self.pixels.brightness = 1
        self.execute_emotion(commands_loop=surprised_loop)

    def low_power(self):
        low_power_loop = [
            "self.pixels.fill(color=(255, 0, 0))",
            "self.breathing_effect()",
            "self.pixels.show()",
            "time.sleep(0.001)"
        ]
        self.execute_emotion(commands_loop=low_power_loop)

    def scan(self):
        scan_loop = [
            "self.scan_light()",
            "self.pixels.show()",
            "time.sleep(0.01)"
        ]
        self.execute_emotion(commands_loop=scan_loop)

    def scan_light(self):
        if self.scan_iter < NUM_PIXELS_USED:
            self.pixels[self.scan_iter] = (255, 0, 0)
        elif self.scan_iter >= NUM_PIXELS_USED and self.scan_iter < (NUM_PIXELS_USED * 2):
            self.pixels[self.scan_iter - NUM_PIXELS_USED] = (0, 255, 0)
        elif self.scan_iter >= (NUM_PIXELS_USED * 2) and self.scan_iter < (NUM_PIXELS_USED * 3):
            self.pixels[self.scan_iter - (NUM_PIXELS_USED * 2)] = (0, 0, 255)
        else:
            self.scan_iter = -1
        self.scan_iter += 1

    def wheel(self, pos):
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos*3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos*3)
            g = 0
            b = int(pos*3)
        else:
            pos -= 170
            r = 0
            g = int(pos*3)
            b = int(255 - pos*3)
        return (r, g, b)

    def rainbow_cycle(self):
        for i in range(NUM_PIXELS_USED):
            pixel_index = (i * 256 // NUM_PIXELS_USED) + self.rainbow_cycle_index
            self.pixels[i] = self.wheel(pixel_index & 255)
        if self.rainbow_cycle_index == 254:
            self.rainbow_cycle_index = 0
        else:
            self.rainbow_cycle_index += 1

    def breathing_effect(self):
        maximum_brightness = 1
        speed_factor = 0.01
        self.pixels.brightness = maximum_brightness / 2.0 * (1.0 + math.sin(speed_factor * self.breathing_index))
        if self.breathing_index == 65534:
            self.breathing_index = 0
        else:
            self.breathing_index += 1
