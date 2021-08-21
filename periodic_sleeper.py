import threading
import time
from abc import abstractmethod


class PeriodicSleeper(threading.Thread):
    def __init__(self, period):
        super().__init__()
        self.period = period
        self.i = 0
        self.t0 = time.time()
        self.stopped = False
        self.start()

    def sleep(self):
        self.i += 1
        delta = self.t0 + self.period * self.i - time.time()
        if delta > 0:
            time.sleep(delta)

    def run(self):
        while not self.stopped:
            self.task()
            self.sleep()

    def stop(self):
        self.stopped = True

    @abstractmethod
    def task(self):
        pass
