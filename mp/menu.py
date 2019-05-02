from cloud_db import cloud_db

class Menu:
    def main(self):
        with cloud_db() as db:
            db.createPersonTable()
        self.runMenu()

    def runMenu(self):
        while(True):
            print()
            print("1. List People")
            print("2. Insert Person")
            print("3. Quit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                self.listPeople()
            elif(selection == "2"):
                self.insertPerson()
            elif(selection == "3"):
                print("Goodbye!")
                break
            else:
                print("Invalid input - please try again.")

    def listPeople(self):
        print("--- People ---")
        print("{:<15} {}".format("Person ID", "Name"))
        with cloud_db() as db:
            for person in db.getPeople():
                print("{:<15} {}".format(person[0], person[1]))

    def insertPerson(self):
        print("--- Insert Person ---")
        name = input("Enter the person's name: ")
        with cloud_db() as db:
            if(db.insertPerson(name)):
                print("{} inserted successfully.".format(name))
            else:
                print("{} failed to be inserted.".format(name))

if __name__ == "__main__":
    Menu().main()