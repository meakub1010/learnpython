from DSAndAlgorithms.DSModule.stack import Stack


def convert_infix_to_postfix(infixexpr):
    precedence_dict = {}
    precedence_dict["*"] = 3
    precedence_dict["/"] = 3
    precedence_dict["+"] = 2
    precedence_dict["-"] = 2
    precedence_dict["("] = 1

    opStack = Stack()

    result_string = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            result_string.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                result_string.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isempty()) and precedence_dict[opStack.peek()] >= precedence_dict[token]:
                result_string.append(opStack.pop())
            opStack.push(token)


    while not opStack.isempty():
        result_string.append(opStack.pop())

    return " ".join(result_string)


print("A * B + C * D ===> ", convert_infix_to_postfix("A * B + C * D"))

print("(A + B) * C / D ===>", convert_infix_to_postfix("( A + B ) * C / D"))
