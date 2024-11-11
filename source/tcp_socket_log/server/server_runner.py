import logging
import os.path
import logging.handlers
from source.tcp_socket_log.common.constants import Constants
from source.tcp_socket_log.server.log_record_tcp_socket_receiver import LogRecordTcpSocketReceiver
from logging.handlers import RotatingFileHandler
class LoggingServer:
    """serve as receiver for all log messages,
    produce a log file from all received logs"""

    def __init__(self, logs_path: str, host: str = "localhost", port: int = logging.handlers.DEFAULT_TCP_LOGGING_PORT):
        self.logs_path = logs_path
        self.host = host
        self.port = port

    def start(self):
        """start the logging server"""
        os.makedirs(self.logs_path, exist_ok=True)
        # setup file logging handler
        logging_formatter = logging.Formatter(Constants.FORMATTER_STRING)
        base_log_file = os.path.join(self.logs_path, "central_log.log")
        # TODO: consider rolling file handler or DB usage
        handler = logging.FileHandler(base_log_file)
        a=logging.handlers.RotatingFileHandler
        handler.formatter = logging_formatter
        tcp_server = LogRecordTcpSocketReceiver(self.host, self.port, handler)
        print("Starting log server...")
        tcp_server.serve_forever()

if __name__ == "__main__":
    server = LoggingServer(logs_path="d:\\temp\\logs")
    # TODO: values should be read from config file
    server.start()
