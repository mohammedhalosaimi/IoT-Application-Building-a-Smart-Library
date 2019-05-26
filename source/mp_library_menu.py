# # pip3 install PrettyTable
# from database_utils import DatabaseUtils
# import logging
# from prettytable import PrettyTable
# import re 
# from bookevent import bookevent
# from voice_recognition import voice_recognition
# import datetime
# from barcodescanner import barcodescanner


# logging.basicConfig(filename="library.log", level = logging.ERROR)
class library_menu:
 
    def runMenu(self, user):
        """
        This method provides users with the search/borrow/return book(s) options

        Parameters:

            User name

        Returns:

            logout message if the user requests
        """

        # print("\nWelcome " + user + "!")
        # while True:
        #     print()
        #     print("1. Search a book")
        #     print("2. Borrow a book")
        #     print("3. Return a book")
        #     print("4. Logout")
        #     selection = input("Select an option: ")
        #     print()

        #     try:
        #         if(selection == "1"):
        #             self.searchBook(user)
        #         elif(selection == "2"):
        #             self.borrowBook(user)
        #         elif(selection == "3"):
        #             self.returnBook(user)
        #         elif(selection == "4"):
        #             print("Goodbye!")
        #             return "logout"
        #         else:
        #             print("Invalid input - please try again.")
        #     except  Exception as e:
        #         logging.error("Library menu error: {}".format(str(e)))
        # return "login"


    # Search a book
    def searchBook(self, user):
        """
        There are three methods to search for a book:

        1- Search by book's title
        2- Search by book's author
        3. Search by ISBN

        By selecting any option LMS prompts user to enter title/author/ISBN and retrieves the result in a table
        
        Parameters:

        Returns:

        """

        # while True:
        #     print()
        #     print("1. Search by title")
        #     print("2. Search by author")
        #     print("3. Search by ISBN")
        #     print("4. back")
        #     selection = input("Select an option: ")
        #     print()

        #     try:
        #         if(selection == "1"):
        #             title = self.SearchByVoiceOrText("title")
        #             title_result=self.listBooksByTitle(title)
        #         elif(selection == "2"):
        #             author = self.SearchByVoiceOrText("author")
        #             author_result=self.listBooksByAuthor(author)
        #         elif(selection == "3"):
        #             isbn = self.SearchByVoiceOrText("ISBN")
        #             isbn_result=self.listBooksByISBN(isbn)
        #         elif(selection == "4"):
        #             break
        #         else:
        #             print("Invalid input - please try again.")
        #         if title_result==True or isbn_result==True or author_result==True:
        #             self.borrowBook(user)
        #     except  Exception as e:
        #         logging.error("Search menu error: {}".format(str(e)))

    def SearchByVoiceOrText(self, subject):
        """
        We can search a book by typing on the command line or talking to google voice recognition.

        Parameters:

        Returns:

        """
        # while True:
        #     print()
        #     print("1. Search through command line")
        #     print("2. Search through voice")
        #     print("3. back")
        #     selection = input("Select an option: ")
        #     print()

        #     try:
        #         if(selection == "1"):
        #             return input("Enter book's "+subject+": ")
        #         elif(selection == "2"):
        #             return voice_recognition.getTextFromVoice()
        #         elif(selection == "3"):
        #             break
        #         else:
        #             print("Invalid input - please try again.")
        #     except  Exception as e:
        #         logging.error("Search menu error: {}".format(str(e)))

        # Borrow a book
    def borrowBook(self, user):

        """
        this method allows the user to borrow a book from the library if it is avilabel.

        It also add event to Google calendar with user and book details
        
        Parameters: username
        """

        # print('Please Note that you only can borrow a book by its ISBN. If you do not know the ISBN, please go back to the menu and search the book first')
        # # prompt the user for book's ISBN
        # book_isbn = input('Please type the ISBN here or hit q to go back to menu: \n')
        # # exit if user hits q
        # if book_isbn == 'q': exit
        # # call DatabaseUtils class and create an object of it
        # db_object = DatabaseUtils()
        # # call library menu class and create an object of it
        # lm_object = library_menu()
        # # get today's date
        # now = datetime.datetime.now()
        # today_date = now.strftime("%Y-%m-%d")
        # # remove spaces
        # book_isbn = book_isbn.strip()
        # # check if the user typed the ISBN
        # regex= r'978[\d\-]+\d'
        # pattern = re.match(regex, book_isbn)
        # if bool(pattern)==True:
        #     # call the getBookByISBN function to check if the book exists at the library
        #     book_list = db_object.getBookByISBN(book_isbn)
        #     # convert to list
        #     book_list = list(book_list)
        #     # if the book doesn't exist, the apologize for the user
        #     if not book_list:
        #         print('We are sorry, we do not have the book at the moment')
        #     # if the book exists
        #     else:
        #         # boolean variable to check that the user only borrows one copy of a book at a time
        #         #bool_borroed = False
        #         # loop through all the copies of the same book and check which one is avilable to borrow
        #         for i in book_list:
        #             # check if the book is avilable to borrow
        #             return_value = db_object.getAvilableBook(i[0])
        #             #if return_value == True and bool_borroed == False:
        #             if return_value == True:
        #                 # get book details from the library
        #                 book_details = db_object.getBookByID(i[0])
        #                 book_details = list(book_details)
        #                 # add leading zeros to the book id to be able to add an event
        #                 # since the id in google calendar must be at least 5 digits
        #                 id_event = '00000' + str(book_details[0][0])
        #                 # add an event to the calendar with the book details
        #                 bookevent.insert(user, id_event, book_details[0][2], book_details[0][3])
        #                 # check if the user exists in LmsUser table
        #                 check_user_in_LmsUser = db_object.getUser(user)
        #                 if check_user_in_LmsUser == False:
        #                     # add the user the LmsUser table to keep track of users who borrowed book
        #                     lm_object.insertUser(user)
        #                 # insert book and user details to BookBorrowed table
        #                 db_object.insertBookBorrowed(user, book_details[0][0], 'borrowed', today_date)
        #                 # print success message
        #                 print("You have successfully borrowed: " + book_details[0][2])
        #                 #bool_borroed = True
        #                 return True
        #            # elif return_value == False and i == len(book_list)-1:
        #         # if the book is not avilable, the print a message to the user
        #         print('Sorry but the book is not avilable')
        #         return False
        # else:
        #     print("Your Input does not match book's ISBN")
        # Return a book
    def returnBook(self, user):        
        """
        allow the user to return a book

        Paramters: user
        """

        # # prompt the user to choose between entering the ISBN manually or scanning the QR code
        # option=int(input('Please choose\n 1.Manually Enter the detail\n 2.Return the book using QR code \n'))
        # if option==1 :
        #     # prompt the user for the book ISBN
        #     user_input = input('Please type your book ISBN to continue with return process\n')
        # # if user choses to scan a QR code
        # elif option==2:
        #     # call the barcodescanner file
        #     user_input = barcodescanner.scanQR()
        #     # strip the ISBN if it has spaces
        #     user_input = user_input.strip()
        #     # if the ISBN code does not match the format then exit
        #     if user_input == "quitbyuser":
        #         exit

        # # call DatabaseUtils class and create an object of it
        # db_object = DatabaseUtils()

        # # get today's date
        # now = datetime.datetime.now()
        # today_date = now.strftime("%Y-%m-%d")
        # # check if the user typed the ISBN
        # regex= r'978[\d\-]+\d'
        # pattern = re.match(regex, user_input)

        # if bool(pattern)==True:
        #     # check if the book has been borrowed at the first place
        #     return_value, t_value = db_object.checkIfBookExistsInBookBorrowed(user_input, user)
        #     if isinstance(return_value, int) and t_value == True:
        #         id_event = '00000' + str(return_value)
        #         # remove the event from Google Calendar
        #         bookevent.removeEvent(id_event)
        #         #  update the status of the book in BookBorrowed table
        #         db_object.updateBookBorrowed(user, return_value, 'returned', today_date)
        #         # print a message to the user
        #         print('We hope that you enjoyed your journey reading the book')
        #     # if the book doesn't exist in the BookBorrowed table, then it means the book has not been borrowed
        #     else:
        #         print('We apologize, the ISBN you entered has not been borrowed by you!')
        #     # if the user typed something else rather than book ISBN
        # else:
        #     print('Your Input does not match books ISBN')

    # list books by title
    def listBooksByTitle(self, title):
        """
        Search books by book name

        Parameters:

            Book title

        Returns:

            All books with the title name
        """
        # print("--- Books ---")
        # table = PrettyTable(['ISBN','Title', 'Author'])
        # with DatabaseUtils() as db:
        #     books =  db.getBookByTitle(title)
        #     if(len(books) > 0):
        #         for book in books:
        #             table.add_row([book[1], book[2], book[3]])
        #         print(table)
        #         return True
        #     else:
        #         print("Book not found! please try again.")
        #         return False

    # list books by author 
    def listBooksByAuthor(self, author):
        """
        Search books by their author.

        Parameters:

            Author of a book

        Returns:

            All books which have been written by the author
        """
        # print("--- Books ---")
        # table = PrettyTable(['ISBN','Title', 'Author'])
        # with DatabaseUtils() as db:
        #     books = db.getBookByAuthor(author)
        #     if(len(books) > 0):
        #         for book in books:
        #             table.add_row([book[1], book[2], book[3]])
        #         print(table)
        #         return True
        #     else:
        #         print("Book not found! please try again.")
        #         return False

    # list books by ISBN
    def listBooksByISBN(self, isbn):
        """
        Search Books by ISBN. 

        Parameters:

            ISBN

        Returns:
        
            All books which have the ISBN
        """

        # print("--- Books ---")
        # table = PrettyTable(['ISBN','Title', 'Author'])
        # with DatabaseUtils() as db:
        #     books = db.getBookByISBN(isbn)
        #     if(len(books) > 0):
        #         for book in books:
        #             table.add_row([book[1], book[2], book[3]])
        #         print(table)
        #         return True
        #     else:
        #         print("Book not found! please try again.")
        #         return False


