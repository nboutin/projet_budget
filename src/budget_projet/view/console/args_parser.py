'''
Created on Feb 16, 2021

@author: nboutin
'''

import getopt
import sys
import logging

from . import printer


class ArgParser:
    ''' follow by ':' require an argument '''
    __SHORT_OPTS = 'h'

    '''
        follow by '=' require an argument
        optional arguments not supported
    '''
    __LONG_OPTS = ['help']

    __COMMANDS = ['transaction']

    __COMMAND_SHORT_OPTS = {'transaction': 'lau:'}
    __COMMAND_LONG_OPTS = {'transaction': ['list', 'add', 'update=']}

    def __init__(self, controller):
        self._controller = controller

    def parse_args(self, argv):
        '''
        :param argv: equal sys.argv[1:]
        '''
        logging.debug(argv)

        if argv and argv[0] in ArgParser.__COMMANDS:
            self.parse_command(argv)
            return

        try:
            opts, _ = getopt.getopt(argv, ArgParser.__SHORT_OPTS, ArgParser.__LONG_OPTS)
        except getopt.GetoptError as err:
            logging.error(err)
            self.usage()
            sys.exit(2)

        if not opts:
            opts = [('-h', None)]

        for opt, _ in opts:
            if opt in ('-h', '--help'):
                self.usage()
                sys.exit()
            else:
                logging.error('unhandled option')
                self.usage()
                sys.exit(2)

    @staticmethod
    def usage():
        logging.info('\nusage: budget_projet.py [-h] [transaction]')
        logging.info('optional arguments:')
        logging.info('-h, --help\t Show this help message and exit')
        logging.info('commands:')
        logging.info('transaction -l -a -u')
        logging.info('  -l, --list\t List all transactions')
        logging.info('  -a, --add date src dst desc credit debit\t Add a transaction')

    def parse_command(self, argv):
        cmd = argv[0]
        args = argv[1:]

        if cmd == 'transaction':
            self.parse_command_transaction(args)
        else:
            logging.error('unhandled command')

    def parse_command_transaction(self, argv):

        cmd = 'transaction'
        try:
            opts, args = getopt.getopt(
                argv, ArgParser.__COMMAND_SHORT_OPTS[cmd], ArgParser.__COMMAND_LONG_OPTS[cmd])
        except getopt.GetoptError as err:
            logging.error(err)
            self.usage()
            sys.exit(2)

        if not opts:
            opts = [('-h', None)]

        for opt, _ in opts:
            if opt in ('-h', '--help'):
                self.usage()
                sys.exit()
            elif opt in ('-l', '--list'):
                data = self._controller.transaction_list()
                printer.transaction_list(data)
            elif opt in ('-a', '--add'):
                self._controller.transaction_add(args)
            else:
                logging.error('unhandled {} option'.format(cmd))
                self.usage()
                sys.exit(2)
