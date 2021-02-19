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
__LONG_OPTS = ['help']

__COMMANDS = ['transaction']

__COMMAND_SHORT_OPTS = {'transaction': 'la:u:'}
__COMMAND_LONG_OPTS = {'transaction': ['list', 'add=', 'update=']}


def parse_args(argv):
    '''
    :param argv: equal sys.argv[1:]
    '''
    logging.debug(argv)

    if argv and argv[0] in __COMMANDS:
        parse_command(argv)
        return

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
    logging.info('\nusage: budget_projet.py [-h] [transaction]')
    logging.info('optional arguments:')
    logging.info('-h, --help\t Show this help message and exit')
    logging.info('commands:')
    logging.info('transaction -l -a -u')
    logging.info('  -l, --list\t List all transactions')


def parse_command(argv):
    cmd = argv[0]
    args = argv[1:]

    if cmd == 'transaction':
        parse_command_transaction(args)
    else:
        logging.error('unhandled command')


def parse_command_transaction(argv):

    cmd = 'transaction'
    try:
        opts, args = getopt.getopt(argv, __COMMAND_SHORT_OPTS[cmd], __COMMAND_LONG_OPTS[cmd])
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
        elif opt in ('-l', '--list'):
            pass
        else:
            logging.error('unhandled {} option'.format(cmd))
            usage()
            sys.exit(2)
