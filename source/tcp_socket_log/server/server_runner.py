import logging
import os
import socketserver
import pickle
import struct
import sys
import threading
import time

class LogRecordStreamHandler(socketserver.StreamRequestHandler):
    def handle(self):
        try:
            while True:
                # Read the message length (4 bytes)
                length_prefix = self.rfile.read(4)
                if not length_prefix:
                    break  # Connection closed or empty data

                # Unpack the length and read the actual log record data
                record_length = struct.unpack('>I', length_prefix)[0]
                record_data = self.rfile.read(record_length)

                # Deserialize the record
                log_record = pickle.loads(record_data)
                record = logging.makeLogRecord(log_record)

                # Debug: Print the received log record
                print("Received log record:", record)

                # Log the record to the server's logger
                self.server.logger.handle(record)
        except Exception as e:
            print(f"Error handling log record: {e}")

class LogRecordSocketReceiver(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

    def __init__(self, host, port, handler, logger):
        super().__init__((host, port), handler)
        self.logger = logger

def exit_server():
    time.sleep(5)
    # os._exit(0)

def start_logging_server(host='0.0.0.0', port=9000, log_file='server_logs.log'):
    logger = logging.getLogger('LogCollector')
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s'))
    logger.addHandler(handler)

    server = LogRecordSocketReceiver(host, port, LogRecordStreamHandler, logger)
    print(f"Starting log server on {host}:{port}")
    try:
        threading.Thread(target=exit_server).start()
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        handler.close()
        print("Log server closed.")

if __name__ == '__main__':
    start_logging_server()