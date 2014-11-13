class MinStack:
    def __init__(self):
        self.stack = [] # LIFO
        self.minima = [] # stack to keep the most current mins

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.minima or x <= self.minima[-1]:
            self.minima.append(x)

    # @return nothing
    def pop(self):
        popped = self.stack.pop()
        if popped == self.minima[-1]:
            self.minima.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if self.minima:
            return self.minima[-1]
