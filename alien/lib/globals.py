import os

# Common
LOGGER_TAG = "alien"

# External MQTT Address
EXTERNAL_BROKER_HOST = "localhost" # testing, to be removed
#EXTERNAL_BROKER_HOST = "terrarium"
EXTERNAL_BROKER_PORT = 1883

# Backdoor Auth
AUTH_INFO_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "auth_info")
KEEP_STREAM_TIME = 120
