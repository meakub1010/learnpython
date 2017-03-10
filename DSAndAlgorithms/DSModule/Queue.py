class Queue:
    def __init__(self):
        self.items = []

    def enque(self, item):
        self.items.insert(0, item)

    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isempty(self):
        return self.items.count == 0

    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enque(13)
    q.enque('True')
    q.enque(4.5)
    # print(q.deque())
    print("size = ", q.size())
    print(q)
    print(q.isempty())
