from DSAndAlgorithms.DSModule.stack import Stack


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
            if symbol in '([{':
                s.push(symbol)
            else:
                if s.isempty():
                    balanced = False
                else:
                    top = s.pop()
                    if not self.matches(top, symbol):
                        balanced = False
            index += 1
        if balanced and s.isempty():
            return True
        else:
            return False

    def matches(self, top, close):
        opens = "({["
        closes = ")}]"
        return opens.index(top) == closes.index(close)


if __name__ == '__main__':
    obj = ParenthesesChecker()
    print(obj.Check("([])("))
    print(obj.Check("()()((((((((((((()))))))))))))"))




