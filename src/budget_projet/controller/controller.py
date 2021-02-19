'''
@author: nboutin
'''


class Controller:

    def __init__(self, database):
        self._database = database

    def transaction_list(self):
        return [row for row in self._database.transaction_select()]

    def transaction_add(self, transaction):
        return self._database.transaction_insert(transaction)
