from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
import numpy as np


class DataAnalyzerHandler(BaseRequestHandler):

    def handle(self):
        byte_data = self.request.recv(1024).strip()
        vector = np.frombuffer(byte_data, np.float64)
        print(f"{self.client_address[0]} wrote: {vector}")


class DataAnalyzerServer(ThreadingMixIn, TCPServer):

    def __init__(self, host, port):
        super().__init__((host, port), DataAnalyzerHandler)
