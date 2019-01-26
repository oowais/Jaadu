import os

# Common
LOGGER_TAG = "alien"

# MQTT
# External MQTT Address
EXTERNAL_BROKER_HOST = "localhost" # testing, to be removed
#EXTERNAL_BROKER_HOST = "terrarium"
EXTERNAL_BROKER_PORT = 1883
# Backdoor Auth
AUTH_INFO_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "auth_info")
KEEP_STREAM_TIME = 120
# Topics to listen to
MQTT_TOPIC_LISTING_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "mqtt_topic_mappings.json")

# Movement
# GPIO Setup
MIN_DUTY = 3
MAX_DUTY = 11
CENTER = (MAX_DUTY + MIN_DUTY) / 2
CHANNEL_FREQ = 50
# Movement Setup
WALKING_PINS = [("left_leg", 16), ("left_foot", 20), ("right_leg", 25), ("right_foot", 26)]

# Hand Module
HAND_BLUETOOTH_MAC = "98:D3:31:F5:B9:E7"
HAND_BLUETOOTH_PORT = 1

# Ground Module
GROUND_BLUETOOTH_MAC = "98:D3:41:FD:40:7F"
GROUND_BLUETOOTH_PORT = 1

# Eyes and Brain Modules
SHOW_EMOTION_FOR_TIME = 120
# Eyes specific configuration
EYE_I2C_ADDRESS = 0x70
# Brain specific configuration
LED_STRIP_PIN = "board.D18"
NUM_PIXELS_USED = 27
