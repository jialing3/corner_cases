# memoization

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}

    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        elif len(s1) == 0:
            ans = True
        elif sorted(s1) != sorted(s2):
            return False
        elif len(s1) == 1:
            ans = s1 == s2
        #elif len(s1) == 2:
        #    ans = s1 == s2 or list(reversed(s1)) == list(s2)
        else:
            ans = any([(self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])) for i in range(1, len(s1))])

        self.memo[(s1, s2)] = ans
        return ans
