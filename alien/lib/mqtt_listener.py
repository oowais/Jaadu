import hashlib
import json
import logging
import os
import paho.mqtt.client as mqtt
import threading
import time

from lib.globals import (EXTERNAL_BROKER_HOST, EXTERNAL_BROKER_PORT, LOGGER_TAG,
                         AUTH_INFO_PATH, KEEP_STREAM_TIME, MQTT_TOPIC_LISTING_PATH)
from lib.secrets import token_hex


class Samsara(threading.Thread):
    def __init__(self, talk_queue):
        super(Samsara, self).__init__(name=type(self).__name__)
        self.module_up = False
        self.q = talk_queue
        self.logger = logging.getLogger(LOGGER_TAG)
        self.client = mqtt.Client(userdata={})
        self.auth_topic_user = {} # hash : {"time", "userid", "secret", "start"}
        self.key_topic_mappings = self.set_topic_interest()
        self.all_saved_info = {}

    def module_setup(self):
        while not self.module_up:
            try:
                self.client.connect(host=EXTERNAL_BROKER_HOST, port=EXTERNAL_BROKER_PORT)
            except (TimeoutError, ConnectionRefusedError):
                self.module_up = False
                self.logger.warning("Could not connect to Broker, MQTT module not up ...")
                time.sleep(1)
            else:
                self.module_up = True
                self.subscribe_topics()

    def set_topic_interest(self):
        t_mappings = {}
        if os.path.exists(MQTT_TOPIC_LISTING_PATH):
            try:
                with open(MQTT_TOPIC_LISTING_PATH, "r") as fr:
                    mappings = json.load(fr)
            except json.decoder.JSONDecodeError:
                self.logger.error("JSON MQTT topics Mapping file corrupted ...")
            else:
                for item in mappings:
                    try:
                        topic, key = item["topic"], item["key"]
                    except KeyError:
                        continue
                    t_mappings[topic] = key
        return t_mappings

    def subscribe_topics(self):
        self.client.message_callback_add(sub="atman/backdoor/auth", callback=self.handle_backdoor_auth_request)
        self.client.subscribe("atman/backdoor/auth")
        self.client.subscribe("atman/backdoor/server/#")
        for topic in self.key_topic_mappings.keys():
            self.client.message_callback_add(sub=topic, callback=self.topic_messages)
            self.client.subscribe(topic)

    def generate_new_topic_code(self, secret):
        new_hash = None
        new_code = None
        hashes_taken = list(self.auth_topic_user.keys())
        hashes_taken.append(new_hash)
        while new_hash in hashes_taken:
            new_code = token_hex(10)
            new_hash = hashlib.sha256("{}{}".format(secret, new_code).encode()).hexdigest()
        new_topic = "atman/backdoor/server/{}".format(new_hash)
        return new_hash, new_topic, new_code

    def handle_backdoor_auth_request(self, client, userdata, msg):
        time_now = time.time()
        remove_items = []
        for topic, topic_dict in self.auth_topic_user.items():
            if (time_now - topic_dict["time"]) > KEEP_STREAM_TIME:
                remove_items.append(topic)
        for item in remove_items:
            self.auth_topic_user.pop(item)

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
                auth_comps = line.split(":")
                if len(auth_comps) != 3:
                    continue
                user, salt, secret = auth_comps
                if user != userid:
                    continue
                self.logger.debug("[AUTH] Sending salt {} for userID {} ...".format(salt, userid))
                new_hash, new_topic, new_code = self.generate_new_topic_code(secret)
                payload = json.dumps({"status" : "ok", "salt" : salt, "code" : new_code})
                self.client.message_callback_add(sub=new_topic, callback=self.handle_commands)
                self.client.publish(topic="atman/backdoor/{}".format(userid), payload=payload)
                self.auth_topic_user[new_hash] = {"time" : time.time(),
                            "userid" : userid, "secret" : secret, "start" : False}
                found_user = True
                break
            fr.close()
        if not found_user:
            self.logger.debug("[AUTH] User {} not found among authorized users list ...".format(userid))
            self.client.publish(topic="atman/backdoor/{}".format(userid), payload=json.dumps({"status" : "deny"}))

    def handle_commands(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode("utf-8"))
        userid, code, command = payload.get("userid", None), payload.get("code", None), payload.get("command", None)
        try:
            hash_from_topic = msg.topic.split("/")[-1]
            expected_user = self.auth_topic_user[hash_from_topic]["userid"]
        except KeyError:
            return
        if expected_user != userid:
            self.logger.warning("[AUTH] An unexpected user is trying to send messages at a secret communication link ...")
            return

        self.client.message_callback_remove(sub=msg.topic)
        old_info = self.auth_topic_user.pop(hash_from_topic)
        old_info["time"] = time.time()
        client_topic = "atman/backdoor/client/{}".format(hashlib.sha256("{}{}".format(old_info["secret"], code).encode()).hexdigest())
        payload = {"userid" : userid, "status" : "ok", "code" : None}
        if command == "disconnect":
            self.logger.debug("[AUTH] Disconnecting from client for user {}".format(userid))
            payload["status"] = "disconnect"
            payload.pop("code")
        else:
            new_hash, new_topic, new_code = self.generate_new_topic_code(secret=old_info["secret"])
            payload["code"] = new_code
            if command == "start":
                old_info["start"] = True
                self.logger.debug("[AUTH] Handshake between Backdoor client and server successful for user {}".format(userid))
            else:
                if old_info["start"] == True:
                    self.q.put(command)
            self.auth_topic_user[new_hash] = old_info
            self.client.message_callback_add(sub=new_topic, callback=self.handle_commands)
        self.client.publish(topic=client_topic, payload=json.dumps(payload))

    def topic_messages(self, client, userdata, msg):
        self.logger.debug("Received message {} from topic {}".format(msg.payload, msg.topic))
        internal_key = self.key_topic_mappings.get(msg.topic, None)
        if internal_key:
            self.logger.debug("Message saved under internal key : {}".format(internal_key))
            self.all_saved_info[internal_key] = msg.payload.decode().strip().lower()

    def get_latest_value(self, key):
        return self.all_saved_info.get(key, None)

    def run(self):
        self.module_setup()
        self.logger.info("Starting off External MQTT connector ...")
        self.client.loop_forever()
