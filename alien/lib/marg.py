import threading
import time


class HandCoordinator(threading.Thread):
    def __init__(self, talk_queue):
        super(HandCoordinator, self).__init__()
        self.q = talk_queue

    def run(self):
        while True:
            pass
