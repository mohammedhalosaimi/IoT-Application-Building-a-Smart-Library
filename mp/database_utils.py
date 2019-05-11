#!/usr/bin/python3

import MySQLdb
# import pymysql
import json
import logging

logging.basicConfig(filename="library.log", level = logging.ERROR)
class DatabaseUtils:

    def __init__(self):
        """

        Parameters:

        Returns:

        """
        try:
            jsonData = self.readConfig()
            HOST = jsonData["hostname"]
            USER = jsonData["user"]  
            PASSWORD = jsonData["password"]  
            DATABASE = jsonData["database"]  

            self.connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
            print(self.connection)
            self.createTables()
        except  Exception as e:
            print("DatabaseUtils error: {}".format(str(e)))

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createTables(self):
        """
        Create tables into the databse as per Assignment2_CreateTables.sql file if does not exist
        Parameters:

        Returns:

        """
        with self.connection.cursor() as cursor:
            cursor.execute(open("Assignment2_CreateTables.sql", "r").read())
        self.connection.commit()

    # User CRUD table
    # ****************************************
    # Insert user
    def insertUser(self, name):
        """
        Insert loggedin user who borrows a book into the google cloud db
        Parameters:
        User name
        Returns:
            1 if the user is added
        """
        with self.connection.cursor() as cursor:
            cursor.execute("insert into LmsUser (UserName) values (%s)", (name,))
        self.connection.commit()

        return cursor.rowcount == 1

    # Get user
    def getUser(self, name):
        """
        Get the user name from the cloud if already borrowed a book
        Parameters:
            User name
        Returns:
            returns user if borrowed a book in the past
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from LmsUser Where UserName = %s", (name,))
            return cursor.fetchall()

    # Get user
    def getUsers(self):
        """
        Fetch all users from the cloud
        Parameters:

        Returns:
        List of all users
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from LmsUser")
            return cursor.fetchall()

    # Delete User
    def deleteUser(self, lmsUserID):
        """
        Delete a user from the cloud 
        Parameters:
        LMS user ID
        Returns:

        """
        with self.connection.cursor() as cursor:
            cursor.execute("delete from LmsUser where LmsUserID = %s", (lmsUserID,))
        self.connection.commit()


    # Book CRUD table
    # ****************************************
    # Insert Book
    def insertBook(self, title, author, isbn):
        """
        Insert a book into the cloud db
        Parameters:
            Book Name, Book author, ISBN
        Returns:
            Confirms if the book is registered
        """
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Book (Title, Author, ISBN) values (%s, %s, %s)", (title,author, isbn))
        self.connection.commit()

        return cursor.rowcount == 1

    # Get Book by title
    def getBookByTitle(self, title):
        """
        Fetch all the books containing the keyword in the title
        Parameters:
            Title of the book or part of the title
        Returns:
            All books contating the keyword
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where Title Like %s", ("%" + title + "%",))
            return cursor.fetchall()

    # Get Book by Author
    def getBookByAuthor(self, author):
        """
        Fetch all the books containing the keyword in the author
        Parameters:
            author of the book or part of the author
        Returns:
            All books contating the keyword
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where Author Like %s", ("%" + author + "%",))
            return cursor.fetchall()

    # Get Book by ISBN
    def getBookByISBN(self, isbn):
        """
        Fetch all the books containing the keyword in the isbn
        Parameters:
            isbn of the book or part of the isbn
        Returns:
            All books contating the keyword
        """

        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where ISBN Like %s", ("%" + isbn + "%",))
            return cursor.fetchall()

        # Get Book by ISBN
    def getBooks(self):
        """
        Returns all the book in the cloud db
        Parameters:

        Returns:
            Returns all the book in the cloud db

        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book")
            return cursor.fetchall()

    # Delete Book
    def deleteBook(self, bookID):
        """
        Delete a book 
        Parameters:
            Book ID
        Returns:

        """
        with self.connection.cursor() as cursor:
            cursor.execute("delete from Book where BookID = %s", (bookID,))
        self.connection.commit()


    # BookBorrowed CRUD table
    # ****************************************
    # Insert BookBorrowed record
    def insertBookBorrowed(self, lmsUserID, bookID, status, borrowdDate):
        """
        Allocate a book to a user who borrowed the book, mark the book as borrowed and insett the borrowed date 
        Parameters:

        Returns:

        """
        with self.connection.cursor() as cursor:
            cursor.execute("insert into BookBorrowed (LmsUserID, BookID, Status, BorrowedDate) values (%s, %s, %s, %s)", (lmsUserID,bookID, status, borrowdDate))
        self.connection.commit()

        return cursor.rowcount == 1


    # Insert BookBorrowed record
    def updateBookBorrowed(self, lmsUserID, bookID, status, ReturnedDate):
        """
        Update a book which the user returns to the library, change the status to returned and insert the return date 
        Parameters:
            LMS user ID, Book ID, Status=returned,  
        Returns:

        """
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE BookBorrowed SET Status = %s , ReturnedDate = %s WHERE LmsUserID = %s AND BookID = %s", (status, ReturnedDate, lmsUserID,bookID))
        self.connection.commit()

        return cursor.rowcount == 1

    # Get user
    def getBookBorrowed(self, lmsUserID, bookID):
        """
        Get the user's borrowed book status 
        Parameters:
            LMS USER ID, BOOK ID
        Returns:
            user's borrowed book record 
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from BookBorrowed Where LmsUserID = "+ lmsUserID +" AND BookID = "+ bookID)
            return cursor.fetchall()

    # Delete User
    def deleteBookBorrowed(self, bookBorrowedID):
        """
        Delete all borrowed books with the bookBorrowedID
        Parameters:
            Id of the borrowed book(s)
        Returns:

        """
        with self.connection.cursor() as cursor:
            cursor.execute("delete from BookBorrowed where BookBorrowedID != %s", (bookBorrowedID,))
        self.connection.commit()




    # Read config.json
    def readConfig(self):
        """
        Fetch configuration data to connect to google cloud database
        Parameters:

        Returns:
            google cloud database parameters
        """
        with open('config.json') as jsonFile:  
            data = json.load(jsonFile)
        return data

# DatabaseUtils().getUsers()
