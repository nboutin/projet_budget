'''
@author: nboutin
'''
import unittest
import os

from projet_budget.model.database import Database

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
DB_PATHNAME = os.path.join(__location__, 'test.db')


class TestDatabase(unittest.TestCase):

    def tearDown(self):
        os.remove(DB_PATHNAME)

    def test1a_init(self):
        '''open non existing database'''
        db = Database(DB_PATHNAME)

    def test1b_init(self):
        '''open existing database'''
        db1 = Database(DB_PATHNAME)
        db2 = Database(DB_PATHNAME)

    def test2a_account(self):
        '''list empty account'''
        db = Database(DB_PATHNAME)
        self.assertEqual(db.account_select().fetchone(), None)
        self.assertEqual(db.account_select().fetchall(), [])


if __name__ == "__main__":
    unittest.main()
