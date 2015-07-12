class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.queue = [] # can only use append(), pop() and len
        self.hidden = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        while len(self.queue): # bool will be faster
            self.hidden.append(self.queue.pop())
        tmp = self.hidden.pop()
        while len(self.hidden):
            self.queue.append(self.hidden.pop())
        return tmp

    # @return an integer
    def peek(self):
        while len(self.queue):
            self.hidden.append(self.queue.pop())
        tmp = self.hidden.pop()
        self.queue.append(tmp)
        while len(self.hidden):
            self.queue.append(self.hidden.pop())
        return tmp

    # @return an boolean
    def empty(self):
        return len(self.queue) == 0 # bool is better
