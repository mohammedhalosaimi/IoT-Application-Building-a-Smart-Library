from datetime import date
import sqlite3
import time

dbname="Recepition_Pi"

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
            cur.execute("DROP TABLE IF EXITSTS ACCOUNT")
            cur.execute("CREATE TABLE ACCOUNT(username TEXT NOT NULL PRIMARY KEY,password TEXT)")
            cur.execute("DROP TABLE IF EXITSTS USER")
            cur.execute("CREATE TABLE USER(firstname TEXT,lastname TEXT,email TEXT,username TEXT,FOREIGN KEY (username) REFERENCES ACCOUNT(username))")

@staticmethod
def insertData(username,password,firstname,lastname,email):
    pass

@staticmethod
def veriftData(username,password):
    pass