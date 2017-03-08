from DSAndAlgorithms.stack import Stack


class ConvertNumbers:

    def convertdecimaltobinary(self, number):
        s = Stack()
        while number > 0:
            s.push(number % 2)
            number //= 2

        binString = ""
        while not s.isempty():
            binString += str(s.pop()) + ' '

        return binString

if __name__ == '__main__':
    obj = ConvertNumbers()
    print(obj.convertdecimaltobinary(24))
