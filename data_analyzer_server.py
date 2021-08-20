import time
from socketserver import TCPServer

import numpy as np


class DataAnalyzerServer(TCPServer):

    def __init__(self, host, port):
        super().__init__((host, port), None)
        self.t0 = time.time()
        self.i = 0

    def service_actions(self):
        #occurs every loop of checking
        pass

    def finish_request(self, request, client_address):
        byte_data = request.recv(400).strip()
        if len(byte_data) == 400:
            vector = np.frombuffer(byte_data, np.float64)
            t = time.time()
            self.i += 1
            print(t, 'Mean Frequency:', self.i / (t - self.t0))
        # print(f"{client_address[0]} wrote: {vector}")
