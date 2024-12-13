import logging

from simple_logging.simple_logger import SimpleLogger

if __name__ == "__main__":
    SimpleLogger("MyLogger", logging.DEBUG)
    my_logger = logging.getLogger("MyLogger")
    my_logger.debug("This is a DEBUG message.")
    my_logger.info("This is an INFO message.")
    my_logger.warning("This is a WARNING message.")
    my_logger.error("This is an ERROR message.")
    my_logger.critical("This is a CRITICAL message.")
