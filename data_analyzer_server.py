import time
from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
import numpy as np


class DataAnalyzerServer(TCPServer):

    def __init__(self, host, port):
        super().__init__((host, port), None)
        self.last_msg_ts = time.time()


    def service_actions(self):
        #occurs every loop of checking
        pass

    def finish_request(self, request, client_address):
        new_msg_time = time.time()
        msg_delta = new_msg_time - self.last_msg_ts
        frequency = 1 / msg_delta
        self.last_msg_ts = new_msg_time
        print(f"msg_delta: {msg_delta} secs, frequency: {frequency}Hz")
        byte_data = request.recv(1024).strip()
        vector = np.frombuffer(byte_data, np.float64)
        print(f"{client_address[0]} wrote: {vector}")
