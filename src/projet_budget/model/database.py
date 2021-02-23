'''
@author: nboutin
'''

import logging
import sqlite3 as sl
from ..model import request


class Database:

    def __init__(self, pathname):

        self._con = sl.connect(pathname)

        self._execute(request.foreign_key)
        self._create_table(request.account_table)
        self._create_table(request.transaction_table)

    def _execute(self, request):
        logging.debug(request)
        try:
            with self._con:
                self._con.execute(request)
        except (sl.ProgrammingError, sl.OperationalError, sl.IntegrityError) as e:
            logging.error(e)
            return False
        else:
            return True

    def _create_table(self, table):
        try:
            with self._con:
                self._con.execute(table)
        except (sl.ProgrammingError, sl.OperationalError, sl.IntegrityError) as e:
            logging.debug(e)
            pass

    def account_select(self):
        with self._con:
            return self._con.execute(request.account_select).fetchall()

    def account_insert(self, name):
        '''
        :param name: string
        '''
        try:
            with self._con:
                self._con.execute(request.account_insert, (name,))
        except (sl.ProgrammingError, sl.OperationalError, sl.IntegrityError) as e:
            logging.error(e)
            logging.error(name)
            return False
        else:
            return self._account_view(name)

    def _account_view(self, name):
        req = request._account_view.format(name, name)
        return self._execute(req)

    def account_delete(self, id_):
        '''
        :param id_: int
        '''
        try:
            with self._con:
                return self._con.execute(request.account_delete, (id_,))
        except (sl.ProgrammingError, sl.OperationalError, sl.IntegrityError) as e:
            logging.error(e)
            logging.error(id_)

    def transaction_select(self):
        with self._con:
            return self._con.execute(request.transaction_select)

    def transaction_insert(self, transaction):
        '''
        :param transaction: list
        '''
        try:
            with self._con:
                return self._con.executemany(request.transaction_insert, (transaction,))
        except (sl.ProgrammingError, sl.OperationalError, sl.IntegrityError) as e:
            logging.error(e)
            logging.error(transaction)
            return False

    def transaction_delete(self, id_):
        '''
        :param id_: int
        '''
        try:
            with self._con:
                return self._con.execute(request.transaction_delete, (id_,))
        except (sl.ProgrammingError, sl.OperationalError, sl.IntegrityError) as e:
            logging.error(e)
            logging.error(id_)
