class Stack:
    """
    Stack implementation using built in list in python and top of the stack is considered as the end of the list
    """
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Stack2:
    """
    considering front of the list is the top of the stack
    """
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        """
        take the item and insert in 0th position of  the list. Since oth position is considered as the top of the stack
        :param: item to be inserted
        """
        self.items.insert(0, item)

    def pop(self):
        """
        return the 0th item of the list and remove it from the list
        :return:
        """
        return self.items.pop(0)

    def peek(self):
        """
        just return the oth item of the list but don't remove it
        :return: 0th item of the list
        """
        return self.items[0]

    def size(self):
        """
        :return - return the length of the list
        :return:
        """
        return len(self.items)
