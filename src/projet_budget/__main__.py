'''
Created on Feb 7, 2021

@author: nbout
'''

import logging
import os

__NAME = "Budget Projet"
__VERSION = "0.1.0"

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__OUTPUT_FILEPATH = os.path.join(__location__, 'budget_projet.log')


def main():
    configure_logger()
    logging.info('{} {}\n'.format(__NAME, __VERSION))


def configure_logger():
    '''
    write to file, formatted message with log level debug
    '''
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(__OUTPUT_FILEPATH, mode='w')
    fileHandler.setLevel(logging.DEBUG)
    fileFormatter = logging.Formatter('%(message)s')
    fileHandler.setFormatter(fileFormatter)
    logger.addHandler(fileHandler)


if __name__ == '__main__':
    main()
