"""
python support multiple inheritance.
"""


class Parent:

    name = ""

    def __init__(self):
        self.name = "Muhammad"
        self._greet()

    def display_name(self):
        return "Parent : " + self.name

    def greetings(self):
        return "Hello " + self.name

    _greet = display_name


class Child(Parent):

    def display_name(self):
        return "Child : " + "Ehan"


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for c in [B, C, D]:
    try:
        raise c()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


if __name__ == '__main__':
    child = Child()
    print(child.display_name())
    print(child._greet())
    print(child.greetings())