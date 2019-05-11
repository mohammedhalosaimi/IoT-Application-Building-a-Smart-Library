# pip3 install PrettyTable
from database_utils import DatabaseUtils
import logging
from prettytable import PrettyTable
import re 

logging.basicConfig(filename="library.log", level = logging.ERROR)
class library_menu:

    # def __init__(self):
        # self.insertUser("user_name_1")
        # self.listUsers()

  
    def runMenu(self, user):
        print("Welcome " + user + "!")
        while True:
            print()
            print("1. Search a book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Logout")
            selection = input("Select an option: ")
            print()

            try:
                if(selection == "1"):
                    self.searchBook()
                elif(selection == "2"):
                    self.borrowBook()
                elif(selection == "3"):
                    self.returnBook()
                elif(selection == "4"):
                    print("Goodbye!")
                    return "logout"
                else:
                    print("Invalid input - please try again.")
            except  Exception as e:
                logging.error("Library menu error: {}".format(str(e)))
        return "login"


    # Search a book
    def searchBook(self):
        while True:
            print()
            print("1. Search by title")
            print("2. Search by author")
            print("3. Search by published date")
            selection = input("Select an option: ")
            print()

            try:
                if(selection == "1"):
                    title = input("Enter book's title: ")
                    self.listBooksByTitle(title)
                elif(selection == "2"):
                    author = input("Enter book's author: ")
                    self.listBooksByAuthor(author)
                elif(selection == "3"):
                    publishedDate = input("Enter book's published date (YYYY-MM-DD): ")
                    while re.match(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}", publishedDate) == False: publishedDate = input("Enter book's published date (YYYY-MM-DD): ")
                    self.listBooksByPublishedDate(publishedDate)
                else:
                    print("Invalid input - please try again.")
            except  Exception as e:
                logging.error("Search menu error: {}".format(str(e)))

        # Borrow a book
    def borrowBook(self):
        pass  #Add borrow function here

        # Return a book
    def returnBook(self):
        pass #Add return function here


    def listUsers(self):
        print("--- User ---")
        print("{:<15} {}".format("User ID", "Name"))
        with DatabaseUtils() as db:
            for user in db.getUsers():
                print("{:<15} {}".format(user[0], user[1]))

    def insertUser(self, name):
        with DatabaseUtils() as db:
            if(db.insertUser(name)):
                print("{} inserted successfully.".format(name))
            else:
                print("{} failed to be inserted.".format(name))

    # list books by title
    def listBooksByTitle(self, title):
        print("--- Books ---")
        table = PrettyTable(['Title', 'Author', 'Published Date'])
        with DatabaseUtils() as db:
            for book in db.getBookByTitle(title):
                table.add_row([book[1], book[2], book[3]])
        print(table)

    # list books by author 
    def listBooksByAuthor(self, author):
        print("--- Books ---")
        table = PrettyTable(['Title', 'Author', 'Published Date'])
        with DatabaseUtils() as db:
            for book in db.getBookByAuthor(author):
                table.add_row([book[1], book[2], book[3]])
        print(table)

    # list books by published date
    def listBooksByPublishedDate(self, publisheddate):
        print("--- Books ---")
        table = PrettyTable(['Title', 'Author', 'Published Date'])
        with DatabaseUtils() as db:
            for book in db.getBookByPublishedDate(publisheddate):
                table.add_row([book[1], book[2], book[3]])
        print(table)


library_menu()