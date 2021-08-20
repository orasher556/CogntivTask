from socket import socket, AF_INET, SOCK_STREAM

from numpy.random import default_rng

from periodic_sleeper import PeriodicSleeper


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
        sleeper = PeriodicSleeper(self.send_vector, self._PERIOD)

    def send_vector(self):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(self.generate_vector())

    def generate_vector(self):
        vector_bytes = self.rng.normal(size=self._VECTOR_LENGTH).tobytes()
        return vector_bytes
