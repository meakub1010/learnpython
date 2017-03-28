def foo(param1, param2):
    """
    this is function and not associated with any object/instance. can be called directly with any instance
    :param param1:
    :param param2:
    :return:
    """
    return param1 + " " + param2


class Foo:
    def foo(self, param1, param2):
        """
        this is method associated with the object of Foo class
        :param param1: anything
        :param param2: anything
        :return: concatenate params
        """
        return param1 + " " + param2


if __name__ == '__main__':
    print(foo("hi", "there"))
    print(Foo().foo("hi", "there!"))