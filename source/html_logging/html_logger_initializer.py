import logging
import socket
import sys
from datetime import datetime
from logging import StreamHandler
from os import path

from html_Rolling_Appender import HtmlRollingAppender
from logger_text import FORMATTER_TEXT, FORMATTER_TEXT_HTML

class HtmlLoggerInitializer:
    """initialize a html rolling logger with given logger name\n
    max backup count set to 1000 files\
    logger is accessible with:\n
    logger = logging.getLogger(logger_name)"""

    def __init__(self, logger_name, logs_path="logs", max_bytes=1024 * 1024 * 2, ):
        # create the logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        # creating base filename
        now = datetime.now()
        hostname = socket.gethostname()
        time_string = now.strftime("%Y-%m-%d-%H-%M-%S-") + f"{now.microsecond // 1000:03}"
        base_file_name = path.join(logs_path, f"log_[{hostname}]_[{time_string}]")
        # initialize handlers and formatter
        html_handler = HtmlRollingAppender(base_file_name, max_bytes=max_bytes, backup_count=1000)
        stream_handler = StreamHandler(stream=sys.stderr)
        formatter_html = logging.Formatter(FORMATTER_TEXT_HTML)
        formatter_stream = logging.Formatter(FORMATTER_TEXT)
        html_handler.setFormatter(formatter_html)
        stream_handler.setFormatter(formatter_stream)
        logger.addHandler(html_handler)
        logger.addHandler(stream_handler)

if __name__ == '__main__':
    class ExampleLogging:
        def run(self):
            HtmlLoggerInitializer("my_logger", "logs", 1024 * 4)
            my_logger = logging.getLogger("my_logger")
            for a in range(400):
                my_logger.debug(f"debug message {a} " * 2)
                # my_logger.info(f"info message {a} " * 2)
                # my_logger.warning(f"warning message {a} " * 2)
                # my_logger.error(f"error message {a} " * 2)

    ExampleLogging().run()
