import logging
import os
import json

class CustomFormatter(logging.Formatter):
    """Custom formatter, overrides funcName with value of funcname if it exists"""
    def format(self, record):
        if hasattr(record, 'funcname'):
            record.funcName = record.funcname
        return super().format(record)

class JsonLogger:
    """Logger that outputs log messages in JSON format."""

    def __init__(self, name, log_file=None):
        """Create an instance of JsonLogger.

        If log_file is specified, log output will be written to that file,
        otherwise log output will go to the console.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = CustomFormatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s,'
            ' "file": "%(filename)s", "funcName": "%(funcName)s", "lineno": %(lineno)d}\n',
            "%Y-%m-%d %H:%M:%S")
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        else:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def _log(self, level, msg, **kwargs):
        """Log a message at a specified level.

        The message can include placeholders for variable data, which are
        provided as keyword arguments.
        """
        if kwargs:
            msg += ": " + ', '.join(f'{k}={v}' for k, v in kwargs.items())
        self.logger.log(level, msg)

    def debug(self, msg, **kwargs):
        self._log(logging.DEBUG, msg, **kwargs)

    def info(self, msg, **kwargs):
        self._log(logging.INFO, msg, **kwargs)

    def warning(self, msg, **kwargs):
        self._log(logging.WARNING, msg, **kwargs)

    def error(self, msg, **kwargs):
        self._log(logging.ERROR, msg, **kwargs)

    def exception(self, msg, **kwargs):
        self._log(logging.ERROR, msg, **kwargs)
        self.logger.exception(msg)
