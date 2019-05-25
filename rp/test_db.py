# Reference: https://docs.python.org/2/library/unittest.html
import unittest
from db import database

# Reference: https://docs.python.org/2/library/unittest.html
import unittest
from db import database
from passlib.hash import sha256_crypt
class db_test(unittest.TestCase):
    def setUp(self):
        self.c=database.connection().cursor()
        self.hashedPassword = sha256_crypt.hash("TestPassword")
        database.insertData("TestUsername",self.hashedPassword,"TestFirstName","TestLastName","123123@123.com")
    def test_createTables(self):
        self.c=database.connection().cursor()
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='account'")
        name=self.c.fetchone()[0]
        self.assertEqual(name,"account")
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
        name=self.c.fetchone()[0]
        self.assertEqual(name,"user")
    
    def test_insertData(self):
        self.c.execute("SELECT count(*) from user where username='TestUsername' and password=%(password)s and firstname='TestFirstName' and lastname='TestLastName' and email='123123@123.com'",{"password":hashedPassword})
        result=self.c.fetchone()[0]
        self.assertEqual(int(result),1)
    
    def test_verifyPassword(self):
        self.assertTrue(database.veriftPassword("TestUsername",self.hashedPassword))
    
    def test_checkUsernameExists(self):
        self.assertFalse(database.checkusernameexists("TestUsername"))

if __name__ == "__main__":
    unittest.main()