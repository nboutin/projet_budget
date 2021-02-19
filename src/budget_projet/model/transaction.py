'''
@author: nboutin
'''


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
