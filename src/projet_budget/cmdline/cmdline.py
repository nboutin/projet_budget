'''
Created on Feb 16, 2021

@author: nbout
'''

import getopt

'''
[command] [args]

transactions --list -l --add -a --update -u

'''


def parse_args(argv):

    inputfile = None

    try:
        opts, _ = getopt.getopt(argv, 'i:h', [])
    except getopt.GetoptError:
        print_help()
        quit()

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            quit()
        elif opt in ('-i'):
            inputfile = arg

    return inputfile


def print_help():
    print('-i input file')
    print('-h help')
