import time
from threading import Thread

from data_analyzer_server import DataAnalyzerServer
from data_generator import DataGenerator

if __name__ == '__main__':
    HOST, PORT = "localhost", 9999

    with DataAnalyzerServer(HOST, PORT) as server:
        analyzer_thread = Thread(target=server.serve_forever)
        analyzer_thread.daemon = True
        analyzer_thread.start()

        generator = DataGenerator(HOST, PORT)
        generator.start()
        time.sleep(1)
        server.create_result_file()

