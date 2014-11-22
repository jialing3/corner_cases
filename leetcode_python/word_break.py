# Norvig has a more sophisticated version of this...
# memoize and dynamically split words from back to the front

class Solution:
    def __init__(self):
        self.memo = {}

    def valid_combos(self, s, dict__):
        return [s[:i] for i in range(len(s)) if s[i:] in dict__]

    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict__):
        if s == '':
            return True
        elif s in self.memo:
            return self.memo.get(s)
        else:
            dict__ = set(dict__)
            ans = any(self.wordBreak(remaining, dict__) for remaining in self.valid_combos(s, dict__))
            self.memo[s] = ans
            return ans

        
