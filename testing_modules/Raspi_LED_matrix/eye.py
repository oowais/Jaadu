from time import sleep
from Adafruit_LED_Backpack import Matrix8x8

# Create display instance on default I2C address (0x70) and bus number.
l_eye = Matrix8x8.Matrix8x8()
r_eye = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
l_eye.begin()
r_eye.begin()

# Normal, Happy, Laugh, Sad, Angry, Sleepy, Confused
# @Saurav: When combining with the main program, move the expression objects to a different class and import here
default_eyeball_expr = [(0, 2), (0, 3), (0, 4), (0, 5),
                        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
                        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
                        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
                        (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
                        (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
                        (7, 2), (7, 3), (7, 4), (7, 5)]

normal_left_expr = [(0, 2), (0, 3), (0, 4), (0, 5),
                    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
                    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
                    (4, 0), (4, 1), (4, 4), (4, 5), (4, 6), (4, 7),
                    (5, 0), (5, 1), (5, 4), (5, 5), (5, 6), (5, 7),
                    (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
                    (7, 2), (7, 3), (7, 4), (7, 5)]

normal_expr = [(0, 2), (0, 3), (0, 4), (0, 5),
               (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
               (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
               (4, 0), (4, 1), (4, 2), (4, 5), (4, 6), (4, 7),
               (5, 0), (5, 1), (5, 2), (5, 5), (5, 6), (5, 7),
               (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
               (7, 2), (7, 3), (7, 4), (7, 5)]

normal_right_expr = [(0, 2), (0, 3), (0, 4), (0, 5),
                     (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                     (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
                     (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
                     (4, 0), (4, 1), (4, 2), (4, 3), (4, 6), (4, 7),
                     (5, 0), (5, 1), (5, 2), (5, 3), (5, 6), (5, 7),
                     (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
                     (7, 2), (7, 3), (7, 4), (7, 5)]

happy_expr = [(0, 2), (0, 3), (0, 4), (0, 5),
              (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
              (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
              (3, 0), (3, 2), (3, 3), (3, 4), (3, 5), (3, 7),
              (4, 0), (4, 1), (4, 3), (4, 4), (4, 6), (4, 7),
              (5, 0), (5, 1), (5, 2), (5, 5), (5, 6), (5, 7),
              (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
              (7, 2), (7, 3), (7, 4), (7, 5)]

l_laugh_expr = [(0, 2), (0, 3), (0, 4), (0, 5),
                (1, 1), (1, 2), (1, 3), (1, 5), (1, 6),
                (2, 0), (2, 1), (2, 2), (2, 3), (2, 6), (2, 7),
                (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
                (5, 0), (5, 1), (5, 2), (5, 3), (5, 6), (5, 7),
                (6, 1), (6, 2), (6, 3), (6, 5), (6, 6),
                (7, 2), (7, 3), (7, 4), (7, 5)]

r_laugh_expr = [(0, 2), (0, 3), (0, 4), (0, 5),
                (1, 1), (1, 2), (1, 4), (1, 5), (1, 6),
                (2, 0), (2, 1), (2, 4), (2, 5), (2, 6), (2, 7),
                (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
                (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
                (5, 0), (5, 1), (5, 4), (5, 5), (5, 6), (5, 7),
                (6, 1), (6, 2), (6, 4), (6, 5), (6, 6),
                (7, 2), (7, 3), (7, 4), (7, 5)]

sad_expr = [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
            (3, 0), (3, 1), (3, 6), (3, 7),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
            (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)]

l_angry_expr = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                (1, 0), (1, 7),
                (2, 0), (2, 7),
                (3, 0), (3, 3), (3, 4), (3, 7),
                (4, 0), (4, 3), (4, 4), (4, 6),
                (5, 0), (5, 5),
                (6, 0), (6, 4),
                (7, 1), (7, 2), (7, 3)]

r_angry_expr = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                (1, 0), (1, 7),
                (2, 0), (2, 7),
                (3, 0), (3, 3), (3, 4), (3, 7),
                (4, 1), (4, 3), (4, 4), (4, 7),
                (5, 2), (5, 7),
                (6, 3), (6, 7),
                (7, 4), (7, 5), (7, 6)]

# todo
sleepy_expr = []
confused_expr = []


# Run through each pixel individually and turn it on.

def set_pixels_one(eye, arr):
    for a in arr:
        eye.set_pixel(a[0], a[1], 1)
    eye.write_display()


def set_pixels_both(arr):
    for a in arr:
        l_eye.set_pixel(a[0], a[1], 1)
        r_eye.set_pixel(a[0], a[1], 1)
    l_eye.write_display()
    r_eye.write_display()


def clear_buffer():
    l_eye.clear()
    r_eye.clear()


def write_buffer():
    l_eye.write_display()
    r_eye.write_display()


# todo: making the boot up eye
def startup():
    clear_buffer()
    write_buffer()
    print('Startup..')
    for x in range(8):
        for y in range(8):
            l_eye.set_pixel(x, y, 1)
            r_eye.set_pixel(x, y, 1)
            # time.sleep(0.1)
            write_buffer()
    sleep(0.5)
    clear_buffer()
    write_buffer()
    sleep(0.2)


def normal():
    print('Normal')
    clear_buffer()
    set_pixels_both(normal_expr)
    sleep(2)

    clear_buffer()
    set_pixels_both(normal_left_expr)
    sleep(1)

    clear_buffer()
    set_pixels_both(normal_expr)
    sleep(2)

    clear_buffer()
    set_pixels_both(normal_right_expr)
    sleep(1)


def happy():
    print('Happy')
    clear_buffer()
    set_pixels_both(happy_expr)


def laugh(l_arr, r_arr):
    print('Laughing')
    clear_buffer()
    set_pixels_one(l_eye, l_arr)
    set_pixels_one(r_eye, r_arr)


def sad():
    print('Sad')
    clear_buffer()
    set_pixels_both(sad_expr)


def angry(l_arr, r_arr):
    print('angry')
    clear_buffer()
    set_pixels_one(l_eye, l_arr)
    set_pixels_one(r_eye, r_arr)


# todo
def sleepy():
    pass


# todo
def confused():
    pass


try:
    startup()
    while True:
        normal()
        happy()
        sleep(2)
        laugh(l_arr=l_laugh_expr, r_arr=r_laugh_expr)
        sleep(2)
        sad()
        sleep(2)
        angry(l_arr=l_angry_expr, r_arr=r_angry_expr)
        sleep(2)

except KeyboardInterrupt:
    print('Exit...')
