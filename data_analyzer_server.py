import time
from socketserver import TCPServer
from datetime import datetime
import numpy as np


class DataAnalyzerServer(TCPServer):
    _MAX_MATRIX_LENGTH = 100

    def __init__(self, host, port):
        super().__init__((host, port), None)
        self.t0 = time.time()
        self.i = 0
        self.frequency_arr = []
        self.matrix = []
        self.matrix_analytics = []

    def finish_request(self, request, client_address):
        byte_data = request.recv(400).strip()
        if len(byte_data) == 400:
            vector = np.frombuffer(byte_data, np.float64)
            self.matrix.append(vector)
            if len(self.matrix) == self._MAX_MATRIX_LENGTH:
                self.calculate_matrix_analytics()
            self.calculate_frequency()

    def calculate_frequency(self):
        t = time.time()
        self.i += 1
        frequency = self.i / (t - self.t0)
        self.frequency_arr.append(frequency)
        print(t, 'Mean Frequency:', frequency)

    def calculate_matrix_analytics(self):
        np_matrix = np.matrix(self.matrix)
        matrix_mean = np_matrix.mean(1)
        matrix_standard_dev = np_matrix.std(1)
        self.matrix_analytics.append((matrix_mean, matrix_standard_dev))
        self.matrix = []

    def create_result_file(self):
        file_name = f"analytics_results_{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        np_frequency = np.array(self.frequency_arr)
        freq_mean = np.mean(np_frequency)
        freq_standard_dev = np.std(np_frequency, dtype=np.float64)
        with open(file_name, 'w') as f:
            f.write(f"Frequencies Mean: {freq_mean}\n")
            f.write(f"Frequencies Standard Deviation: {freq_standard_dev}\n")
            f.write("Data Frequencies:\n")
            f.write(", ".join([str(freq) for freq in self.frequency_arr]) + "\n")
            f.write("Mean and Standard deviation of matrices-----------------------------------------------------\n")
            for mean, std_dev in self.matrix_analytics:
                f.write("Mean------------------------------------------------------------------------------------\n")
                np.savetxt(f, mean)
                f.write("Standard deviation----------------------------------------------------------------------\n")
                np.savetxt(f, std_dev)
