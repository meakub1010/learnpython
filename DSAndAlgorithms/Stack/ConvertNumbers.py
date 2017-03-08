from DSAndAlgorithms.DSModule.stack import Stack


class ConvertNumbers:

    def convertdecimaltobinary(self, number):
        s = Stack()
        while number > 0:
            s.push(number % 2)
            number //= 2

        result_string = ""
        while not s.isempty():
            result_string += str(s.pop()) + ' '

        return result_string

if __name__ == '__main__':
    obj = ConvertNumbers()
    print(obj.convertdecimaltobinary(30))