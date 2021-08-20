from socket import socket, AF_INET, SOCK_STREAM

from numpy.random import default_rng


class DataGenerator:
    _VECTOR_LENGTH = 50

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.rng = default_rng()

    def start(self):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(self.generate_vector())

    def generate_vector(self):
        return self.rng.normal(size=self._VECTOR_LENGTH).tobytes()

