from DSAndAlgorithms.stack import Stack


def parChecker(symbolStr):
    print("Given symbol string : ", symbolStr)
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolStr) and balanced:
        ltrl = symbolStr[index]
        if ltrl == '(':
            s.push(ltrl)
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

print(parChecker("(((())()())))"))
print(parChecker("()()((((((((((((()))))))))))))"))



