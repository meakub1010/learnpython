"""A module for demonstrating exception handling in python """

import sys


def convert(s):
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):
        pass
    return x


def convert2(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return -1


def convert3(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1