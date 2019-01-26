import logging
import queue
import threading
import time

from lib.brain_emotions import IllusionaryBrain
from lib.globals import LOGGER_TAG
from lib.movement import Karma
from lib.hand_coordinator import MargDarshan
from lib.eye_emotions import EyeDisplay
from lib.ground_coordinator import Prithvi
from lib.mqtt_listener import Samsara


class Atman(threading.Thread):
    def __init__(self):
        super(Atman, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.event_queue = queue.Queue()
        self.emotional_command_eye = lambda x : x
        self.emotional_command_brain = lambda x : x
        self.walker_command_send = None
        self.the_info_src = None
        self.setup()

    def setup(self):
        mqtt_obj = Samsara(talk_queue=self.event_queue)
        walker_obj = Karma()
        emotional_eye_obj = EyeDisplay()
        emotional_brain_obj = IllusionaryBrain()
        hand_ifc_obj = MargDarshan(talk_queue=self.event_queue)
        ground_ifc_obj = Prithvi(talk_queue=self.event_queue)
        mqtt_obj.start()
        walker_obj.start()
        emotional_eye_obj.start()
        emotional_brain_obj.start()
        hand_ifc_obj.start()
        ground_ifc_obj.start()
        self.walker_command_send = walker_obj.set_walking_command
        self.emotional_command_eye = emotional_eye_obj.set_emotion_command
        self.emotional_command_brain = emotional_brain_obj.set_emotion_command
        self.the_info_src = mqtt_obj.get_latest_value

    def pass_item_to_module(self, item):
        module, command = [i.strip() for i in item]

        if module == "move":
            self.walker_command_send(command)
        elif module == "emotify":
            self.emotional_command_eye(command)
            self.emotional_command_brain(command)
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
        elif module == "ground":
            if command == "crocodile":
                pass
            elif command == "plant":
                pass
            elif command == "clear":
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
