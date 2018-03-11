class Stack(object):
    def __init__(self):
        self.data = []
        self.top = -1

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return self.top == -1

    def push(self, element_to_push):
        self.top = self.top + 1
        self.data.append(element_to_push)

    def pop(self):
        if (not self.is_empty()):
            self.top = self.top - 1
            return self.data.pop()
        else:
            raise IndexError('Cannot pop from an empty stack')
            return None

s  = Stack()