'''
@author: nboutin
'''

import os
import logging

from ..database.database import Database

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__DB_PATHNAME = os.path.join(__location__, 'project_budget.db')


def transaction_list():

    db = Database(__DB_PATHNAME)
    for row in db.transaction_select():
        logging.info(row)
