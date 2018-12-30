import threading
import time


class Walker(threading.Thread):
    def __init__(self, listen_queue):
        super(Walker, self).__init__()
        self.q = listen_queue

    def run(self):
        while True:
            if self.q.empty():
                time.sleep(1)
            else:
                item = self.q.get()
