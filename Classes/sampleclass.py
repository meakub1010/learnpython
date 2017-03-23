class C:
    """
    This calss use @property decorator to create class property
    """
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """ property of C class"""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class D:
    """
    This class use property class to create class property
    """

    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "Property of D class")



if __name__ == '__main__':
    obj = C()
    obj.x = 5
    print(obj.x)

    # obj = C()
    # print(obj.x)

    ob = D()
    ob.x = 10

    print(ob.x * obj.x)

