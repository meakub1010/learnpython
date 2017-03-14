""" Model for aircraft flights """


class Flight:

    def __init__(self, number):
        self._number = number # 1. _ used to avoid name clash with method named ""

    def number(self):
        return "SN060"