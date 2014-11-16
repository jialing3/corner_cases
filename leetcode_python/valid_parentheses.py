class Solution:
    pairs = dict(['()', '[]', '{}'])
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}':
                if not stack:
                    return False
                last = stack.pop()
                if self.pairs[last] != c:
                    return False
        return len(stack) == 0
        
