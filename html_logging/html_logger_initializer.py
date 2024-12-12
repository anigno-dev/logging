import logging
import socket
import sys
from datetime import datetime
from logging import StreamHandler
from os import path

from html_logging.html_Rolling_Appender import HtmlRollingAppender
from html_logging.logger_text import FORMATTER_TEXT_HTML, FORMATTER_TEXT

class HtmlLoggerInitializer:
    """initialize a html rolling logger with given logger name\n
    max backup count set to 1000 files\
    logger is accessible with:\n
    logger = logging.getLogger(logger_name)"""

    @staticmethod
    def create(logger_name, logs_path="logs", is_create_new_folder=True, max_bytes=1024 * 1024 * 2):
        """
        creates new logging.Logger using HtmlRollingAppender
        Params:
        -logger_name: name of logger to be registered in logging system
        -logs_path: path for all logs
        -is_create_new_folder: if True, a new folder with date and time will be created for each run.
                              if False  a timestamp is added to log files
        -max_bytes: maximum bytes per log file before rolling occurs
        """
        # create the logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        # creating base filename
        now = datetime.now()
        hostname = socket.gethostname()
        time_string = now.strftime("%Y-%m-%d-%H-%M-%S-") + f"{now.microsecond // 1000:03}"
        base_logs_path = logs_path
        host_and_time_prefix = f"log_[{hostname}]_[{time_string}]"
        log_file_prefix = "log_" + host_and_time_prefix
        if is_create_new_folder:
            base_logs_path = path.join(logs_path, host_and_time_prefix)
            log_file_prefix = "log"
            # initialize handlers and formatter
        html_handler = HtmlRollingAppender(logs_path=base_logs_path, log_file_prefix=log_file_prefix,
                                           max_bytes=max_bytes, backup_count=999)
        stream_handler = StreamHandler(stream=sys.stdout)
        formatter_html = logging.Formatter(FORMATTER_TEXT_HTML)
        formatter_stream = logging.Formatter(FORMATTER_TEXT)
        html_handler.setFormatter(formatter_html)
        stream_handler.setFormatter(formatter_stream)
        logger.addHandler(html_handler)
        logger.addHandler(stream_handler)

