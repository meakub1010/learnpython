from DSAndAlgorithms.stack import Stack


class ParenthesesChecker:
    def __init__(self):
        self.symbolStr = ""
    """
    this class use Stack class from stack module and help checking balanced parentheses
    """

    def Check(self, symbolStr):
        print("Given symbol string : ", symbolStr)
        s = Stack()
        balanced = True
        index = 0
        while index < len(symbolStr) and balanced:
            symbol = symbolStr[index]
            if symbol == '(':
                s.push(symbol)
            else:
                if s.isempty():
                    balanced = False
                else:
                    s.pop()
            index += 1
        if balanced and s.isempty():
            return True
        else:
            return False

if __name__ == '__main__':
    obj = ParenthesesChecker()
    print(obj.Check("(((())()())))"))
    print(obj.Check("()()((((((((((((()))))))))))))"))




