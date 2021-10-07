import os

import mysql.connector
password = "abdulloh"
db = "lugat"

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database=db
)

tablename = "lugat"


class Lugat:
    def __init__(self):
        self.uzbekcha = None
        self.Inglizcha = None

    def start(self):
        print("Lug`atga so`z kiriting")
        Uzbek = input("Uzbek: ").strip()

        while not self.empty_string(Uzbek.isalpha()):
            self.clear()
            print("So'z kiriting son va belgilar kirintmang")
            Uzbek = input("Uzbek: ").strip()


        English = input("English: ").strip()

        while not self.empty_string(English.isalpha()):
            self.clear()
            print("So'z kiriting son va belgilar kirintmang")
            English = input("English: ").strip()

        self.assigh_user_values(tablename, Uzbek, English)


    def empty_string(self, string):
        return bool(string)

    @staticmethod
    def clear():
        os.system("clear")


    def assigh_user_values(self,table_name,  uzbek, english):
        mycursor = my_db.cursor()
        mycursor.execute(
            f"insert into {table_name} (uzbek, english) values ('{uzbek}', '{english}');")
        my_db.commit()

person = Lugat()
person.start()