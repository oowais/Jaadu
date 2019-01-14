import logging
import queue
import threading
import time

from lib.globals import LOGGER_TAG
from lib.movement import Karma
from lib.hand_coordinator import MargDarshan
from lib.emotion_displayer import Maya
from lib.mqtt_listener import Samsara


class Atman(threading.Thread):
    def __init__(self):
        super(Atman, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.event_queue = queue.Queue()
        self.emotional_queue = queue.Queue()
        self.walker_command_send = None
        self.setup()

    def setup(self):
        mqtt_obj = Samsara(talk_queue=self.event_queue)
        walker_obj = Karma()
        emotional_obj = Maya(listen_queue=self.emotional_queue, info_src=mqtt_obj)
        hand_ifc_obj = MargDarshan(talk_queue=self.event_queue)
        mqtt_obj.start()
        walker_obj.start()
        emotional_obj.start()
        hand_ifc_obj.start()
        self.walker_command_send = walker_obj.set_walking_command

    def pass_item_to_module(self, item):
        module, command = [i.strip() for i in item]

        if module == "move":
            self.walker_command_send(command)
        elif module == "hand":
            if command == "forward":
                self.event_queue.put("move forward")
            elif command == "right":
                self.event_queue.put("move right")
            elif command == "left":
                self.event_queue.put("move left")
            elif command == "clear_and_emotify":
                self.event_queue.put("move stop")
            elif command == "look_up":
                pass
        else:
            self.logger.error("The desired module is not configured, ignoring...")

    def run(self):
        self.logger.info("Starting off Event trigger Listener ...")
        # Get events and send them to respective processes
        while True:
            if self.event_queue.empty():
                time.sleep(1)
                continue
            item = self.event_queue.get()
            self.logger.debug("New event : {}".format(item))
            item_parts = item.split()
            module, command = None, None
            if len(item_parts) == 2:
                module, command = item_parts
            else:
                continue
            self.pass_item_to_module(item=tuple([module, command]))
