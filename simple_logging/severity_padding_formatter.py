import logging

class SeverityPaddingFormatter(logging.Formatter):
    def format(self, record):
        if record.levelname == "DEBUG":
            record.levelname = "DEBUG   "
        if record.levelname == "INFO":
            record.levelname = "INFO    "
        if record.levelname == "WARNING":
            record.levelname = "WARNING "
        if record.levelname == "ERROR":
            record.levelname = "ERROR   "
        if record.levelname == "CRITICAL":
            record.levelname = "CRITICAL"
        return super().format(record)
