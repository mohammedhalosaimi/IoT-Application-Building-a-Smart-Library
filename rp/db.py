# pip3 install passlib

from passlib.hash import sha256_crypt
from datetime import date
import sqlite3
import time

dbname="Recepition_Pi.db"

class database:

    @staticmethod
    def connection(): 
        # connect to the database
        conn = sqlite3.connect(dbname)
        # return connection
        return conn
    @staticmethod
    def create_tables():
        conn=database.connection()
        with conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS ACCOUNT")
            cur.execute("CREATE TABLE ACCOUNT(username TEXT NOT NULL PRIMARY KEY,password TEXT)")
            cur.execute("DROP TABLE IF EXISTS USER")
            cur.execute("CREATE TABLE USER(firstname TEXT,lastname TEXT,email TEXT,username TEXT,FOREIGN KEY (username) REFERENCES ACCOUNT(username))")
            
    @staticmethod
    def insertData(username,password,firstname,lastname,email):
        conn=database.connection()
        with conn:
            cur=conn.cursor()
            try:
                cur.execute("INSERT INTO ACCOUNT values(?,?)",(username,password))
                cur.execute("INSERT INTO USER values(?,?,?)",(firstname,lastname,email,username))
            except:
                print("Username already exist!")

    @staticmethod
    def veriftData(username,password):
        conn=database.connection()
        with conn:
            cur=conn.cursor()
            result=list(cur.execute("SELECT * FROM ACCOUNT WHERE USERNAME = ?",(username)))
            if password != result[-1][-1] :
                return True
        return False

    @staticmethod
    def checkusernameexist(username):
        conn=database.connection()
        with conn:
            cur=conn.cursor()
            result=list(cur.execute("SELECTE * FROM ACCOUNT WHERE USERNAME = ?",(username)))
            print('aaaassdfsadgadfgdsfhsdhs')
            print(result)
            if not result:
                return True
            else:
                return False
