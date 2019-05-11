# pip3 install PrettyTable
from database_utils import DatabaseUtils
import logging
from prettytable import PrettyTable
import re 

logging.basicConfig(filename="library.log", level = logging.ERROR)
class library_menu:
 
    def runMenu(self, user):
        """
        This method provides users with the search/borrow/return book(s) options
        Parameters:
            User name
        Returns:
            logout message if the user requests
        """

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
        """
        There are three methods to search for a book:
        1- Search by book's title
        2- Search by book's author
        3. Search by ISBN
        By selecting any option LMS prompts user to enter title/author/ISBN and retrieves the result in a table
        Parameters:

        Returns:

        """

        while True:
            print()
            print("1. Search by title")
            print("2. Search by author")
            print("3. Search by ISBN")
            print("4. back")
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
                    isbn = input("Enter book's ISBN: ")
                    # while re.match(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}", publishedDate) == False: publishedDate = input("Enter book's published date (YYYY-MM-DD): ")
                    self.listBooksByISBN(isbn)
                elif(selection == "4"):
                    break
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


    # list books by title
    def listBooksByTitle(self, title):
        """
        Search books by book name
        Parameters:
            Book title
        Returns:
            All books with the title name
        """
        print("--- Books ---")
        table = PrettyTable(['Title', 'Author', 'ISBN'])
        with DatabaseUtils() as db:
            books =  db.getBookByTitle(title)
            if(books.count > 0):
                for book in books:
                    table.add_row([book[1], book[2], book[3]])
                print(table)
            else:
                print("Book not found! please try again.")

    # list books by author 
    def listBooksByAuthor(self, author):
        """
        Search books by their author.
        Parameters:
            Author of a book
        Returns:
            All books which have been written by the author
        """
        print("--- Books ---")
        table = PrettyTable(['Title', 'Author', 'ISBN'])
        with DatabaseUtils() as db:
            books = db.getBookByAuthor(author)
            if(books.count > 0):
                for book in books:
                    table.add_row([book[1], book[2], book[3]])
                print(table)
            else:
                print("Book not found! please try again.")

    # list books by ISBN
    def listBooksByISBN(self, isbn):
        """
        Search Books by ISBN. 
        Parameters:
            ISBN
        Returns:
            All books which have the ISBN
        """

        print("--- Books ---")
        table = PrettyTable(['Title', 'Author', 'ISBN'])
        with DatabaseUtils() as db:
            books = db.getBookBySIBN(isbn)
            if(books.count > 0):
                for book in books:
                    table.add_row([book[1], book[2], book[3]])
                print(table)
            else:
                print("Book not found! please try again.")


    ##############Out of scope!!!!#############
    ###USERS####
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

    ####BOOKS####
    def listBooks(self):
        print("--- Book ---")
        table = PrettyTable(['ID', 'ISBN','Title', 'Author'])
        with DatabaseUtils() as db:
            for book in db.getBooks():
                table.add_row([book[0],book[1], book[2], book[3]])
        print(table)


    def insertBook(self, title, author, isbn):
        with DatabaseUtils() as db:
            if(db.insertBook(title, author, isbn)):
                print("{} inserted successfully.".format(title))
            else:
                print("{} failed to be inserted.".format(title))
        self.listBooks()


# library_menu().insertBook("THE SUBTLE ART OF NOT GIVING A FUCK","MARK MANSON","9781925483598")
# library_menu().listBooks()




