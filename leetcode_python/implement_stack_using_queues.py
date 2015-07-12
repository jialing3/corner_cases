class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.hidden = []


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)


    # @return nothing
    def pop(self):
        self.top()


    # @return an integer
    def top(self):
        size = len(self.stack)
        if size == 0:
            return
        for i in range(size - 1):
            self.hidden.append(self.stack.pop(0))
        top = self.stack.pop(0)
        self.stack.append(top)
        for i in range(size - 1):
            self.stack.append(self.hidden.pop(0))
        return top


    # @return an boolean
    def empty(self):
        return len(self.stack) == 0 # bool
