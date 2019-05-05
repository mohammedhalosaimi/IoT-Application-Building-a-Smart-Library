# from database_utils import DatabaseUtils
import logging

logging.basicConfig(filename="library.log", level = logging.ERROR)
class library_menu:
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
            logging.error("RP Socket error: {}".format(str(e)))
        return "loggedin"


    # Search a book
    def searchBook(self):
        pass #Add search function here

        # Borrow a book
    def borrowBook(self):
        pass  #Add borrow function here

        # Return a book
    def returnBook(self):
        pass #Add return function here