#     ##############Out of scope!!!!#############
#     ###USERS####
#     def listUsers(self):
#         print("--- User ---")
#         print("{:<15} {}".format("User ID", "Name"))
#         with DatabaseUtils() as db:
#             for user in db.getUsers():
#                 print("{:<15} {}".format(user[0], user[1]))

#     def insertUser(self, name):
#         with DatabaseUtils() as db:
#             if(db.insertUser(name)):
#                 # print("{} inserted successfully.".format(name))
#                 pass
#             else:
#                 print("{} failed to be inserted.".format(name))

#     ####BOOKS####
#     def listBooks(self):
#         print("--- Book ---")
#         table = PrettyTable(['ID', 'ISBN','Title', 'Author'])
#         with DatabaseUtils() as db:
#             for book in db.getBooks():
#                 table.add_row([book[0],book[1], book[2], book[3]])
#         print(table)


#     def insertBook(self, title, author, isbn):
#         with DatabaseUtils() as db:
#             if(db.insertBook(title, author, isbn)):
#                 print("{} inserted successfully.".format(title))
#             else:
#                 print("{} failed to be inserted.".format(title))
#         self.listBooks()

# # library_menu().insertBook("What the fuck","MARK MANSON","978-1-34-123123-1")
# # library_menu().listBooks()

# #a = library_menu()
# #a.runMenu('Mohammed')


