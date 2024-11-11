import logging
import logging.handlers
import socketserver

from source.tcp_socket_log.server.log_record_stream_handler import LogRecordStreamHandler

class LogRecordTcpSocketReceiver(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

    def __init__(self, host='localhost', port=logging.handlers.DEFAULT_TCP_LOGGING_PORT, handler=None):
        print(f"initializing {self.__class__.__name__} at: {host} : {port}")
        socketserver.ThreadingTCPServer.__init__(self, (host, port), LogRecordStreamHandler)
        self.log_handler = logging.getLogger()
        if handler is not None:
            self.log_handler.addHandler(handler)

