class Solution:
    def __init__(self):
        self.lookup = ['_', ' ', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.lookup = dict(enumerate(self.lookup))

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        current = ['']
        for digit in digits:
            current = [a + b for a in current for b in self.lookup[int(digit)]]
        return current
