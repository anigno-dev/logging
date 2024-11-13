import logging
import pickle
import socket
import struct
import time

class PickleSocketHandler(logging.Handler):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def emit(self, record):
        try:
            # Pickle the record to bytes
            data = pickle.dumps(record.__dict__)
            length_prefix = struct.pack('>I', len(data))

            # Debug: Print the log record being sent
            print("Sending log record:", record)

            # Send the length and the data
            self.socket.sendall(length_prefix + data)
        except Exception as e:
            print(f"Error sending log record: {e}")

    def close(self):
        self.socket.close()
        super().close()

def setup_network_logger(server_host, server_port, logger_name='NetworkLogger'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Use PickleSocketHandler
    socket_handler = PickleSocketHandler(server_host, server_port)
    logger.addHandler(socket_handler)

    return logger

# Example usage
logger = setup_network_logger('127.0.0.1', 9000)

for a in range(10):
    logger.info("Test log message from client.")
    logger.warning("Test log message from client.")
    logger.debug("Test log message from client.")
    logger.error("Test log message from client.")
    time.sleep(1)