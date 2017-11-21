# -*- coding:utf-8 -*-

import logging
import sys

def get_logger(name=None, fileName = None,level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('(asctime)s %(levelname)s %(message)s')
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if fileName:
        fh = logging.FileHandler(fileName)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger