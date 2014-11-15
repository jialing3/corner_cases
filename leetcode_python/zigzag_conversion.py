class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        result = [[] for i in range(nRows)]
        for i, c in enumerate(s):
            if (i / (nRows - 1)) % 2 == 0:
                result[i % (nRows - 1)].append(c)
            else:
                result[nRows - 1 - i % (nRows - 1)].append(c)
        result = [''.join(row) for row in result]
        result = ''.join(result)
        return result
