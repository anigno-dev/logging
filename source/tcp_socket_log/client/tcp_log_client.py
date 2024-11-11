import logging
import logging.handlers
import socket
import time

from source.tcp_socket_log.common.constants import Constants

class TcpLogeerClient:
    def __init__(self, name, server_host="localhost", server_port=logging.handlers.DEFAULT_TCP_LOGGING_PORT):
        """client for sending log messages to logger server"""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.socket_handler = logging.handlers.SocketHandler(server_host, server_port)
        formatter = logging.Formatter(Constants.FORMATTER_STRING)
        self.socket_handler.setFormatter(formatter)
        self.logger.addHandler(self.socket_handler)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def close(self):
        """Closes the logging handler to clean up resources."""
        self.logger.removeHandler(self.socket_handler)
        self.socket_handler.close()

# Example Usage
if __name__ == "__main__":
    # Replace 'your-central-server-ip' with the actual IP address of the logging server
    central_logger = TcpLogeerClient(name="ClientLogger")

    # Log some example messages
    for _ in range(4):
        central_logger.log_info("This is an info message.")
        central_logger.log_warning("This is a warning message.")
        central_logger.log_error("This is an error message.")
        time.sleep(0.5)
    # Close the logger when done
    central_logger.close()
