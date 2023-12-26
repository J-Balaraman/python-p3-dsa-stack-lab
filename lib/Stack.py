class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) > self.limit:
            while len(self.items) != self.limit:
                self.items.pop()
        return True

    def search(self, target):
        num = 1
        for element in self.items:
            if element == target:
                return (len(self.items) - num)
            else:
                num += 1
        return -1