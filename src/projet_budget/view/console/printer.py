'''
@author: nboutin
'''

import logging


def transaction_list(data):
    for row in data:
        logging.info(row)
