import logging

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_file_handler():
    file_handler = logging.FileHandler("/var/log/cicflowmeter/cicflowmeter.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name: str, level: int = logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
