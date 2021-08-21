import argparse
import time
from threading import Thread

from data_analyzer_server import DataAnalyzerServer
from data_generator import DataGenerator


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--noisy", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    HOST, PORT = "localhost", 9999
    args = get_args()
    with DataAnalyzerServer(HOST, PORT) as server:
        analyzer_thread = Thread(target=server.serve_forever)
        analyzer_thread.daemon = True
        analyzer_thread.start()

        generator = DataGenerator(HOST, PORT, args.noisy)
        time.sleep(5)
        generator.stop()
        server.create_result_file()
