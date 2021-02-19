'''
Created on Feb 7, 2021

@author: nboutin
'''

import logging
import os
import sys

from .cmdline.args_parser import parse_args

__NAME = "Budget Projet"
__VERSION = "0.1.0-dev"

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__OUTPUT_FILEPATH = os.path.join(__location__, '{}.log'.format(__NAME.lower().replace(' ', '_')))


def main(argv):
    configure_logger()
    logging.info('{} {}'.format(__NAME, __VERSION))

    parse_args(argv)


def configure_logger():
    '''
    write to file, formatted message with log level debug
    '''
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleFormatter = logging.Formatter('%(message)s')
    consoleHandler.setFormatter(consoleFormatter)
    logger.addHandler(consoleHandler)

    fileHandler = logging.FileHandler(__OUTPUT_FILEPATH, mode='w')
    fileHandler.setLevel(logging.DEBUG)
    fileFormatter = logging.Formatter('%(message)s')
    fileHandler.setFormatter(fileFormatter)
    logger.addHandler(fileHandler)


if __name__ == '__main__':
    main(sys.argv[1:])
