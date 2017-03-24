"""
Callable is something that can be called. A function or class can be callable if __call__ is implemented in that class.
"""


def greetings():
    print("Hello")


class D:
    pass


class C:
    def __call__(self, val):
        """makes the instance of the current class callable"""
        print("Called with param: ", val)

rest = 100

if __name__ == '__main__':

    obj1 = C()
    obj2 = D()

    print("Class C is callable - ", callable(C))
    print("Object of C is callable - ", callable(obj1))
    print("-------------")
    print("Class D is callable - ", callable(D))
    print("Object of D is callable - ", callable(obj2))
    print("-------------")
    print("Function greetings() is callable - ", callable(greetings))
    print("Variable rest is callable - ", callable(rest))
    print("INT is callable - ", callable(int))

