"""
References:
https://stackoverflow.com/questions/9202224/getting-command-line-password-input-in-python

"""

# import packages
from db import database
import re 
from passlib.hash import sha256_crypt
import getpass
from rp_socket import rp_socket
from capture import capture
from encode import encode
from recognise import recognise
import time

# start of class user
class user:

    # menu method to be displayed for users
    @staticmethod
    def menu():
        """
        menu method does display the menu for the user
        """
        # keep looping
        while True:
            # print the menu and welcome message
            print('Welcome to smart library\n1- Register a new account \n2- Login into your account')
            # try clause
            try:
                # prompt user for input options either 1 or 2
                user_input = int(input())
                # if user types 1 --> call registration method
                if user_input == 1:
                    # call registration method
                    user.registration()
                # if user types 2 -- > call login method
                elif user_input == 2:
                    # call login method
                    user.login()
                else:
                # if user types something else --> prompts them again
                    print('Please type either 1 or 2')
            except:
                # if user types something else --> prompts them again
                print('Please type either 1 or 2')

    # registration method
    @staticmethod
    def registration():
        """
        registration method does the register a new user into the library system
        """
        # print a message to the user
        print('Welcome to registration page.\n- Please note that username must contain letters only.\n- Note that your two passwords must match.')

        # prompt user for username
        username = input('Please type your username ')
        # using regular expression, check if the username contains letters only
        while not bool(re.match("[a-zA-Z]", username)): 
            # if username doesn't match the specification, then prompt the user again for thier username
            username = input('Please type your username ')
        # check if the username already exists in the database. if username does not exist, then exceed
        # with registration process
        if(database.checkusernameexists(username)):
            # prompt user for password
            password = getpass.getpass('Please type your password ')
            # prompt user for password again
            re_password = getpass.getpass('Please re-type your password again ')
            # attempt variable to count the number of attempts the user tries to match their passwords
            attempt = 0
            # if the two passwords does not match and attempt times is less than two time then
            # prompt user again 
            while password != re_password and attempt < 2:
                # prompt user for password
                password = getpass.getpass('Please type your password ')
                # prompt user for password again
                re_password = getpass.getpass('Please re-type your password again ')
                # increment attempt times
                attempt += 1
            # if attempt is equal of greater than 2, then exist the registration page
            if attempt >= 2: 
                print('You exceeded more than two attempts. Try and register again')
                exit
            # exceed with registration process
            # hash the password and assign it to a variable named hashedPassword
            hashedPassword = sha256_crypt.hash(password)
            # prompt user for first name
            first_name = input('Please type your first name ')
            # check if first name contains letters only, if not then prompt user for first name again
            while bool(re.match("[a-zA-Z]", first_name)) == False: first_name = input('Please type your first name ')
            # prompt user for last name
            last_name = input('Please type your last name ')
            # check if last name contains letters only, if not then prompt user for last name again
            while bool(re.match("[a-zA-Z]", last_name)) == False: last_name = input('Please type your last name ')
            # prompt user for email address
            email = input('Please type your email address ')
            # check if email address does contain the proper format of an email, if not then prompt user for last name again
            while bool(re.match("\S+@\S+", email)) == False: email = input('Please type your email address ')
            
            # insert the data into the databse calling database class
            database.insertData(username, hashedPassword, first_name, last_name, email)

            # prompt user to choose bwtween console-based/acial recognition authentication
            option = int(input('Please choose one of the following options for your login process:\n- 1 for console-based authentication\n- 2 for facial recognition authentication\n'))
        
            # if user choses 1, the exit since the user doesn't want to do facial recognition authentication
            if option == 1:
                exit

            # if user choses facial recognition authentication, then call facial recognition files
            elif option == 2:
                print('Please be ready as we will take some picture of your face')
                time.sleep(5)
                print('Taking pictures now')
                # capture user face
                capture.main(username)
                print('Our system is encoding your pictures for learning purposes.')
                # encode user face pictures
                encode.main()
                                    
        # else means that the username already exists in the database
        else:
            # print a message
            print("Username already exists!")
            exit
    

    # login method
    @staticmethod
    def login():
        """
        Login method, able the user to login in to the library system
        """

        # prompt user to choose bwtween console-based/acial recognition authentication for login option
        option = int(input('Please choose one of the following options to login:\n- 1 for console-based authentication\n- 2 for facial recognition authentication\n'))
        
        # if user choses 1, it means the user want to login with console-based authentication
        if option == 1:
            # prompt user for username
            username = input('Please type your username ')
            # prompt user for password
            password = getpass.getpass('Please type your password ')
            # hash the password
            if database.checkusernameexists(username) == True:
                print('Either username or password is wrong, please re-enter')
            # attempt variable to count the number of attempts the user tries to login
            attempt = 0
            # check if username and password aren't associated with each other and attempt is less than 4 times
            checkPass = database.veriftPassword(username, password)
            while checkPass == False and attempt < 4:
                # print a meaningful message
                print('Either username or password is wrong, please re-enter')
                # prompt user for username
                username = input('Please type your username ')
                # prompt user for password
                password = getpass.getpass('Please type your password ')
                # hash the password
                # hashedPassword = sha256_crypt.hash(password)
                # increment attempt times
                attempt += 1
                checkPass = database.veriftPassword(username, password)
            # if attempts is greater or equal tna 4, then print a message and exit
            if attempt >= 4:
                print('You exceeded more than 4 attempts to login. Try and login again')
                exit
                
            # check if username and password are matching for one user
            if checkPass == True:
                # send login message to Master Pi
                print(username, ' welcome to the Smart Library')
                # create an object from rp_socket
                rp_socket_object = rp_socket()
                rp_socket_object.connection(username)

            
                
        # if user choses 2, it means the user wants to login with facial recognition authentication
        elif option == 2:    
            # call the recognise file which returns two values, True if face has been recognized, and the user name
            boolean, name = recognise.main()
            # if the face has been recognized, welcome the user to the smaer library
            if boolean == True and name != 'Unknown':
                # send login message to Master Pi
                print(name, ' welcome to the Smart Library')
                # create an object from rp_socket
                rp_socket_object = rp_socket()
                rp_socket_object.connection(name)
            else:
                print('The System Could Not Recognize your Face')
        # if login is not successful, then print a message saying login could not be done
        else:
            print('Please type either 1 or 2')
            

# call the user menu
user.menu()
