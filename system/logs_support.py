import config
import logging
import sys


def init_logger(mainLoggerName=__name__):
    logger = logging.getLogger(mainLoggerName)

    # create formatter
    formatter = logging.Formatter(config.LOG_FORMAT)

    # adding console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(config.LOG_LEVEL)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.setLevel(config.LOG_LEVEL)
    return logger
