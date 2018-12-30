import threading
import time


class Emotioner(threading.Thread):
    def __init__(self, listen_queue, info_src):
        super(Emotioner, self).__init__()
        self.info_src = info_src
        self.q = listen_queue

    def run(self):
        while True:
            if self.q.empty():
                time.sleep(1)
            else:
                item = self.q.get()
