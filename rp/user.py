from db import database
import re 
# pip3 install passlib
from passlib.hash import sha256_crypt

class user:

    @staticmethod
    # menu method to be displayed for users
    def menu():
        while True:
        # complete while loop
        # print welcome message and menu
            print('Welcome to smart library')
            print('1- Register a new account')
            print('2- Login into your account')
            try:
                # prompt user for input
                user_input = int(input())
                # if user types 1 --> call register method
                if user_input == 1:
                    user.register()
                # if user types 2 -- > call login method
                elif user_input == 2:
                    user.login()
                else:
                # if user types something else --> prompts them again
                    print('Please type either 1 or 2')
            except:
                print('Please type either 1 or 2')

    @staticmethod
    def register():

        username = input('Please type your username ')
        while not re.match("[a-zA-Z]", username): 
            username = input('Please type your username ')
        # check if the username already exists in the database
        # add some code if statement
        if database.checkusernameexist(username):
            password = input('Please type your password ')
            re_password = input('Please re-type your password again ')
            attempt = 0
            while password != re_password and attempt < 2:
                password = input('Please type your password ')
                re_password = input('Please re-type your password again ')
                attempt += 1
            if attempt >= 2: exit
            hashedPassword = sha256_crypt.hash(password)
            first_name = input('Please type your first name ')
            while re.match("[a-zA-Z]", first_name) == False: first_name = input('Please type your first name ')
            last_name = input('Please type your last name ')
            while re.match("[a-zA-Z]", last_name) == False: last_name = input('Please type your last name ')
            email = input('Please type your email address ')
            while re.match("\S+@\S+", first_name) == False: email = input('Please type your email address ')
            
            # insert the data into the databse table
            database.insertData(username, hashedPassword, first_name, last_name, email)
            

    @staticmethod
    def login():
        username = input('Please type your username ')
        password = input('Please type your password ')
        attempt = 0
        while database.veriftData(username, password) == False and attempt < 4:
            print('Either username or password is wrong, please re-enter')
            username = input('Please type your username ')
            password = input('Please type your password ')
            attempt += 1
        if attempt >= 4: exit
        if database.veriftData(username,password)== True:
            # send login message to Master Pi
            pass