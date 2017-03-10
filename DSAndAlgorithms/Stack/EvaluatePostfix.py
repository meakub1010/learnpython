from DSAndAlgorithms.DSModule.stack import Stack


def evaluate_postfix(postfixString):

    operandStack = Stack()
    tokenList = postfixString.split()
    for token in tokenList:
        if token.isnumeric():
            operandStack.push(int(token))
        else:
            try:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(token, operand1, operand2)
            except (IndexError, ValueError):
                result = "Invalid input"
                return result
            operandStack.push(result)
    return operandStack.pop()


def doMath(operator, operand1, operand2):
    if operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    elif operator == "+":
        result = operand1 + operand2
    elif operator == "==":
        result = operand1 == operand2
    elif operator == "**":
        result = operand1 ** operand2
    else:
        result = operand1 - operand2

    return result


print("'7 8 + 3 2 + /' ==>", evaluate_postfix("7 8 + 3 2 + /"))

print("'17 10 + 3 * 9 / * =='  ==>", evaluate_postfix("17 10 + 3 * 9 / 8 =="))

print("'17 10 + 3 * 9 / 2 **'  ==>", evaluate_postfix("17 10 + 3 * 9 / 2 **"))

print("'17 10 + 3 * 9 / =='  ==>", evaluate_postfix("17 10 + 3 * 9 / =="))

print(evaluate_postfix("5 * 3 ** ( 4 - 2 )"))