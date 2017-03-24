"""
all about class and instance member of the class.
"""


class Worker:
    address = None # class variable

    def __init__(self, name, id):
        self.name = name  # instance variable
        self.id = id  # instance variable

    @classmethod
    def greetings(self):
        return "Hello"

    @staticmethod
    def display():
        print("Hello")

if __name__ == '__main__':
    Worker.address = "13209 83rd street"
    w1 = Worker("Muhammad", 126)
    w2 = Worker("Ehan", 700)
    print("Name : {}\n id : {}\n Address : {}".format(w1.name, w1.id, w1.address))
    print("Name : {}\n id : {}\n Address : {}".format(w2.name, w2.id, w2.address))
    w1.display()
    w1.greetings()