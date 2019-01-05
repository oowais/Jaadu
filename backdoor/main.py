import argparse
import getpass
import hashlib
import json
import logging
import os
import paho.mqtt.client as mqtt
import secrets
import sys


def handle_salt(client, userdata, msg):
    logger = logging.getLogger("alien_backdoor")
    try:
        userid = msg.topic.split("/")[-1]
    except Exception:
        logger.error("Could not get back the userID. Exiting...")
        client.disconnect()
        return

    client.message_callback_remove(sub=msg.topic)
    client.unsubscribe(msg.topic)
    payload = json.loads(msg.payload.decode("utf-8"))
    status, salt, code = payload.get("status", None), payload.get("salt", None), payload.get("code", None)
    if status == "deny":
        logger.error("Cannot connect with backdoor. Exiting ...")
        client.disconnect()
        return
    logger.debug("Received salt {} for USerID {}".format(salt, userid))
    passwd = getpass.getpass()
    if not passwd:
        logger.error("Password entered is not valid. Exiting ....")
        client.disconnect()
        return

    secret = hashlib.sha256("{}{}{}".format(salt, userid, passwd).encode()).hexdigest()
    userdata["secret"] = secret
    client.user_data_set(userdata)
    bkdoor_topic = "atman/backdoor/server/{}".format(hashlib.sha256("{}{}".format(secret, code).encode()).hexdigest())
    new_code = secrets.token_hex(10)
    client_stream_topic = "atman/backdoor/client/{}".format(hashlib.sha256("{}{}".format(secret, new_code).encode()).hexdigest())

    client.message_callback_add(sub=client_stream_topic, callback=handle_commands)
    client.subscribe(client_stream_topic)
    client.publish(topic=bkdoor_topic, payload=json.dumps({"userid" : userid,
                                    "code" : new_code, "command" : "start"}))


def handle_commands(client, userdata, msg):
    logger = logging.getLogger("alien_backdoor")
    payload = json.loads(msg.payload.decode("utf-8"))
    userid, status, code = payload.get("userid", None), payload.get("status", None), payload.get("code", None)
    if userid != userdata["userid"]:
        return

    client.message_callback_remove(sub=msg.topic)
    client.unsubscribe(msg.topic)
    if status == "ok":
        logger.info("Received successfully at Backdoor ...")
    elif status == "disconnect":
        logger.info("Disconnected from Backdoor. Exiting ...")
        client.disconnect()
        return
    else:
        return

    command = input("\nSend command : ")
    bkdoor_topic = "atman/backdoor/server/{}".format(hashlib.sha256("{}{}".format(userdata["secret"], code).encode()).hexdigest())
    new_code = secrets.token_hex(10)
    client_stream_topic = "atman/backdoor/client/{}".format(hashlib.sha256("{}{}".format(userdata["secret"], new_code).encode()).hexdigest())
    client.message_callback_add(sub=client_stream_topic, callback=handle_commands)
    client.subscribe(client_stream_topic)
    payload = json.dumps({"userid" : userid, "code" : new_code, "command" : command})
    client.publish(topic=bkdoor_topic, payload=payload)


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

    userid = input("Enter UserID : ")
    logger.info("Sending request to Check USERID with Alien ...")

    client = mqtt.Client(userdata={"userid" : userid})
    client.connect(host=host, port=port)
    topic = "atman/backdoor/{}".format(userid)
    client.message_callback_add(sub=topic, callback=handle_salt)
    client.subscribe(topic)
    client.publish(topic="atman/backdoor/auth", payload=userid)

    client.loop_forever()
