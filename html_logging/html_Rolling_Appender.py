import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

from html_logging.logger_text import HTML_PRETEXT

class HtmlRollingAppender(RotatingFileHandler):
    """perform log file rolling and handling HTML pre text, scripts and tags.\n
    log files extension is .html, to allow any browser to display the log file"""

    def __init__(self, logs_path: str, log_file_prefix="log", max_bytes: int = 1024 * 1024 * 2, backup_count=999,
                 encoding='utf-8', delay=False):
        # filename = os.path.basename(logs_path)
        self.emit_prefix = True
        filename = log_file_prefix
        self.next_file_ext: int = 0
        Path(logs_path).mkdir(parents=True, exist_ok=True)
        base_filename = os.path.join(logs_path, filename)
        full_log_file_path = f'{base_filename}.{self.next_file_ext:03}.html'
        super().__init__(full_log_file_path, 'a', max_bytes, backup_count, encoding, delay)
        self.stream.write(HTML_PRETEXT)
        self.baseFilename = base_filename

    def doRollover(self):
        self.emit_prefix = True
        if self.stream:
            self.stream.close()
            self.stream = None
        if self.backupCount > 0:
            self.next_file_ext += 1
            if self.next_file_ext > self.backupCount:
                self.next_file_ext = 0
        if not self.delay:
            self.stream = open(f'{self.baseFilename}.{self.next_file_ext:03}.html', 'w', encoding=self.encoding)
            self.stream.write(HTML_PRETEXT)

    def emit(self, record):
        super().emit(record)
