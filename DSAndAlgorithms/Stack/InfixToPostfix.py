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

