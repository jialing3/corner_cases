class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return x
        x = list(str(x))
        if x[0] == '-':
            extra = '-'
            x.pop(0)
        else:
            extra = None
        for ind in reversed(range(len(x))):
            if x[ind] == '0':
                x.pop(ind)
            else:
                break
        for ind in range(len(x) / 2):
            x[ind], x[len(x) - 1 - ind] = x[len(x) - 1 - ind], x[ind]
        if extra:
            x = [extra] + x
        return int(''.join(x))
