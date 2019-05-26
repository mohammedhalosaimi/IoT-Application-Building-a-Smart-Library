# Reference: https://docs.python.org/2/library/unittest.html
import unittest
import MySQLdb
from database_utils import DatabaseUtils

class TestDatabaseUtils(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseUtils()

    def test_getBookByISBN(self,):
        result = self.db.getBookByISBN('9781925483598')
        print(result)
        self.assertTrue(result[0][2],"THE SUBTLE ART OF NOT GIVING A FUCK")

    def test_getBookByTitle(self,):
        result = self.db.getBookByTitle('test')
        self.assertTrue(result.count,0)

    def test_getBookByAuthor(self,):
        result = self.db.getBookByAuthor('MARK MANSON')
        print(result)
        self.assertTrue(result[0][2],"THE SUBTLE ART OF NOT GIVING A FUCK")



if __name__ == "__main__":
    unittest.main()


