from DSAndAlgorithms.DSModule.stack import Stack


def convert_infix_to_postfix(infixexpr):
    precedence_dict = {"**": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    opStack = Stack()

    result_string = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token.isnumeric():
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


#print("A * B + C * D ===> ", convert_infix_to_postfix("A * B + C * D"))

#print("( A + B ) * C / D ===>", convert_infix_to_postfix("( A + B ) * C / D"))

#print("A + B * C ===>", convert_infix_to_postfix("A + B * C"))

#print(convert_infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )"))

print(convert_infix_to_postfix("5 * 3 ** ( 4 - 2 )"))