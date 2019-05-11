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
                connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
                print("Connecting to: {} with details: {}".format(DATABASE,connection))
                self.createTables()
                
            except Exception as e:
                print("DatabaseUtils error: {}".format(str(e)))
            
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createTables(self):
        """
        This method connects runs the SQL in "Assignment2_CreateTables.sql"
        """
        with self.connection.cursor() as cursor:
            cursor.execute(open("Assignment2_CreateTables.sql", "r").read())
        self.connection.commit()

    # User CRUD table
    # ****************************************
    # Insert user
    def insertUser(self, name):
        """
        This method inserts a user into the cloud database

        Parameters:

            Name: The username of a user.
        
        Returns:

            True: The user was succesfully added
            False: The user was not added (Possibly already exists)        
        """
        with self.connection.cursor() as cursor:
            cursor.execute("insert into LmsUser (UserName) values (%s)", (name,))
        self.connection.commit()

        return cursor.rowcount == 1

    # Get user
    def getUser(self, name):
        """
        This method returns a user (Id, username) given a username

        Parameters:

            Name: The username of a user.
        
        Returns:
            List of lists: The results of the query.       
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from LmsUser Where UserName = %s", (name,))
            #Could change to cursor.fetchone() as Username are unique
            return cursor.fetchall()

    # Get user
    def getUsers(self):
        """
        This method returns all users in the cloud database
        
        Returns:
            List of lists: The results of the query.       
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from LmsUser")
            return cursor.fetchall()

    # Delete User
    def deleteUser(self, lmsUserID):
        """
        This method returns deletes a user on the cloud given an id       
        """
        with self.connection.cursor() as cursor:
            cursor.execute("delete from LmsUser where LmsUserID = %s", (lmsUserID,))
        self.connection.commit()


    # Book CRUD table
    # ****************************************
    # Insert Book
    def insertBook(self, title, author, publishedDate):
        """
        This method inserts a book into the cloud database

        Parameters:

            Title: The title of the book.
            Author: The author of the book
            Published Date: The date of publish. YYYY-MM-DD
        
        Returns:
            
            True: The book was added.
            False: The book was not added.      
        """
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Book (Title, Author, PublishedDate) values (%s, %s, %s)", (title,author, publishedDate))
        self.connection.commit()

        return cursor.rowcount == 1

    # Get Book by title
    def getBookByTitle(self, title):
        """
        This method retrieves all books with a similiar title
        to the supplied title

        Parameters:

            Title: The search term used.
        
        Returns:
        List of lists: Representing the result     
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where Title Like %s", ("%" + title + "%",))
            return cursor.fetchall()

    # Get Book by Author
    def getBookByAuthor(self, author):
        """
        This method retrieves all books with a similiar author

        Parameters:

            author: The search term used.
        
        Returns:
        List of lists: Representing the result     
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where Author Like %s", ("%" + author + "%",))
            return cursor.fetchall()

    # Get Book by PublishedDate
    def getBookByPublishedDate(self, publishedDate):
        """
        This method retrieves all books published between a given date

        Parameters:

            Published Date: The search term used.
        
        Returns:
        List of lists: Representing the result     
        """
        #Possible change to get book by date range.
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book Where PublishedDate Like %s", ("%" + publishedDate + "%",))
            return cursor.fetchall()

    # Delete Book
    def deleteBook(self, bookID):
        """
        This method deletes a book given a Book ID

        Parameters:

            BookID: The ID of the book being deleted.    
        """
        with self.connection.cursor() as cursor:
            cursor.execute("delete from Book where BookID = %s", (bookID,))
        self.connection.commit()


    # BookBorrowed CRUD table
    # ****************************************
    # Insert BookBorrowed record
    def insertBookBorrowed(self, lmsUserID, bookID, status = 'borrowed', borrowdDate, returnDate):
        """
        This method inserts a bookBorrowed into the cloud database

        Parameters:

            Lms User ID: ID representing the user borrowing the book
            Book ID: ID representing the book being borrowed.
            Status: The status of the book. Defaults to borrowed.
            Borrowed Date: The date the book was borrowed.
            Return Date: The expected return date of the book.
        Returns:
            
            True: The book was borrowed.
            False: The book was not borrowed.   
        """
        with self.connection.cursor() as cursor:
            cursor.execute("insert into BookBorrowed (LmsUserID, BookID, Status, BorrowedDate, ReturnedDate) values (%s)", (lmsUserID,bookID, status, borrowdDate, returnDate))
        self.connection.commit()

        return cursor.rowcount == 1

    # Get user
    def getBookBorrowed(self, lmsUserID, bookID):
        """
        This method returns all borrows given a User and a Book

        Parameters:

            Lms User ID: ID representing the user borrowing the book
            Book ID: ID representing the book being borrowed.
        Returns:
            List of lists: The result of the query.  
        """
        with self.connection.cursor() as cursor:
            cursor.execute("select * from BookBorrowed Where LmsUserID = "+ lmsUserID +" AND BookID = "+ bookID)
            return cursor.fetchall()

    # Delete User
    def deleteBookBorrowed(self, bookBorrowedID):
        """
        This method deletes a borrowed book from the cloud.

        Parameters:
            
            Book Borrowed ID: The ID of the Book Borrowed.    
        """
        with self.connection.cursor() as cursor:
            cursor.execute("delete from BookBorrowed where BookBorrowedID != %s", (bookBorrowedID,))
        self.connection.commit()




    # Read config.json
    def readConfig(self):
        """
        This method reads the config.json
        This is used for connecting to the cloud db.

        Parameters:

            Lms User ID: ID representing the user borrowing the book
            Book ID: ID representing the book being borrowed.
        Returns:
            List of lists: The result of the query.  
        """
        with open('config.json') as jsonFile:  
            data = json.load(jsonFile)
        return data
