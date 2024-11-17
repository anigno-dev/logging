import os
from logging.handlers import RotatingFileHandler
import time
from pathlib import Path

from logger_text import HTML_PRETEXT

class HtmlRollingAppender(RotatingFileHandler):
    def __init__(self, logs_path, max_bytes, backup_count, encoding='utf-8', delay=False):
        # filename = os.path.basename(logs_path)
        filename = "log"
        self.next_file_ext: int = 0
        Path(logs_path).mkdir(parents=True, exist_ok=True)
        base_filename = os.path.join(logs_path, filename)
        full_log_file_path = f'{base_filename}.{self.next_file_ext:03}.html'
        super().__init__(full_log_file_path, 'a', max_bytes, backup_count, encoding, delay)
        self.baseFilename = base_filename

    def doRollover(self):
        """increase log file extension by +1"""
        if self.stream:
            self.stream.close()
            self.stream = None
        if self.backupCount > 0:
            self.next_file_ext += 1
            if self.next_file_ext > self.backupCount:
                self.next_file_ext = 0
        if not self.delay:
            self.stream = open(f'{self.baseFilename}.{self.next_file_ext:03}.html', 'w', encoding=self.encoding)

    # def __init__(self, filename, max_bytes, backup_count, mode='a', encoding=None, delay=False):
    #     self.emit_prefix = True
    #     # create path if not exist
    #     Path(filename).parent.mkdir(parents=True, exist_ok=True)
    #     super().__init__(filename, mode, max_bytes, backup_count, encoding, delay)
    #
    # def emit(self, record):
    #     if self.emit_prefix and self.stream:
    #         self.stream.write(HTML_PRETEXT)
    #         self.emit_prefix = False
    #     super().emit(record)
    #
    # def doRollover(self):
    #     # setup rollover file names from 000 to 999
    #     super().doRollover()
    #     # directory = os.path.dirname(self.baseFilename)
    #     # base_name = os.path.basename(self.baseFilename)
    #     # file_name, ext = os.path.splitext(base_name)
    #     # new_filename = path.join(directory, file_name + "." + str(f"{(int(ext[1:]) + 1):03}"))
    #     # self.baseFilename = new_filename
    #
    # def shouldRollover(self, record):
    #     should_rollover = super().shouldRollover(record)
    #     if should_rollover:
    #         self.emit_prefix = True
    #     return should_rollover
