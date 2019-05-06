from database_utils import DatabaseUtils
import logging

logging.basicConfig(filename="library.log", level = logging.ERROR)
class library_menu:

    def __init__(self):
        self.insertUser("user_name_1")
        # self.listUsers()

    @staticmethod
    def runMenu(self, user):
        print("Welcome " + user + "!")
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
        pass #Add search function here

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


library_menu()




