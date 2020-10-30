from datetime import date
import logging
import sys
import time


def getLogger(name=__name__):

    # Change here if you want another date format
    formatter = logging.Formatter(
        fmt="%(asctime)s UTC %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Change here if you want change the file name
    handler = logging.FileHandler(
        filename="{}-log.txt".format(str(date.today())))
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logging.Formatter.converter = time.gmtime
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger
