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
WALKING_PINS = [("left_leg", 2), ("left_foot", 3), ("right_leg", 4), ("right_foot", 17)]

# Hand Module
HAND_BLUETOOTH_MAC = "98:D3:31:F5:B9:E7"
HAND_BLUETOOTH_PORT = 1
HAND_BLUETOOTH_RECV_PORT = 2

# Ground Module
GROUND_BLUETOOTH_MAC = None
GROUND_BLUETOOTH_SEND_PORT = 1
GROUND_BLUETOOTH_RECV_PORT = 2

# Eyes and Brain Modules
SHOW_EMOTION_FOR_TIME = 120
# Eyes specific configuration
EYE_I2C_ADDRESS = None
# Brain specific configuration
NUM_PIXELS_USED = 30
PIXEL_BRIGHTNESS = 0.2
