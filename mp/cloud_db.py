"""
Create a file called dbInfo.json.
Follow week 7 tutorials to get your gCloud DB set up.
Copy the following JSON object into it and adjust it to suit your DB.
{
    "address": "0.0.0.0",
    "username": "root",
    "password":"your_password"
}

Don't forget to add your raspberry pi's IP to allowed connections in gCloud.
"""
import json
import os
import MySQLdb

class cloud_db:
    
    #Largely based off week 7 code supplied.
    DATABASE = "People"

    def __init__(self, connection = None):
        dbInfo = cloud_db.load_json()
        if(connection == None):
            connection = MySQLdb.connect(dbInfo["address"], dbInfo["username"],
                dbInfo["password"], cloud_db.DATABASE)
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createPersonTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists Person (
                    PersonID int not null auto_increment,
                    Name text not null,
                    constraint PK_Person primary key (PersonID)
                )""")
        self.connection.commit()

    def insertPerson(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Person (Name) values (%s)", (name,))
        self.connection.commit()
        return cursor.rowcount == 1

    def getPeople(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select PersonID, Name from Person")
            return cursor.fetchall()
        
    def deletePerson(self, personID):
        with self.connection.cursor() as cursor:
                cursor.execute("delete from Person where PersonID = %s", (personID,))
        self.connection.commit()


    @staticmethod
    def load_json():
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'dbInfo.json')
        with open(filename, 'r') as j:
            return json.load(j)