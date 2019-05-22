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
            # print(self.connection)
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
        Create tables into the databse as per cloud_db_schema.sql file if does not exist
        Parameters:

        Returns:

        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(open("cloud_db_schema.sql", "r").read())
            self.connection.commit()
        except:
            print("ip address not authorised by google cloud")

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
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("insert into LmsUser (UserName) values (%s)", (name,))
            self.connection.commit()

            return cursor.rowcount == 1
        except:
            print("ip address not authorised by google cloud")

    # Get user
    def getUser(self, name):
        """
        Get the user name from the cloud if already borrowed a book
        Parameters:
            User name
        Returns:
            returns user if borrowed a book in the past
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from LmsUser Where UserName = %s", (name,))
                if cursor.rowcount > 0:
                    return True
                else:
                    return False
        except:
            print("ip address not authorised by google cloud")

    # Get user
    def getUsers(self):
        """
        Fetch all users from the cloud
        Parameters:

        Returns:
        List of all users
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from LmsUser")
                return cursor.fetchall()
        except:
            print("ip address not authorised by google cloud")

    # Delete User
    def deleteUser(self, name):
        """
        Delete a user from the cloud 
        Parameters:
        LMS user ID
        Returns:

        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("delete from LmsUser where UserName = %s", (name,))
            self.connection.commit()
        except:
            print("ip address not authorised by google cloud")


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
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("insert into Book (Title, Author, ISBN) values (%s, %s, %s)", (title,author, isbn))
            self.connection.commit()

            return cursor.rowcount == 1
        except:
            print("ip address not authorised by google cloud")

    # Get Book by title
    def getBookByTitle(self, title):
        """
        Fetch all the books containing the keyword in the title
        Parameters:
            Title of the book or part of the title
        Returns:
            All books contating the keyword
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from Book Where Title Like %s", ("%" + title + "%",))
                return cursor.fetchall()
        except:
            print("ip address not authorised by google cloud")

    # Get Book by Author
    def getBookByAuthor(self, author):
        """
        Fetch all the books containing the keyword in the author
        Parameters:
            author of the book or part of the author
        Returns:
            All books contating the keyword
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from Book Where Author Like %s", ("%" + author + "%",))
                return cursor.fetchall()
        except:
            print("ip address not authorised by google cloud")

    # Get Book by ISBN
    def getBookByISBN(self, isbn):
        """
        Fetch all the books containing the keyword in the isbn
        Parameters:
            isbn of the book or part of the isbn
        Returns:
            All books contating the keyword
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from Book Where ISBN Like %s", ("%" + isbn + "%",))
                return cursor.fetchall()
        except:
            print("ip address not authorised by google cloud")

    # Get Book by book ID
    def getBookByID(self, bookID):
        """
        Fetch all the books containing the keyword in the bookID
        Parameters:
            isbn of the book or part of the isbn
        Returns:
            All books contating the keyword
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from Book Where BookID Like %(BookID)s", {"BookID":bookID})
                return cursor.fetchall()
        except:
            print("ip address not authorised by google cloud")

        # Get Book by ISBN
    def getBooks(self):
        """
        Returns all the book in the cloud db
        Parameters:

        Returns:
            Returns all the book in the cloud db

        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from Book")
                return cursor.fetchall()
        except:
            print("ip address not authorised by google cloud")

    # Delete Book
    def deleteBook(self, bookID):
        """
        Delete a book 
        Parameters:
            Book ID
        Returns:

        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("delete from Book where BookID = %s", (bookID,))
            self.connection.commit()
        except:
            print("ip address not authorised by google cloud")


    # BookBorrowed CRUD table
    # ****************************************
    # Insert BookBorrowed record
    def insertBookBorrowed(self, name, bookID, status, borrowdDate):
        """
        Allocate a book to a user who borrowed the book, mark the book as borrowed and insert the borrowed date 
        Parameters:

        Returns:

        """
        try :
            with self.connection.cursor() as cursor:
                cursor.execute("insert into BookBorrowed (UserName, BookID, Status, BorrowedDate) values (%s, %s, %s, %s)", (name,bookID, status, borrowdDate))
                # cursor.execute("insert into BookBorrowed (UserName, BookID, Status, BorrowedDate) values (%(UserName)s, %(BookID)s, %(Status)s, %(BorrowedDate)s)", {'UserName':name,"BookID":'bookID', 'Status':status, 'BorrowedDate':borrowdDate})
                # cursor.execute("insert into BookBorrowed Where BookID = %(BookID)s AND Status = %(Status)s", {'BookID':bookID,"Status":'borrowed'})
            self.connection.commit()
        except:
            print("ip address not authorised by google cloud")
        # return cursor.rowcount == 1


    # Insert BookBorrowed record
    def updateBookBorrowed(self, name, bookID, status, ReturnedDate):
        """
        Update a book which the user returns to the library, change the status to returned and insert the return date 
        Parameters:
            LMS user ID, Book ID, Status=returned,  
        Returns:

        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE BookBorrowed SET Status = %s , ReturnedDate = %s WHERE UserName = %s AND BookID = %s", (status, ReturnedDate, name,bookID))
            self.connection.commit()

            return cursor.rowcount == 1
        except:
            print("ip address not authorised by google cloud")

    # Get user
    def getBookBorrowed(self, name, bookID):
        """
        Get the user's borrowed book status 
        Parameters:
            LMS USER ID, BOOK ID
        Returns:
            user's borrowed book record 
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from BookBorrowed Where UserName = "+ name +" AND BookID = "+ bookID)
                return cursor.fetchall()
        except:
            print("ip address not authorised by google cloud")

    # The 2 methods below are new 

    def getAvilableBook(self, bookID):
        """
        This method checks if the book that is associated with the bookID is avilable to borrow or not

        Parameters:
            BookID
        Returns:
            Either the avilable bookID or a message stating that the book is not avilable to borrow
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select BookID from BookBorrowed Where BookID = %(BookID)s AND Status = %(Status)s", {'BookID':bookID,"Status":'borrowed'})
                if cursor.rowcount > 0:
                    return False
                else:
                    return True
        except:
            print("ip address not authorised by google cloud")


    def checkIfBookExistsInBookBorrowed(self, isbn, name):
        """
        Check if the book has been borrowed by a user

        Paramters: book ISBN, username

        Returns: book ID and True if the user has borrowed the book. None and False if the user did not borrow the book
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select BookBorrowed.BookID from Book, BookBorrowed Where Book.ISBN = %(isbn)s AND Book.BookID = BookBorrowed.BookID AND BookBorrowed.Status = 'borrowed' AND BookBorrowed.UserName = %(name)s",{"isbn":isbn,"name":name})
                if cursor.rowcount > 0:
                    return list(cursor.fetchall())[0][0], True
                else:
                    return None, False
        except:
            print("ip address not authorised by google cloud")

    # Delete User
    def deleteBookBorrowed(self, bookBorrowedID):
        """
        Delete all borrowed books with the bookBorrowedID
        Parameters:
            Id of the borrowed book(s)
        Returns:

        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("delete from BookBorrowed where BookBorrowedID != %s", (bookBorrowedID,))
            self.connection.commit()
        except:
            print("ip address not authorised by google cloud")

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
