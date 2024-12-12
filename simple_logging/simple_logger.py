import logging
import sys

from severity_padding_formatter import SeverityPaddingFormatter

class SimpleLogger:
    def __init__(self, name, level):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.hasHandlers():
            logger.setLevel(level)
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(level)
            formatter = SeverityPaddingFormatter('%(asctime)s|%(levelname)s|%(funcName)s|%(lineno)d|%(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

if __name__ == "__main__":
    SimpleLogger("MyLogger", logging.DEBUG)
    my_logger = logging.getLogger("MyLogger")
    my_logger.debug("This is a DEBUG message.")
    my_logger.info("This is an INFO message.")
    my_logger.warning("This is a WARNING message.")
    my_logger.error("This is an ERROR message.")
    my_logger.critical("This is a CRITICAL message.")
