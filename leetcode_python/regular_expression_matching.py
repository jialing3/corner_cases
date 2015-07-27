# recursion or DP
# Sometimes, 10 lines of code can mean more than 1000 words

class Solution:

    def memo(f):
        "Memoize function f."
        table = {}
        def fmemo(*args):
            if args not in table:
                table[args] = f(*args)
            return table[args]
        fmemo.memo = table
        return fmemo


    # @param {string} s
    # @param {string} p
    # @return {boolean}
    @memo
    def isMatch(self, s, p):
        if p == '':
            return s == ''
        elif len(p) == 1 or p[1] != '*':
            if s == '' or p[0] not in (s[0], '.'):
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        else: # p[1] is '*'
            if self.isMatch(s, p[2:]):
                return True
            i = 0
            while i < len(s) and p[0] in (s[i], '.'):
                if self.isMatch(s[i + 1:], p[2:]):
                    return True
                i += 1
            return False
