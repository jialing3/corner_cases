class Solution:
    def __init__(self):
        self.memo = {}

    split_and_valid = lambda self, y: all(self.validate(x) for x in y.split('.'))

    validate = lambda self, x: False if len(x) > 1 and x[0] == '0' else int(x) < 256 # leading zeros

    def divide(self, s):
        if s in self.memo:
            return self.memo[s]
        else:
            if len(s) == 0:
                self.memo[s] = ['']
                return self.memo[s]
            elif len(s) == 1:
                self.memo[s] = [s]
                return self.memo[s]
            elif len(s) > 12: # too long
                return ['']
            else:
                #post = self.divide(s[1:])
                pre = self.divide(s[:-1])
                self.memo[s] = list(set(([s] if self.split_and_valid(s) else []) +
                    #[s[0] + '.' + x for x in post if self.split_and_valid(x)] +
                    [x + '.' + s[-1] for x in pre if self.split_and_valid(x)] +
                    #[s[0] + x for x in post if self.split_and_valid(s[0] + x)] +
                    [x + s[-1] for x in pre if self.split_and_valid(x + s[-1])]))
                    # two types of concatenation
                return self.memo[s]

    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        return [x for x in self.divide(s) if len(x.split('.')) == 4]
