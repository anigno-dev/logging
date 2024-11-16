import logging
import os.path
import socket
from datetime import datetime
from logging.handlers import RotatingFileHandler
from os import path
from pathlib import Path

class SimpleRollingAppender(RotatingFileHandler):
    def __init__(self, filename, maxBytes=1024, backupCount=5, mode='a', encoding=None, delay=False):
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        super().__init__(filename, mode, maxBytes, backupCount, encoding, delay)

    def emit(self, record):
        # Placeholder for log emission logic
        # You can preprocess the record or customize how logs are written
        super().emit(record)  # Call parent method for default behavior

    def doRollover(self):
        # Placeholder for rollover logic
        # Customize file renaming, compression, or any additional tasks during rollover
        directory = os.path.dirname(self.baseFilename)  # Directory path
        base_name = os.path.basename(self.baseFilename)  # File name with extension
        file_name, ext = os.path.splitext(base_name)  # Split into name and extension

        new_filename = path.join(directory, file_name + "." + str(f"{(int(ext[1:]) + 1):03}"))
        self.baseFilename = new_filename
        super().doRollover()  # Call parent method for default behavior

    def shouldRollover(self, record):
        # Placeholder for custom rollover conditions
        # Use the default size-based logic by calling the parent method
        return super().shouldRollover(record)

# Usage Example
if __name__ == "__main__":
    logger = logging.getLogger("SimpleRollingLogger")
    logger.setLevel(logging.DEBUG)
    now = datetime.now()
    hostname = socket.gethostname()
    # Format to include milliseconds
    time_string = now.strftime("%Y-%m-%d-%H-%M-%S-") + f"{now.microsecond // 1000:03}"
    base_file_name=f"logs\\log_[{hostname}]_[{time_string}].000"
    handler = SimpleRollingAppender(base_file_name, maxBytes=1024*5, backupCount=1000)
    formatter = logging.Formatter("$%(asctime)s|%(threadName)s|%(levelname)s|%(module)s,%(funcName)s|%(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    # Generate some logs for testing
    for i in range(100):
        logger.debug(f"This is log message {i}")
