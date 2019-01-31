import os

# Common
LOGGER_TAG = "alien"

# MQTT
# External MQTT Address
EXTERNAL_BROKER_HOST = "localhost"
EXTERNAL_BROKER_PORT = 1883
# Backdoor Auth
AUTH_INFO_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "auth_info")
KEEP_STREAM_TIME = 120
# Topics to listen to
MQTT_TOPIC_LISTING_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "mqtt_topic_mappings.json")

# Movement
# --------------- PIGPIO control values (Experimental) ---------------------
# | Left foot | Angle | pigpio width | | Right foot | Angle | pigpio width |
# | up        | 10    | 500          | | up         | 180   | 2500         |
# | straight  | 45    | 900          | | straight   | 130   | 1944         |
# | down      | 120   | 1900         | | down       | 40    | 944          |

# | Left leg  | Angle | pigpio width | | Right leg  | Angle | pigpio width |
# | center    | 60    | 1066         | | center     | 180   | 2500         |
# | extreme   | 150   | 2166         | | extreme    | 90    | 1500         |
# --------------------------------------------------------------------------
MOVE_CONTROL_VALUES = {"left_foot" : {"up" : 500, "straight" : 900, "down" : 1900 },
                       "right_foot" : {"up" : 2500 , "straight" : 1944, "down" : 944 },
                       "left_leg" : {"center" : 1066, "extreme" : 2166 },
                       "right_leg" : {"center" : 2500, "extreme" : 1500, "hello" : 2000 }}
# Movement Setup
WALKING_PINS = [("left_leg", 16), ("left_foot", 20), ("right_leg", 25), ("right_foot", 26)]

# Hand Module
HAND_BLUETOOTH_MAC = "98:D3:31:F5:B9:E7"
HAND_BLUETOOTH_PORT = 1

# Ground Module
GROUND_BLUETOOTH_MAC = "98:D3:41:FD:40:7F"
GROUND_BLUETOOTH_PORT = 2

# Eyes specific configuration
EYE_I2C_ADDRESS = 0x70
# Brain specific configuration
LED_STRIP_PIN = "board.D18"
NUM_PIXELS_USED = 27
