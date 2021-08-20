import time
from socketserver import TCPServer

import numpy as np


class DataAnalyzerServer(TCPServer):

    def __init__(self, host, port):
        super().__init__((host, port), None)
        self.t0 = time.time()
        self.i = 0
        self.frequency_arr = []

    def service_actions(self):
        #occurs every loop of checking
        pass

    def finish_request(self, request, client_address):
        byte_data = request.recv(400).strip()
        if len(byte_data) == 400:
            vector = np.frombuffer(byte_data, np.float64)
            t = time.time()
            self.i += 1
            frequency = self.i / (t - self.t0)
            self.frequency_arr.append(frequency)
            print(t, 'Mean Frequency:', frequency)

    def print_data_acquisition_analytics(self):
        np_frequency = np.array(self.frequency_arr)
        freq_mean = np.mean(np_frequency)
        freq_standard_dev = np.std(np_frequency, dtype=np.float64)
        print("Mean", freq_mean, "Standard Deviation", freq_standard_dev)
