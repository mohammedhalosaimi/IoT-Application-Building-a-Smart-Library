import MySQLdb
import json
import logging

logging.basicConfig(filename="library.log", level = logging.ERROR)
class DatabaseUtils:

    def __init__(self, connection = None):
        if(connection == None):
            try:
                jsonData = self.readConfig()
                HOST = jsonData["hostname"]
                USER = jsonData["user"]  
                PASSWORD = jsonData["password"]  
                DATABASE = jsonData["database"]
                print("Connecting to: {}".format(DATABASE))
                connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
            except  Exception as e:
                print("DatabaseUtils error: {}".format(str(e)))
        self.connection = connection
        print(self.connection)
        self.createTables()


    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createTables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(open("Assignment2_CreateTables.sql", "r").read())
        self.connection.commit()

    # User CRUD table
    # ****************************************
    # Insert user
    def insertUser(self, userName, name):
        with self.connection.cursor() as cursor:
            cursor.execute("""insert into LmsUser 
                (UserName, Name) values (%(username)s,%(name)s)""",
                {'username': userName, 'name': name})
        self.connection.commit()

        return cursor.rowcount == 1

    # Get user
    def getUser(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute("select * from LmsUser Where UserName = %s", (name,))
            return cursor.fetchall()

    # Get user
    def getUsers(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select * from LmsUser")
            return cursor.fetchall()

    # Delete User
    def deleteUser(self, lmsUserID):
        with self.connection.cursor() as cursor:
            cursor.execute("delete from LmsUser where LmsUserID = %s", (lmsUserID,))
        self.connection.commit()


    # Book CRUD table
    # ****************************************
    # Insert Book
    def insertBook(self, title, author, publishedDate):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Book (Title, Author, PublishedDate) values (%s)", (title,author, publishedDate))
        self.connection.commit()

        return cursor.rowcount == 1

    # Get Book by title
    def getBookByTitle(self, title):
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where Title = %s", (title,))
            return cursor.fetchall()

    # Get Book by Author
    def getBookByAuthor(self, author):
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where Author = %s", (author,))
            return cursor.fetchall()

    # Get Book by PublishedDate
    def getBookByPublishedDate(self, publishedDate):
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where PublishedDate = %s", (publishedDate,))
            return cursor.fetchall()

    # Delete Book
    def deletePerson(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute("delete from Book where BookID = %s", (bookID,))
        self.connection.commit()


    # BookBorrowed CRUD table
    # ****************************************
    # Insert BookBorrowed record
    def insertBookBorrowed(self, lmsUserID, bookID, status, borrowdDate, returnDate):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into BookBorrowed (LmsUserID, BookID, Status, BorrowedDate, ReturnedDate) values (%s)", (lmsUserID,bookID, status, borrowdDate, returnDate))
        self.connection.commit()

        return cursor.rowcount == 1

    # Get user
    def getBookBorrowed(self, lmsUserID, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute("select * from BookBorrowed Where LmsUserID = "+ lmsUserID +" AND BookID = "+ bookID)
            return cursor.fetchall()

    # Delete User
    def deleteBookBorrowed(self, bookBorrowedID):
        with self.connection.cursor() as cursor:
            cursor.execute("delete from BookBorrowed where BookBorrowedID != %s", (bookBorrowedID,))
        self.connection.commit()




    # Read config.json
    def readConfig(self):
        with open('config.json') as jsonFile:  
            data = json.load(jsonFile)
        return data
