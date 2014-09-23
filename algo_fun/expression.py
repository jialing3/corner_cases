## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.

"""
 ONE
+ONE
----
 TWO

 231
+231
----
 462

 FOUR
+FOUR
-----
EIGHT

 5239
 5239
 ----
10478

interface Expression {
  Set<Char> getChars();  # all chars used
  boolean evaluate(Map<Char, Int> m);  # true if substitution solves the problem
}
"""

class Expression:
    def __init__(self, str1, str2, str3):
        self.strs = [str1, str2, str3]

    def getChars(self):
        return set(self.strs[0]) | set(self.strs[1]) | set(self.strs[2])

    def char_to_num(self, m, str):
        new_str = []
        for c in str: # str is a list, ONE
            new_str.append(m.get(c))
        return int(new_str)

    def evaluate(self, m): # m = {'a': 1, 'b': 2}
        return self.char_to_num(m, self.strs[0]) + self.char_to_num(m, self.strs[1]) == self.char_to_num(m, self.strs[2])



# Map<Char, Int> solve(Expression e)
e = Expression('ONE', 'ONE', 'TWO')

def solve(e):
    chars = e.getChars()
    n = len(chars)
    return walk([str(x) for x in range(10)], [], n, e, chars)


def walk(remaining, taken, n, e, chars): # n is the total len(getChars)
    if len(taken) == n:
        m = dict([(c, num) for c, num in zip(chars, path)])
        if e.evaluate(m):
            return m
    else:
        for ind in range(len(remaining)):
            tmp = walk(remaining[:ind] + remaining[ind+1:], taken + [remaining[ind]], n, e, chars)
            if tmp is not None:
                return tmp
    return None
    
