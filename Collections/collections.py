def minmax(items):
    return min(items), max(items)


def print_minmax():
    """
    Evaluate min and max function against list
    """
    print("(min, max) =  ", minmax([34, 23, 79, 10]))
    lower, upper = minmax([34, 23, 79, 10])
    # assign tuple to multiple variables
    print("Min = ", lower)
    print("Max = ", upper)


if __name__ == '__main__':
    print_minmax()
