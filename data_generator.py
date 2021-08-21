import time
from socket import socket, AF_INET, SOCK_STREAM

from numpy.random import default_rng

from periodic_sleeper import PeriodicSleeper


class DataGenerator(PeriodicSleeper):
    _VECTOR_LENGTH = 50
    _FREQUENCY = 1000

    def __init__(self, host, port, noisy_mode):
        self.host = host
        self.port = port
        self.rng = default_rng()
        self.drop_time = time.time() + self.rng.uniform(2, 3) if noisy_mode else 0
        super().__init__(1.0 / self._FREQUENCY)

    def task(self):
        if self.drop_time and self.drop_time <= time.time():
            self.drop_time += self.rng.uniform(2, 3)
        else:
            with socket(AF_INET, SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                sock.sendall(self.generate_vector())

    def generate_vector(self):
        vector_bytes = self.rng.normal(size=self._VECTOR_LENGTH).tobytes()
        return vector_bytes
