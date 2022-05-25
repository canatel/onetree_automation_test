from logging import getLogger, Logger, StreamHandler, INFO
from logging.handlers import TimedRotatingFileHandler


def build_logger() -> Logger:
    logger = getLogger(__name__)
    filename = 'logfile.log'
    handlers = [
        TimedRotatingFileHandler(filename, when="h", interval=1),
        StreamHandler()
    ]
    for handler in handlers + [logger]:
        handler.setLevel(INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    for handler in handlers:
        logger.addHandler(handler)

    return logger
