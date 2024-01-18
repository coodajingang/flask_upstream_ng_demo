import logging
from logging.handlers import RotatingFileHandler

def configure_logger(logger_name='my_app'):
    # 如果记录器已存在，直接返回
    if logger_name in logging.root.manager.loggerDict:
        return logging.getLogger(logger_name)
    logger = logging.getLogger('my_app')
    logger.setLevel(logging.DEBUG)

    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(module)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    log_handler = RotatingFileHandler('app.log', maxBytes=10*1024*1024, backupCount=5)
    log_handler.setFormatter(log_formatter)

    logger.addHandler(log_handler)

    return logger
