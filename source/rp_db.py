# # import packages
# from passlib.hash import sha256_crypt
# from datetime import date
# import sqlite3
# import time

# # database name
# dbname="Recepition_Pi.db"

# start of a class
class database:

    # connection method
    @staticmethod
    def connection(): 
        """
        This method connects to the local database and returns the connection

        Returns:
        connection object
        """
        # # connect to the database
        # conn = sqlite3.connect(dbname)
        # database.create_tables(conn)
        # # return connection
        # return conn

    # create tables method
    @staticmethod
    def create_tables(conn):
        """
        This method creates two tables. user and account table
        """
        # # call the connection method which returns the connection object
        # # conn = database.connection()
        # with conn:
        #     # move the cursor to the top
        #     cur = conn.cursor()
        #     # drop table account if exists
        #     # cur.execute("DROP TABLE IF EXISTS account")
        #     # create a table named account with the variables: username, and password
        #     cur.execute("CREATE TABLE  IF NOT EXISTS account(username TEXT NOT NULL PRIMARY KEY,password TEXT)")
        #     # drop table user if exists
        #     # cur.execute("DROP TABLE IF EXISTS user")
        #     # create a table named user with the variables: firstname, lastname, username, and email
        #     cur.execute("CREATE TABLE IF NOT EXISTS user(firstname TEXT,lastname TEXT,username TEXT, email TEXT,FOREIGN KEY (username) REFERENCES ACCOUNT(username))")

    # insert data method  
    @staticmethod
    def insertData(username,password,firstname,lastname,email):

        """
        This method inserts data to two tables. account table and user table

        Parameters:
        
        username: the username of the user
        password: password of the user after it's been hashed
        firstname: user's first name
        lastname: user's last name
        email: user's email address

        """

        # # call the connection method which returns the connection object
        # conn=database.connection()
        # with conn:
        #     # move the cursor to the top
        #     cur = conn.cursor()
        #     # try clause
        #     try:
        #         # insert username and password into account table     
        #         cur.execute("INSERT INTO account values(?,?)",(username,password))
        #         # insert firstname, lastname, username, email into user table
        #         cur.execute("INSERT INTO user values(?,?,?,?)",(firstname,lastname,username,email))
        #     # except clause
        #     except:
        #         # since username is primary key, we can't add more than once.
        #         # So print the message below if trying to insert duplicate username
        #         print("Username already exists!")

    # veriftPassword method
    @staticmethod
    def veriftPassword(username,password):
        """
        This method verifies if the password that is associated with the username is right

        Parameters:
        
        username: user's username
        password: hashed value for the user's password

        Returns:
        
        True: check if the passed password equals the password that is associated with the username in account table
        False: if the passed password does not equal the password that is associated with the username in account table

        """

        # # call the connection method which returns the connection object
        # conn=database.connection()
        # with conn:
        #     # move the cursor to the top
        #     cur = conn.cursor()
        #     # assign the output of the sql code to a result variable after converting the sql object into a python list
        #     result = list(cur.execute("SELECT password FROM account WHERE USERNAME = ?",(username,)))
        #     # check if the passed password equals the password that is associated with the username in account table
        #     if(sha256_crypt.verify(password, result[0][0])):
        #         return True
        #     else:
        #         return False
                

        #     # if password == result[0][0]:
        #     #     print('True')
        #     #     return True
        #     # # else return False
        #     # else: 
        #     #     print('False')
        #     #     return False

    # check username exists method
    @staticmethod
    def checkusernameexists(username):
        """
        This method checks if the username is already in the account table

        Parameters:
        
        username: user's username

        Returns:
        
        True: true if username does not exist
        False: false if username exists

        """
        # # call the connection method which returns the connection object
        # try:
        #     conn=database.connection()
        #     with conn:
        #         # move the cursor to the top 
        #         cur=conn.cursor()
        #         # assign the output of the sql code to a result variable after converting the sql object into a python list
        #         result = list(cur.execute("SELECT * FROM account WHERE USERNAME = ?",(username,)))
        #         # if result is empty which means username does not exist, then return true
        #         if not result:
        #             return True
        #         # if result is empty which means username does exists in the account table, then return false
        #         else:
        #             return False
        # except  Exception as e:
        #     print("Error: " + str(e))