import pickle
import socketserver
import struct

class LogRecordStreamHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            try:
                chunk = self.connection.recv(4)
                if len(chunk) < 4:
                    break
                slen = struct.unpack('>L', chunk)[0]
                chunk = self.connection.recv(slen)
                while len(chunk) < slen:
                    chunk += self.connection.recv(slen - len(chunk))
                record = self.server.log_handler.makeLogRecord(pickle.loads(chunk))
                self.server.logger.handle(record)
                raise Exception("test")
            except Exception as ex:
                print(f'Exception in {type(self)} {ex} {ex.args}')
                break
