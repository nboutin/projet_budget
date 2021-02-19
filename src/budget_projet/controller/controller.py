'''
@author: nboutin
'''


class Controller:

    def __init__(self, database):
        self._database = database

    def transaction_list(self):
        '''
        :return list of list
        '''
        return [list(row) for row in self._database.transaction_select()]

    def transaction_insert(self, transaction):
        return self._database.transaction_insert(transaction)

    def transaction_delete(self, id_):
        return self._database.transaction_delete(id_)

    def account_list(self):
        '''
        :return list of list
        '''
        return [list(row) for row in self._database.account_select()]

    def account_insert(self, account):
        return self._database.account_insert(account)
