'''
@author: nboutin
'''

# Date and Time datatype
# TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").

test_table = """
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            );
        """

transaction_table = """
    CREATE TABLE TRANSACTION_ (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        account_src TEXT,
        account_dst TEXT,
        description TEXT,
        credit INTEGER,
        debit INTEGER
    );"""

transaction_select = 'SELECT * FROM TRANSACTION_'

transaction_insert = '''
    INSERT INTO
        TRANSACTION_ (date, account_src, account_dst, description, credit, debit)
        values(?, ?, ?, ?, ?, ?)'''
