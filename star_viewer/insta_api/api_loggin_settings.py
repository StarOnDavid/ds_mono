import logging
import sys
from logging import Logger

file_handler = logging.FileHandler(filename='tmp.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)


def get(name):
    print(name)
    if name == 'star_viewer.insta_api.connection':
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        # logger.setLevel(logging.DEBUG)
        return logger

    if name == 'star_viewer.insta_api.connect_instagram_private_api':
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        # logger.setLevel(logging.DEBUG)
        return logger

    if name == 'easy_insta_api.filehandler':
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        # logger.setLevel(logging.DEBUG)
        return logger
