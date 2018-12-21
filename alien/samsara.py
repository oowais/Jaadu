#!/usr/bin/env python3

"""samsara.py : Receive outside world information and send required actions to others."""

import logging
import paho.mqtt.client as mqtt

from connection import EXTERNAL_BROKER_HOST, EXTERNAL_BROKER_PORT


def on_connect(client, userdata, flags, rc):
    logger = logging.getLogger("alien")
    #client.subscribe("") -- other side topic


def on_message(client, userdata, msg):
    logger = logging.getLogger("alien")
    logger.debug("Received message {} from topic {}".format(msg.topic, msg.payload))


if __name__ == "__main__":
    client = mqtt.Client(client_id="Narad")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host=EXTERNAL_BROKER_HOST, port=EXTERNAL_BROKER_PORT)
    client.loop_forever()
