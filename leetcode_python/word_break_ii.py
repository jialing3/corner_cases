# Norvig comes to the rescue

class Solution:
    def __init__(self):
        self.memo = {'': ['']}

    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        if s in self.memo:
            return self.memo.get(s)
        else:
            ans = [(combo + ' ' + s[i:] if combo else s[i:]) for i in range(len(s)) if s[i:] in wordDict for combo in self.wordBreak(s[:i], wordDict)]
            self.memo[s] = ans
            return ans
