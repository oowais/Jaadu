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
        self.walking_queue = queue.Queue()
        self.setup()

    def setup(self):
        mqtt_obj = Samsara(talk_queue=self.event_queue)
        walker_obj = Karma(listen_queue=self.walking_queue)
        emotional_obj = Maya(listen_queue=self.emotional_queue, info_src=mqtt_obj)
        hand_ifc_obj = MargDarshan(talk_queue=self.event_queue)
        mqtt_obj.start()
        walker_obj.start()
        emotional_obj.start()
        hand_ifc_obj.start()

    def run(self):
        self.logger.info("Starting off Event trigger Listener ...")
        # Get events and send them to respective processes
        while True:
            if self.event_queue.empty():
                time.sleep(1)
            else:
                item = self.event_queue.get()
                self.logger.debug("Received event : {}".format(item))
                if item == "clear":
                    # Clear all items in all controlled Queues
                    pass
                elif item == "walk":
                    # Send event to walking module
                    pass
