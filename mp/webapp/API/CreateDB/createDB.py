import MySQLdb


class CreateDB:

    def __init__(self):
        HOST = "35.201.19.68"
        USER = "root"
        PASSWORD = "klLBK8BxKmNOfhkE"
        DATABASE = "Library_test"
        self.connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
        
    def createTables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(open("sql1.2.sql", "r").read())
        self.connection.commit()

if __name__ == "__main__":
    db = CreateDB()
    db.createTables()