from typing import Union, Dict
import sys
import logging

LOGGERS: Dict[str, logging.Logger] = {}


def get_logger(name: Union[None, str] = None) -> logging.Logger:
    """  获得一个logger 实例，用来打印日志
    Args:
        name: logger的名称
    Return:
        返回一个logger实例
    """
    global LOGGERS

    if not name:
        name = __name__

    has = LOGGERS.get(name)

    if has:
        return has

    logger = logging.getLogger(name=name)
    stream_handler = logging.StreamHandler(sys.stdout)

    LOG_LEVEL = 'DEBUG'
    LOGGING_FORMATTER = "%(levelname)s - %(asctime)s - process: %(process)d - %(filename)s - %(name)s - %(lineno)d - %(module)s - %(message)s"  # 每条日志输出格式
    logger.setLevel(LOG_LEVEL)
    stream_handler.setLevel(LOG_LEVEL)
    formatter = logging.Formatter(LOGGING_FORMATTER)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    LOGGERS.setdefault(name, logger)

    return logger
