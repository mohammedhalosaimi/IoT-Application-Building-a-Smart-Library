# Reference: https://docs.python.org/2/library/unittest.html
import unittest
import MySQLdb
import json
import logging
from database_utils import DatabaseUtils

class TestDatabaseUtils (unittest.TestCase):

    def setUp(self):
        try:
            jsonData = self.readConfig()
            HOST = jsonData["hostname"]
            USER = jsonData["user"]  
            PASSWORD = jsonData["password"]  
            DATABASE = jsonData["database"]  
            self.connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
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
            count = cursor.fetchone()[0]
            print("The book count is {}".format(count))
            return count

    def countBorrowedBook(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from BookBorrowed")
            return cursor.fetchone()[0]
    
    #User CRUD Tests
    #****************************************

    #Create a User
    #TODO Finalise the MP SQL
    """
    def test_createUser(self):
        count = self.countUsers()
        self.assertTrue(self.dbUtils.insertUser("Test", "Test"))
        self.assertTrue(count + 1 == self.countUsers())
        self.assertTrue(self.dbUtils.insertUser("Test2", "Test2"))
        self.assertTrue(count + 2 == self.countUsers())

    #Read the created User
    def test_readUser(self):
        self.assertTrue(self.dbUtils.insertUser("ReadUser", "ReaderUser"))
    #Update the User

    #Delete the User
    def test_deleteUser(self):
        count = self.countUsers()
        self.assertTrue(self.dbUtils.insertUser("Test_Delete","Test_Delete"))
        self.assertTrue(count + 1 == self.countUsers())
        self.dbUtils.deleteUser(0)
        self.assertTrue(count == self.countUsers())
    """
    #Book CRUD Tests
    #****************************************
    
    #Create a Book
    def test_insertBook(self):
        title = "Test Book 1"
        author = "None"
        publishedDate = "20190508"
        #ISBN: 978-3-16-148410-0
        count = self.countBooks()
        self.assertTrue(self.dbUtils.insertBook(title, author, publishedDate))
        self.assertTrue(count + 1 == self.countBooks)
        
    #Read the created Book
    def test_readBook(self):
        title = "Read Book 1"
        author = "None"
        publishedDate = "20190508"
        #ISBN: 978-3-16-148410-0
        self.assertTrue(self.dbUtils.insertBook(title, author, publishedDate))
        searchResult = self.dbUtils.getBookByTitle(title)
        #Search the results for the book added.
        for results in searchResult:
            if(results[1] == title):
                self.assertTrue(True)
                return
        print("No Book was found with the title {}".format(title))
        self.assertTrue(False)
    #Update the Book

    #Delete the Book
    def test_deleteBook(self):
        title = "Delete Book 1"
        author = "Deleter"
        publishedDate = "20190508"
        #ISBN: 978-3-16-148410-0
        count = self.countBooks()
        self.assertTrue(self.dbUtils.insertBook(title, author, publishedDate))
        searchResult = self.dbUtils.getBookByAuthor(author)
        for results in searchResult:
            self.dbUtils.deleteBook(results[0])
            self.assertTrue(count - 1 == self.countBooks)
            count -= 1


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

if __name__ == "__main__":
    unittest.main()
