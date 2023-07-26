import logging
import json
from logging.handlers import RotatingFileHandler

class CustomFormatter(logging.Formatter):
    """Custom formatter to output logs in JSON with additional metadata"""

    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "file": record.filename,
            "line": record.lineno,
            "function": record.funcName
        }
        if record.exc_info:  # Capture exception info if available
            log_record["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_record)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = CustomFormatter()
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Rotating File Handler (max 5 files of 2MB each)
file_handler = RotatingFileHandler('app.log', maxBytes=2*1024*1024, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_formatter = CustomFormatter()
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
