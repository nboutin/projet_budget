'''
Created on Feb 16, 2021

@author: nboutin
'''

import getopt
import sys
import logging

''' follow by ':' require an argument '''
__SHORT_OPTS = 'h'

'''
    follow by '=' require an argument
    optional arguments not supported
'''
__LONG_OPTS = ['--help']


def parse_args(argv):
    '''
    :param argv: equal sys.argv[1:]
    '''
    try:
        opts, args = getopt.getopt(argv, __SHORT_OPTS, __LONG_OPTS)
    except getopt.GetoptError as err:
        logging.error(err)
        usage()
        sys.exit(2)

    if not opts:
        opts = [('-h', None)]

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        else:
            logging.error('unhandled option')
            usage()
            sys.exit(2)


def usage():
    logging.info('usage: budget_projet.py [-h]')
    logging.info('optional arguments:')
    logging.info('-h, --help\t Show this help message and exit')
