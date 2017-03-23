"""
Take an integer as input and return factorial of it.
"""


def factorial(n):
    """
    In mathematics, the factorial of a non-negative integer n, denoted by n !, is the product of all positive integers less than or equal to n.
    :param n:
    :return: factorial of n
    """

    fact = 1
    given = n

    if not str(n).isnumeric():
        return n, "invalid input"

    n = int(n)

    if n == 0:
        return given, 1
    elif n < 0:
        return given, "invalid input"

    while n > 0:
        fact *= n
        n -= 1
    return given, fact

if __name__ == '__main__':
    number, fact = factorial(input("Enter a positive integer: "))
    print("Factorial of \'{}\' is : {}".format(number, fact ))