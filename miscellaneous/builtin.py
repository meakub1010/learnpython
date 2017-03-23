"""
Explore all the built-in functions in python
"""


def convert_to_binary():
    # inp = int(input("Enter an integer: "))
    inp = 5
    print("Binary of {} is {}".format(inp, bin(inp)))


def any_iterable():
    list = []
    print("list: ", list)
    if any(list):
        print("Iterable is not empty")
    else:
        print("Iterable is empty")


def get_bytearray():
    print("byte array of string ... ")
    print(bytes("t", "utf-8"))
    for item in bytearray("this is string", "utf-8"):
        print(item)

if __name__ == '__main__':
    convert_to_binary()
    any_iterable()
    get_bytearray()