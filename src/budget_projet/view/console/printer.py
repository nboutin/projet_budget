'''
@author: nboutin
'''

import logging
from tabulate import tabulate


def transaction_list(data):

    table = []
    table.append(['Id', 'Date', 'Account Source', 'Account Destination', 'Description', 'Credit', 'Debit'])
    for row in data:
        table.append(row)
    logging.info(tabulate(table, headers="firstrow"))
