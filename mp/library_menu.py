# from database_utils import DatabaseUtils
import logging

logging.basicConfig(filename="library.log", level = logging.ERROR)
class library_menu:
    # def main(self):
    #     # with DatabaseUtils() as db:
    #     #     db.createPersonTable()
    #     self.runMenu()
    @staticmethod
    def runMenu(self):
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
                return "loggedout"
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

    # def listPeople(self):
    #     print("--- People ---")
    #     print("{:<15} {}".format("Person ID", "Name"))
    #     with DatabaseUtils() as db:
    #         for person in db.getPeople():
    #             print("{:<15} {}".format(person[0], person[1]))

    # def insertPerson(self):
    #     print("--- Insert Person ---")
    #     name = input("Enter the person's name: ")
    #     with DatabaseUtils() as db:
    #         if(db.insertPerson(name)):
    #             print("{} inserted successfully.".format(name))
    #         else:
    #             print("{} failed to be inserted.".format(name))

# if __name__ == "__main__":
#     menu().main()
