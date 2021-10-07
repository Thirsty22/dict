import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2160900",
    database="lugat"
)


class Lugat:
    def __init__(self):
        self.uzbekcha = None
        self.Inglizcha = None

    def start(self):
        print("Lug`atga so`z kiriting")
        Uzbek = input("Uzbek: ")
        English = input("English: ")


person = Lugat()
person.start()