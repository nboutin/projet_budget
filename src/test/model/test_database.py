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
        _ = Database(DB_PATHNAME)

    def test1b_init(self):
        '''open existing database'''
        _ = Database(DB_PATHNAME)
        _ = Database(DB_PATHNAME)

    def test2a_account(self):
        '''list empty account'''
        db = Database(DB_PATHNAME)
        self.assertEqual(db.account_select(), [])
        self.assertEqual(db.account_select(), [])

    def test2b_account(self):
        '''account insert'''
        db = Database(DB_PATHNAME)
        self.assertTrue(db.account_insert('name'))
        self.assertTrue(db.account_insert("name with space"))

    def test2c_account(self):
        '''list account'''
        db = Database(DB_PATHNAME)
        result = list()
        for i, name in enumerate(['name', 'my account', 'cchq', 'ldd']):
            db.account_insert(name)
            result.append((i + 1, name))

        self.assertEqual(db.account_select(), result)

    def test2d_account(self):
        '''account delete'''
        db = Database(DB_PATHNAME)
        result = list()
        for i, name in enumerate(['name', 'my account', 'cchq', 'ldd']):
            db.account_insert(name)
            result.append((i + 1, name))

        self.assertTrue(db.account_delete(3))
        del result[2]
        self.assertEqual(db.account_select(), result)


if __name__ == "__main__":
    unittest.main()
