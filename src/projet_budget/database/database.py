'''
@author: nboutin
'''

import logging
import sqlite3 as sl
from projet_budget.database import request


class Transaction:

    def __init__(self, date, account_src, account_dst, description, credit, debit):
        self.date = date
        self.account_src = account_src
        self.account_dst = account_dst
        self.description = description
        self.credit = credit
        self.debit = debit

    def list(self):
        return (self.date, self.account_src, self.account_dst, self.description, self.credit, self.debit)


class Database:

    def __init__(self, pathname):

        self._con = sl.connect(pathname)

        self._create_tables()

    def _create_tables(self):

        try:
            with self._con:
                self._con.execute(request.transaction_table)
        except sl.OperationalError as e:
            logging.debug(e)
            pass

    def transaction_select(self):
        with self._con:
            return self._con.execute(request.transaction_select)

    def transaction_insert(self, transaction):
        '''
        :param transaction: type Transaction
        '''
        with self._con:
            self._con.executemany(request.transaction_insert, transaction.list())
