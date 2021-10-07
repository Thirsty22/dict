print("Hello world")

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdulloh",
    database="log_pass"
)

class Lugat:
    def __init__(self):
        self.uzbekcha = None
        self.INglizcha = None

    def start(self):
        pass

person = Lugat()
person.start()