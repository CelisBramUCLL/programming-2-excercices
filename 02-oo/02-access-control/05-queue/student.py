class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def next(self):
        item = self.queue[0]
        self.queue.pop(0)
        return item

    def is_empty(self):
        return len(self.queue) == 0
