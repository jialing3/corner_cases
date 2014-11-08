class Solution:
    # @param s, a string
    # @return an integer
    memo = dict()

    def numDecodings(self, s): # recurse from left to right
        if s in self.memo:
            return self.memo.get(s)

        if len(s) == 0 or s == '0':
            self.memo[s] = 0
            return 0
        elif len(s) == 1:
            self.memo[s] = 1
            return 1
        elif len(s) == 2:
            if s in ('10', '20'):
                self.memo[s] = 1
                return 1
            elif s in [str(x) for x in range(11, 27)]:
                self.memo[s] = 2
                return 2
            elif '0' in s:
                self.memo[s] = 0
                return 0
            else:
                self.memo[s] = 1
                return 1
        else:
            if s[-2:] in ('10', '20'):
                self.memo[s] = self.numDecodings(s[:-2])
                return self.memo[s]
            elif s[-2:] in [str(x) for x in range(11, 27)]:
                self.memo[s] = self.numDecodings(s[:-1]) + self.numDecodings(s[:-2])
                return self.memo[s]
            elif s[-1] == '0':
                self.memo[s] = 0
                return 0
            else:
                self.memo[s] = self.numDecodings(s[:-1])
                return self.memo[s]

                
