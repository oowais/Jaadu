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
        self.walker_command_send = lambda x : x
        self.the_info_src = None
        self.ground_module_last = None
        self.timed_wait_events = {}
        self.setup()

    def setup(self):
        mqtt_obj = Samsara(talk_queue=self.event_queue)
        mqtt_obj.start()
        self.the_info_src = mqtt_obj.get_latest_value
        walker_obj = Karma()
        walker_obj.start()
        self.walker_command_send = walker_obj.set_walking_command
        emotional_eye_obj = EyeDisplay()
        emotional_eye_obj.start()
        self.emotional_command_eye = emotional_eye_obj.set_emotion_command
        emotional_brain_obj = IllusionaryBrain()
        emotional_brain_obj.start()
        self.emotional_command_brain = emotional_brain_obj.set_emotion_command
        hand_ifc_obj = MargDarshan(talk_queue=self.event_queue)
        hand_ifc_obj.start()
        ground_ifc_obj = Prithvi(talk_queue=self.event_queue)
        ground_ifc_obj.start()
        self.timed_wait_events[time.time() + 6] = "emotify normal"

    def pass_item_to_module(self, item):
        module, command = [i.strip() for i in item if i != None]
        time_now = time.time()

        if module == "move":
            self.walker_command_send(command)

        elif module == "emotify":
            self.emotional_command_eye(command)
            self.emotional_command_brain(command)
            remove_item = []
            for t, event in self.timed_wait_events.items():
                if event.startswith("emotify"):
                    remove_item.append(t)
            for item in remove_item:
                self.timed_wait_events.pop(item)
            if command == "normal":
                self.timed_wait_events[time_now + 30] = "emotify sleepy"
            else:
                self.timed_wait_events[time_now + 30] = "emotify normal"

        elif module == "hand":
            if command == "forward":
                self.event_queue.put("move forward")
            elif command == "right":
                self.event_queue.put("move right")
            elif command == "left":
                self.event_queue.put("move left")
            elif command == "clear":
                self.event_queue.put("move stop")
                self.event_queue.put("internal ground_fetch")
            elif command == "look_up":
                # User wishes to get the emotions for the Squid
                self.event_queue.put("move hello")
                self.timed_wait_events[time_now + 5] = "emotify scan"
                emotion_value = self.the_info_src("squid")
                if not emotion_value:
                    emotion_value = "surprised"
                self.timed_wait_events[time_now + 10] = "emotify {}".format(emotion_value)

        elif module == "ground":
            if command == "crocodile":
                self.ground_module_last = "crocodile"
            elif command == "plant":
                self.ground_module_last = "plant"
            elif command == "clear":
                self.ground_module_last = None

        elif module == "internal":
            if command == "ground_fetch":
                if not self.ground_module_last:
                    return
                self.event_queue.put("move hello")
                self.timed_wait_events[time_now + 5] = "emotify scan"
                emotion_value = self.the_info_src(self.ground_module_last)
                if not emotion_value:
                    emotion_value = "surprised"
                self.timed_wait_events[time_now + 10] = "emotify {}".format(emotion_value)

        else:
            self.logger.error("The desired module is not configured, ignoring...")

    def run(self):
        self.logger.info("Starting off Event trigger Listener ...")
        # Get events and send them to respective processes
        while True:
            remove_later = []
            for event_time, event in self.timed_wait_events.items():
                if event_time <= time.time():
                    self.event_queue.put(event)
                    remove_later.append(event_time)
            for item in remove_later:
                self.timed_wait_events.pop(item)

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
