import logging
import paho.mqtt.client as mqtt
import threading

from lib.globals import EXTERNAL_BROKER_HOST, EXTERNAL_BROKER_PORT, LOGGER_TAG

class ExternalConnector(threading.Thread):
    def __init__(self):
        super(ExternalConnector, self).__init__()
        self.logger = logging.getLogger(LOGGER_TAG)
        self.client = mqtt.Client()
        self.client.connect(host=EXTERNAL_BROKER_HOST, port=EXTERNAL_BROKER_PORT)
        self.client.on_message = self.on_message
        self.subscribe_topics()

    def subscribe_topics(self):
        self.client.subscribe("testing/#")

    def on_message(self, client, userdata, msg):
        self.logger.debug("Received message {} from topic {}".format(msg.topic, msg.payload))

    def run(self):
        self.logger.info("Starting off External MQTT connector ...")
        self.client.loop_forever()
