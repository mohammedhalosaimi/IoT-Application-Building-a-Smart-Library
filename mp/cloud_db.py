"""
Create a file called dbInfo.json.
Follow week 7 tutorials to get your gCloud DB set up.
Copy the following JSON object into it and adjust it to suit your DB.
{
    "address": "0.0.0.0",
    "username": "root",
    "password":"your_password"
}

Don't forget to add your raspberry pi's IP to allowed connections in gCloud.
"""
import json
import os
import MySQLdb

class cloud_db:
    
    #Largely based off week 7 code supplied.
    DATABASE = "Library"

    def __init__(self, connection = None):
        dbInfo = cloud_db.load_json()
        if(connection == None):
            connection = MySQLdb.connect(dbInfo["address"], dbInfo["username"],
                dbInfo["password"], cloud_db.DATABASE)
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createLmsUserTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists LmsUser (
                    LmsUserID int not null auto_increment,
                    UserName nvarchar(256) not null,
                    Name text not null,
                    constraint PK_LmsUser primary key (LmsUserID),
                    constraint UN_UserName unique (UserName)
                )""")
        self.connection.commit()

    def createBookTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists Book (
                    BookID int not null auto_increment,
                    Title text not null,
                    Author text not null,
                    PublishedDate date not null,
                    constraint PK_Book primary key (BookID)
                )""")
        self.connection.commit()
    
    def createBorrowTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists BookBorrowed (
                    BookBorrowedID int not null auto_increment,
                    LmsUserID int not null,BookID int not null,
                    Status enum ('borrowed', 'returned'),
                    BorrowedDate date not null,
                    ReturnedDate date null,
                    constraint PK_BookBorrowed primary key (BookBorrowedID),
                    constraint FK_BookBorrowed_LmsUser foreign key (LmsUserID) references LmsUser (LmsUserID),
                    constraint FK_BookBorrowed_Book foreign key (BookID) references Book (BookID)
                )""")
        self.connection.commit()

    def insertUser(self, username, name):
        return False
    
    def getUsers(self):
        return False
    
    def deleteUser(self, userID):
        return False
    
    def insertBook(self, title, author, pDate):
        with self.connection.cursor() as cursor:
            cursor.execute("""insert into Person ( 
                VALUES(%(title)s, %(author)s, %(pdate)s)""",
                {'title': title, 'author': author, 'pdate' : pDate})
        self.connection.commit()
        #If a row was added, return true.
        return cursor.rowcount == 1
    
    def getBooks(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select BookID, Name from Book")
            return cursor.fetchall()

    def deleteBook(self, bookID):
        return False
    """
    #Week 7 code
    def insertPerson(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Person (Name) values (%s)", (name,))
        self.connection.commit()
        return cursor.rowcount == 1

    def getPeople(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select PersonID, Name from Person")
            return cursor.fetchall()
        
    def deletePerson(self, personID):
        with self.connection.cursor() as cursor:
                cursor.execute("delete from Person where PersonID = %s", (personID,))
        self.connection.commit()
    """

    @staticmethod
    def load_json():
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'dbInfo.json')
        with open(filename, 'r') as j:
            return json.load(j)