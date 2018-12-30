import logging
import queue
import threading
import time

from lib.deva import ExternalTrigger
from lib.globals import LOGGER_TAG
from lib.karma import Walker
from lib.marg import HandCoordinator
from lib.maya import Emotioner
from lib.samsara import ExternalConnector


class TriggerEvents(threading.Thread):
    def __init__(self):
        super(TriggerEvents, self).__init__()
        self.logger = logging.getLogger(LOGGER_TAG)
        self.event_queue = queue.Queue()
        self.emotional_queue = queue.Queue()
        self.walking_queue = queue.Queue()
        self.setup()

    def setup(self):
        mqtt_obj = ExternalConnector()
        walker_obj = Walker(listen_queue=self.walking_queue)
        emotional_obj = Emotioner(listen_queue=self.emotional_queue, info_src=mqtt_obj)
        hand_ifc_obj = HandCoordinator(talk_queue=self.event_queue)
        ext_trigger_obj = ExternalTrigger(talk_queue=self.event_queue)
        mqtt_obj.start()
        walker_obj.start()
        emotional_obj.start()
        hand_ifc_obj.start()
        ext_trigger_obj.start()

    def run(self):
        self.logger.debug("Starting off Event trigger Listener ...")
        # Get events and send them to respective processes
        while True:
            if self.event_queue.empty():
                time.sleep(1)
            else:
                item = self.event_queue.get()
                if item == "clear":
                    # Clear all items in all controlled Queues
                    pass
                elif item == "walk":
                    # Send event to walking module
                    pass
