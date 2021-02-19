'''
@author: nboutin
'''

import logging
import sqlite3 as sl
from ..model import request


class Database:

    def __init__(self, pathname):

        self._con = sl.connect(pathname)

        self._create_tables()

    def _create_tables(self):

        try:
            with self._con:
                return self._con.execute(request.transaction_table)
        except sl.OperationalError as e:
            logging.debug(e)
            pass

    def transaction_select(self):
        with self._con:
            return self._con.execute(request.transaction_select)

    def transaction_insert(self, transaction):
        try:
            with self._con:
                return self._con.executemany(request.transaction_insert, (transaction,))
        except sl.ProgrammingError as e:
            logging.error(e)
            logging.error(transaction)
            return False

    def transaction_delete(self, id_):

        id_ = int(id_[0])

        try:
            with self._con:
                return self._con.execute(request.transaction_delete, (id_,))
        except sl.InterfaceError as e:
            logging.error(e)
            logging.error(id_)
