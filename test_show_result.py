#chech connectivity with DB

from os import access
import unittest
import authentications as au, psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

def result():
    try:
        conn = psycopg2.connect(au.connection_string)

        cur = conn.cursor()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur.execute("""SELECT version();""")
        vacuum1 = cur.fetchall()
        for t1 in vacuum1:
            return True
    except psycopg2.OperationalError as e:

        return 

    finally:

        if conn:
            conn.close()

class test_db_connectivity(unittest.TestCase):
    def test_connectivity(self):
        self.assertTrue(True, result())

if __name__ == '__main__':
    unittest.main()
        
