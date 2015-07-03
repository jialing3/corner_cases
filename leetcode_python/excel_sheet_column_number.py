import string

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        d = dict((_, ind + 1) for ind, _ in enumerate(string.ascii_uppercase))
        output = 0
        counter = 0
        for i in range(len(s) - 1, -1, -1):
            output += d[s[i]] * 26 ** counter
            counter += 1
        return output
