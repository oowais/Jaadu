from Adafruit_LED_Backpack import Matrix8x8

from lib.display_emotions import EmotionsDisplayer
from lib.globals import EYE_I2C_ADDRESS


class EyeDisplay(EmotionsDisplayer):
    def __init__(self):
        super(EyeDisplay, self).__init__(name=type(self).__name__)
        self.left_eye = None
        self.right_eye = None

    def module_setup(self):
        if not self.module_up:
            self.left_eye = Matrix8x8.Matrix8x8(address=EYE_I2C_ADDRESS, busnum=1)
            self.right_eye = Matrix8x8.Matrix8x8(address=EYE_I2C_ADDRESS, busnum=3)
            self.left_eye.begin()
            self.right_eye.begin()
            self.module_up = True
            self.set_emotion_command(command="startup")
            self.logger.info("Successfully setup the Eyes Module to display emotions ...")

    def startup(self):
        startup_loop = [
            "self.clear_buffer()",
            "self.write_buffer()",
            "self.set_pixels(lib.emotions_library.BOOT, lib.emotions_library.BOOT)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.BOOT, lib.emotions_library.BOOT)",
            "time.sleep(0.5)",
            "self.set_pixels(lib.emotions_library.BOOT, lib.emotions_library.BOOT)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.LEFT_BOOT_1, lib.emotions_library.RIGHT_BOOT_1)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.LEFT_BOOT_2, lib.emotions_library.RIGHT_BOOT_2)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.LEFT_BOOT_3, lib.emotions_library.RIGHT_BOOT_3)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.LEFT_BOOT_4, lib.emotions_library.RIGHT_BOOT_4)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.LEFT_BOOT_5, lib.emotions_library.RIGHT_BOOT_5)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.LEFT_BOOT_6, lib.emotions_library.RIGHT_BOOT_6)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.LEFT_BOOT_7, lib.emotions_library.RIGHT_BOOT_7)",
            "time.sleep(0.5)",
            "self.clear_pixels(lib.emotions_library.LEFT_BOOT_8, lib.emotions_library.RIGHT_BOOT_8)",
            "time.sleep(0.5)"
        ]
        self.execute_emotion(commands_loop=startup_loop, loop=False)

    def normal(self):
        normal_loop = [
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_NORMAL, lib.emotions_library.RIGHT_NORMAL)",
            "time.sleep(2)",
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_NORMAL_2, lib.emotions_library.RIGHT_NORMAL_2)",
            "time.sleep(2)"
        ]
        self.execute_emotion(commands_loop=normal_loop, next_emotion="sleepy")

    def happy(self):
        happy_loop = [
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_HAPPY, lib.emotions_library.RIGHT_HAPPY)",
            "time.sleep(0.7)",
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_HAPPY_2, lib.emotions_library.RIGHT_HAPPY_2)",
            "time.sleep(0.7)"
        ]
        self.execute_emotion(commands_loop=happy_loop)

    def sad(self):
        sad_loop = [
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_SAD, lib.emotions_library.RIGHT_SAD)"
        ]
        self.execute_emotion(commands_loop=sad_loop)

    def angry(self):
        angry_loop = [
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_ANGRY, lib.emotions_library.RIGHT_ANGRY)",
            "time.sleep(1)",
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_ANGRY_2, lib.emotions_library.RIGHT_ANGRY_2)",
            "time.sleep(1)"
        ]
        self.execute_emotion(commands_loop=angry_loop)

    def sleepy(self):
        sleepy_loop = [
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_SLEEPY, lib.emotions_library.RIGHT_SLEEPY)"
        ]
        self.execute_emotion(commands_loop=sleepy_loop, next_emotion="sleepy")

    def surprised(self):
        surprised_loop = [
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_SURPRISED, lib.emotions_library.RIGHT_SURPRISED)",
            "time.sleep(1)",
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_SURPRISED_2, lib.emotions_library.RIGHT_SURPRISED_2)",
            "time.sleep(1)"
        ]
        self.execute_emotion(commands_loop=surprised_loop)

    def low_power(self):
        low_power_loop = [
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_LOW_POWER, lib.emotions_library.RIGHT_LOW_POWER)",
            "time.sleep(0.5)",
            "self.clear_buffer()",
            "self.set_pixels(lib.emotions_library.LEFT_LOW_POWER_2, lib.emotions_library.RIGHT_LOW_POWER_2)",
            "time.sleep(0.5)"
        ]
        self.execute_emotion(commands_loop=low_power_loop)

    def clear_pixels(self, l_arr, r_arr):
        for a in l_arr:
            self.left_eye.set_pixel(a[0], a[1], 0)
        for a in r_arr:
            self.right_eye.set_pixel(a[0], a[1], 0)
        self.write_buffer()

    def set_pixels(self, l_arr, r_arr):
        for a in l_arr:
            self.left_eye.set_pixel(a[0], a[1], 1)
        for a in r_arr:
            self.right_eye.set_pixel(a[0], a[1], 1)
        self.write_buffer()

    def clear_buffer(self):
        self.left_eye.clear()
        self.right_eye.clear()

    def write_buffer(self):
        self.left_eye.write_display()
        self.right_eye.write_display()
