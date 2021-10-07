import os

import mysql.connector
password = "123456789"
db = "lugat"

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password= password,
    database= db
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

    def izlash(self):
        self.clear()
        print("Izlanmoqda")
        soz = input("So`zni kiriting: ")
        while not self.empty_string(soz.isalpha()):
            self.clear()
            print("So'z kiriting son va belgilar kirintmang")
            soz = input("So`zni kiriting: ")
        print("7")


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

    def izlash_uchun(self, table_name, title, info):
        mycursor = my_db.cursor()
        mycursor.execute(f"select * from {table_name} where {title} = '{info}';")
        mycursor_1=mycursor.fetchall()

        if mycursor_1:
            return True
        return False



person = Lugat()
person.start()