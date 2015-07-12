# use a stack
# FILO

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if not x:
            return x
        if x < 0:
            minus = True
            x = -x
        else:
            minus = False
        mod = 10
        stack = []
        while x > 0:
            stack.append(x % mod)
            x = x // mod
        x = 0
        max__ = 2 ** 31 - 1
        while stack:
            current_digit = stack.pop(0) # O[n], can use another stack to flip the original stack
            if x == 0 and current_digit == 0:
                pass
            else:
                x += current_digit * 10 ** len(stack)
            if x > max__:
                return 0
        if minus is True:
            x = -x
        return x
            
