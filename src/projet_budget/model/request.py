'''
@author: nboutin
'''

foreign_key = "PRAGMA foreign_keys = 1"

# Date and Time datatype
# TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
transaction_table = """
   CREATE TABLE TRANSACTION_ (
    id          INTEGER PRIMARY KEY AUTOINCREMENT
                        UNIQUE
                        NOT NULL,
    date        TEXT    NOT NULL,
    account_src TEXT    REFERENCES ACCOUNT (name),
    account_dst TEXT    REFERENCES ACCOUNT (name),
    description TEXT,
    credit      INTEGER NOT NULL,
    debit       INTEGER NOT NULL
);"""

transaction_select = 'SELECT * FROM TRANSACTION_'

transaction_insert = """
    INSERT INTO
        TRANSACTION_ (date, account_src, account_dst, description, credit, debit)
        values (?, ?, ?, ?, ?, ?)"""

transaction_delete = 'DELETE FROM TRANSACTION_ WHERE id=?'

account_table = """
    CREATE TABLE ACCOUNT (
    id   INTEGER PRIMARY KEY AUTOINCREMENT
                 UNIQUE
                 NOT NULL,
    name TEXT    NOT NULL
                 UNIQUE
);"""

account_select = 'SELECT * FROM ACCOUNT'

account_insert = 'INSERT INTO ACCOUNT (name) values (?)'
