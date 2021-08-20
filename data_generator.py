import time
from socket import socket, AF_INET, SOCK_STREAM

from numpy.random import default_rng


class DataGenerator:
    _VECTOR_LENGTH = 50
    _FREQUENCY = 1000
    _PERIOD = 1.0 / _FREQUENCY
    _PRECISION = 0.00001

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.rng = default_rng()

    def start(self):
        while True:
            with socket(AF_INET, SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                time_before = time.time()
                sock.sendall(self.generate_vector())
            while (time.time() - time_before) < self._PERIOD:
                time.sleep(self._PRECISION)

    def generate_vector(self):
        return self.rng.normal(size=self._VECTOR_LENGTH).tobytes()
