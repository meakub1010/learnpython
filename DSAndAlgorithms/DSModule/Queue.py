class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isempty(self):
        return self.items.count == 0

    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(13)
    q.enqueue('True')
    q.enqueue(4.5)
    # print(q.dequeue())
    print("size = ", q.size())
    print(q)
    print(q.isempty())
