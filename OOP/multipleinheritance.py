"""
Illustrate multiple inheritance in python
"""


class A1:
    def name(self):
        return "B1-->A1"


class B1(A1):
    pass


class B2:
    def name(self):
        """ can't be reached, since class A1(base class of B1) has the definition of name method """
        return "B2"

    def Age(self):
        """ will be called since class B1 doesn't have the defintion of Age method """
        return "B2-16"


class B3:
    def name(self):
        return "B3"

    def Age(self):
        """ can't be reached, since class B2 has the definition of Age method """
        return "B3-18"


class Child(B1, B2, B3):
    """
    search Salary method in class B1 then B2 then finally B3.
    """
    def Salary(self):
        return "100K"


if __name__ == '__main__':
    c = Child()

    print(c.name())
    print(c.Age())
    print(c.Salary())
