"""
yield help us with custom iteration over a collection
"""


def print_numbers(numbers):
    for num in numbers:
        print(num)


def print_greater_than_five(numbers):
    for num in numbers:
        if num > 4:
            yield num


def running_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
        yield sum


def running_avg(numbers):
    sum = 0
    for index, val in enumerate(numbers):
        sum += val
        yield sum/(index+1)


def sum_of_n():
    inp = int(input("Enter an integer: "))
    result = 0
    result2 = (inp * (inp + 1)) / 2
    while inp > 0:
        result += inp
        inp -= 1
    return result, result2


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_numbers(numbers)

    # yield will return only items greater than 5
    print("Using yield return >= 5... ")
    for item in print_greater_than_five(numbers):
        print(item)

    print("Running sum ... ")
    for sum in running_sum(numbers):
        print(sum)

    print("Running avg ... ")
    for item in running_avg(numbers):
        print(item)

    result, result2 = sum_of_n()

    print("Sum series : ", result2)
    print("Sum while :", result)