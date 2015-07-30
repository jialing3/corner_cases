class Solution:
    def __init__(self):
        self.letter2number = dict(enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        output = []
        while n:
            output.append(self.letter2number.get((n - 1) % 26))
            n = (n - 1) // 26
        return ''.join(reversed(output))
