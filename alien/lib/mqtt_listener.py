import logging
import os
import paho.mqtt.client as mqtt
import random
import threading

from lib.globals import (EXTERNAL_BROKER_HOST, EXTERNAL_BROKER_PORT, LOGGER_TAG,
                         AUTH_INFO_PATH)

class Samsara(threading.Thread):
    def __init__(self, talk_queue):
        super(Samsara, self).__init__(name="Samsara")
        self.q = talk_queue
        self.logger = logging.getLogger(LOGGER_TAG)
        self.client = mqtt.Client(userdata={})
        self.client.connect(host=EXTERNAL_BROKER_HOST, port=EXTERNAL_BROKER_PORT)
        self.authenticated_user = {"userid" : None}
        self.subscribe_topics()

    def subscribe_topics(self):
        self.client.message_callback_add(sub="info/#", callback=self.info_messages) # TBD
        self.client.message_callback_add(sub="atman/auth", callback=self.handle_backdoor_auth)
        self.client.subscribe("atman/auth")

    def info_messages(self, client, userdata, msg):
        self.logger.debug("Received message {} from topic {}".format(msg.topic, msg.payload))

    def handle_backdoor_auth(self, client, userdata, msg):
        userid = msg.payload.decode("utf-8")
        self.logger.debug("[AUTH] Received authentication request for User : {}".format(userid))
        found_user = False
        if not os.path.exists(AUTH_INFO_PATH):
            self.logger.warning("[AUTH] No Auth credentials setup, not expecting this request ... ")
        else:
            fr = open(AUTH_INFO_PATH, "r")
            while True:
                line = fr.readline().strip()
                if not line:
                    break
                else:
                    auth_comps = line.split(":")
                    if len(auth_comps) == 3:
                        user, salt, hash_pass = auth_comps
                        if user != userid:
                            continue
                        self.logger.debug("[AUTH] Sending salt {} for userID {} ...".format(salt, userid))
                        self.client.publish(topic="atman/{}".format(userid), payload=salt)
                        self.client.message_callback_add(sub=hash_pass, callback=self.confirm_handshake)
                        self.logger.debug("[AUTH] Subscribed to secret topic channel for user {}".format(userid))
                        self.client.subscribe(hash_pass)
                        found_user = True
                        break
            fr.close()
        if not found_user:
            self.logger.debug("[AUTH] User {} not found among authorized users list ...".format(userid))
            self.client.publish(topic="atman/{}".format(userid), payload="NONE")

    def confirm_handshake(self, client, userdata, msg):
        client_token = msg.payload.decode("utf-8")
        self.client.unsubscribe(msg.topic)
        used_tokens = list(userdata.keys())
        used_tokens.append(client_token)
        bkdoor_token = client_token
        while bkdoor_token in used_tokens:
            bkdoor_token = "".join(random.choices(population=["0", "1", "2", "3",
                "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"], k=20))
        userdata[bkdoor_token] = client_token
        self.client.user_data_set(userdata)
        self.client.message_callback_add(sub=bkdoor_token, callback=self.handle_commands)
        self.client.subscribe(bkdoor_token)
        self.logger.debug("[AUTH] Communication channel setup : {} (alien) <-> {} (client)".format(bkdoor_token, client_token))
        self.client.publish(topic=client_token, payload=bkdoor_token)

    def handle_commands(self, client, userdata, msg):
        command_recvd = msg.payload.decode("utf-8")
        client_token = userdata.get(msg.topic)
        self.logger.debug("[AUTH] Received from {} : {}".format(client_token, command_recvd))
        payload = "OK"
        if command_recvd == "disconnect":
            self.client.unsubscribe(msg.topic)
            userdata.pop(msg.topic)
            payload = "disconnect"
        else:
            self.q.put(command_recvd)
        self.logger.debug("[AUTH] Sending MESSAGE {} to {}".format(payload, client_token))
        self.client.publish(topic=client_token, payload=payload)

    def run(self):
        self.logger.info("Starting off External MQTT connector ...")
        self.client.loop_forever()
