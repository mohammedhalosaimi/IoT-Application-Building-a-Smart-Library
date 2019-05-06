# Reference: https://docs.python.org/2/library/unittest.html
import unittest
import MySQLdb
from database_utils import DatabaseUtils

# class TestDatabaseUtils(unittest.TestCase):
class TestDatabaseUtils:
    # HOST = "35.201.18.142"
    # USER = "root"
    # PASSWORD = "abc123"
    # DATABASE = "TestPeople"

    def setUp(self):
        db = DatabaseUtils()
        db.insertUser("user_name_1")
        db.listUsers()
        # self.connection = MySQLdb.connect(TestDatabaseUtils.HOST, TestDatabaseUtils.USER,
        #     TestDatabaseUtils.PASSWORD, TestDatabaseUtils.DATABASE)
        
        # with self.connection.cursor() as cursor:
        #     cursor.execute("drop table if exists Person")
        #     cursor.execute("""
        #         create table if not exists Person (
        #             PersonID int not null auto_increment,
        #             Name text not null,
        #             constraint PK_Person primary key (PersonID)
        #         )""")
        #     cursor.execute("insert into Person (Name) values ('Matthew')")
        #     cursor.execute("insert into Person (Name) values ('Shekhar')")
        #     cursor.execute("insert into Person (Name) values ('Rodney')")
        # self.connection.commit()


    # def tearDown(self):
    #     try:
    #         self.connection.close()
    #     except:
    #         pass
    #     finally:
    #         self.connection = None

    # def countPeople(self):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("select count(*) from Person")
    #         return cursor.fetchone()[0]

    # def personExists(self, personID):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("select count(*) from Person where PersonID = %s", (personID,))
    #         return cursor.fetchone()[0] == 1

    # def test_insertPerson(self):
    #     with DatabaseUtils(self.connection) as db:
    #         count = self.countPeople()
    #         self.assertTrue(db.insertPerson("Kevin"))
    #         self.assertTrue(count + 1 == self.countPeople())
    #         self.assertTrue(db.insertPerson("Ryan"))
    #         self.assertTrue(count + 2 == self.countPeople())

    # def test_getPeople(self):
    #     with DatabaseUtils(self.connection) as db:
    #         self.assertTrue(self.countPeople() == len(db.getPeople()))

    # def test_deletePerson(self):
    #     with DatabaseUtils(self.connection) as db:
    #         count = self.countPeople()
    #         personID = 1

    #         self.assertTrue(self.personExists(personID))

    #         db.deletePerson(personID)

    #         self.assertFalse(self.personExists(personID))
    #         self.assertTrue(count - 1 == self.countPeople())

# if __name__ == "__main__":
#     unittest.main()

TestDatabaseUtils().setUp()
