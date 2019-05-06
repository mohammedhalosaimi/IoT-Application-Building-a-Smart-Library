# Reference: https://docs.python.org/2/library/unittest.html
import unittest
import MySQLdb
import json
import logging
from database_utils import DatabaseUtils

# class TestDatabaseUtils(unittest.TestCase):
class TestDatabaseUtils (unittest.TestCase):
    # HOST = "35.201.18.142"
    # USER = "root"
    # PASSWORD = "abc123"
    # DATABASE = "TestPeople"

    def setUp(self):
        try:
            jsonData = self.readConfig()
            HOST = jsonData["hostname"]
            USER = jsonData["user"]  
            PASSWORD = jsonData["password"]  
            DATABASE = jsonData["database"]  
            self.connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
            print("Connecting to: {}".format(DATABASE))
            self.dbUtils = DatabaseUtils(self.connection)
            self.createTestTables()
        except  Exception as e:
            print("Test DatabaseUtils error: {}".format(str(e)))

    def tearDown(self):
        try:
            self.connection.close()
        except:
            pass
        finally:
            self.connection = None

    #Wipe the data from the test DB
    def createTestTables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(open("Test_Assignment2_CreateTables.sql", "r").read())
            #cursor.execute(open("Assignment2_CreateTables.sql", "r").read())
        self.connection.commit()
    
    #Helper functions that let us poll general information.
    #****************************************
    def userExists(self, LmsUserID):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from LmsUser where LmsUserID = %s", (LmsUserID,))
            return cursor.fetchone()[0] == 1

    def bookExists(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Book where BookID = %s", (bookID,))
            return cursor.fetchone()[0] == 1

    def borrowedBookExists(self, BBId):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Person where BookBorrowed = %s", (BBId,))
            return cursor.fetchone()[0] == 1
    
    def countUsers(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from LmsUser")
            return cursor.fetchone()[0]

    def countBooks(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Book")
            return cursor.fetchone()[0]

    def countBorrowedBook(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from BookBorrowed")
            return cursor.fetchone()[0]
    
    #User CRUD Tests
    #****************************************

    #Create a User
    def test_createUser(self):
        count = self.countUsers()
        self.assertTrue(self.dbUtils.insertUser("Test", "Test"))
        self.assertTrue(count + 1 == self.countUsers())
        self.assertTrue(self.dbUtils.insertUser("Test2", "Test2"))
        self.assertTrue(count + 2 == self.countUsers())

    #Read the created User
    def test_readUser(self):
        self.assertTrue(self.dbUtils.insertUser("ReadUser", "ReaderUser"))
        #self.assertTrue(len(self.dbUtils.getUser("ReadUser"))[0] == 1)
    #Update the User

    #Delete the User
    def test_deleteUser(self):
        count = self.countUsers()
        self.assertTrue(self.dbUtils.insertUser("Test_Delete","Test_Delete"))
        self.assertTrue(count + 1 == self.countUsers())
        self.dbUtils.deleteUser(0)
        self.assertTrue(count == self.countUsers())
    #Book CRUD Tests
    #****************************************
    
    #Create a Book

    #Read the created Book

    #Update the Book

    #Delete the Book

    #BorrowedBook CRUD Tests
    #****************************************
    
    #Create a BorrowedBook

    #Read the created BorrowedBook

    #Update the BorrowedBook

    #Delete the BorrowedBook

    
    # Read the test_config.json
    def readConfig(self):
        with open('test_config.json') as jsonFile:  
            data = json.load(jsonFile)
        return data
        
        # with self.connection.cursor() as cursor:
        #     cursor.execute("drop table if exists Person")
        #     cursor.execute("""
        #         create table if not exists Person (
        #             PersonID int not null auto_increment,
        #             Name text not null,
        #             constraint PK_Person primary key (PersonID)
        #         )""")
        #     cursor.execute("insert into Person (Name) values ('Matthew')")
        #     cursor.execute("insert into Person (Name) values ('Shekhar')")
        #     cursor.execute("insert into Person (Name) values ('Rodney')")
        # self.connection.commit()


    # def tearDown(self):
    #     try:
    #         self.connection.close()
    #     except:
    #         pass
    #     finally:
    #         self.connection = None

    # def countPeople(self):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("select count(*) from Person")
    #         return cursor.fetchone()[0]

    # def personExists(self, personID):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("select count(*) from Person where PersonID = %s", (personID,))
    #         return cursor.fetchone()[0] == 1

    # def test_insertPerson(self):
    #     with DatabaseUtils(self.connection) as db:
    #         count = self.countPeople()
    #         self.assertTrue(db.insertPerson("Kevin"))
    #         self.assertTrue(count + 1 == self.countPeople())
    #         self.assertTrue(db.insertPerson("Ryan"))
    #         self.assertTrue(count + 2 == self.countPeople())

    # def test_getPeople(self):
    #     with DatabaseUtils(self.connection) as db:
    #         self.assertTrue(self.countPeople() == len(db.getPeople()))

    # def test_deletePerson(self):
    #     with DatabaseUtils(self.connection) as db:
    #         count = self.countPeople()
    #         personID = 1

    #         self.assertTrue(self.personExists(personID))

    #         db.deletePerson(personID)

    #         self.assertFalse(self.personExists(personID))
    #         self.assertTrue(count - 1 == self.countPeople())

# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    unittest.main()
