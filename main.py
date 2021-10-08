import os
import mysql.connector

password = "abdulloh"
db = "lugat"

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = password,
    database = db
)

tablename = "lugat"


class Lugat:
    def __init__(self):
        self.uzbekcha = None
        self.Inglizcha = None

    def tanlash(self):
        self.clear()
        print("""
********************************************
* Yangi so'z qo'shish                  [1] *
* Lug'at ichidagi so'zlarni ko'rish    [2] *
* Izlash                               [3] *
* Chiqish                              [4] *
********************************************
        """)
        option = ['1', '2', '3', '4']
        input_num = input("[1-4]: ").strip()

        while input_num not in option:
            self.clear()
            print("Bunaqa raqam yo'q!")
            input_num = input("[1-4]: ")

        if input_num == option[0]:
            self.qoshishqismi()
        elif input_num == option[1]:
            print("Lug'at ichidagi so'zlarni ko'rish")
            self.lugati_ichini_korish()
        elif input_num == option[2]:
            self.izlash()
        else:
            exit()

    def qoshishqismi(self):
        print("Lug`atga so`z kiriting")
        uzbek = input("Uzbek: ").strip().lower()

        while not self.empty_string(uzbek.isalpha()):
            self.clear()
            print("So'z kiriting son va belgilar kirintmang")
            uzbek = input("Uzbek: ").strip()


        english = input("English: ").strip().lower()

        while not self.empty_string(english.isalpha()):
            self.clear()
            print("So'z kiriting son va belgilar kirintmang")
            english = input("English: ").strip()

        self.assigh_user_values(tablename, uzbek, english)
        self.clear()
        print(f"Qo'shilgan so'zlar: {uzbek} - {english}")
        self.tizizga_qaytish()


    def lugati_ichini_korish(self):
        mycursor = my_db.cursor()
        mycursor.execute(f"select * from {tablename};")
        new_mycursor = mycursor.fetchall()
        [print(list(row)) for row in new_mycursor]

    def izlash(self):
        self.clear()
        print("Izlanmoqda")
        soz = input("So`zni kiriting: ")
        while not self.empty_string(soz.isalpha()):
            self.clear()
            print("So'z kiriting son va belgilar kirintmang")
            soz = input("So`zni kiriting: ")



    def empty_string(self, string):
        return bool(string)

    @staticmethod
    def clear():
        os.system("clear")


    def assigh_user_values(self, table_name, uzbek, english):
        mycursor = my_db.cursor()
        mycursor.execute(
            f"insert into {table_name} (uzbek, english) values ('{uzbek}', '{english}');")
        my_db.commit()

    def izlash_uchun(self, table_name, title, info):
        mycursor = my_db.cursor()
        mycursor.execute(f"select * from {table_name} where {title} = '{info}';")
        mycursor_1 = mycursor.fetchall()

        if mycursor_1:
            return True
        return False


    @staticmethod
    def chiqsih():
        self.clear()
        print("Tizimdan muffaqiyatlik chiqip kettingiz! ")
        exit()

    def tizizga_qaytish(self):
        tanlash = input("Bosh sahifaga o'tasizmi yoki dasturdan chiqip ketasizmi?\n"
                        "[y/n]: ")
        tanlash_option = ['yes', 'y', 'n', 'no']

        while tanlash not in tanlash_option:
            self.clear_and_invalid_text("")
            tanlash = input("[y/n]: ")

        if tanlash == tanlash_option[0] or tanlash == tanlash_option[1]:
            self.clear()
            self.tanlash()
        else:
            self.chiqsih()



person = Lugat()
person.tanlash()


