# recursion or DP
# Sometimes, 10 lines of code can mean more than 1000 words

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        current_row = [True] + [False] * len(p)
        # compare p[:j] to ''
        for j in range(2, len(p) + 1): # 2
            if p[j - 1] == '*':
                current_row[j] = current_row[j - 2]
        # compare p[:j] to s[:i]
        for i in range(1, len(s) + 1):
            last_row = current_row[:]
            current_row = [False] * (len(p) + 1)
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.':
                    current_row[j] = last_row[j - 1]
                elif p[j - 1] == '*':
                    current_row[j] = current_row[j - 1] or current_row[j - 2] or (last_row[j] and p[j - 2] in (s[i - 1], '.')) # j - 2
                else:
                    current_row[j] = last_row[j - 1] and s[i - 1] == p[j - 1]
        return current_row[-1]
