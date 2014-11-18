class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False # negative sign
        len_x = 1
        while x / 10 ** len_x >= 1:
            len_x += 1
        #len_x = len(x)
        for i in range(len_x / 2):
            if x % 10 ** (i + 1) / 10 ** i != x / 10 ** (len_x - i - 1) % 10:
            # if x[i] != x[len_x - 1 - i]:
                return False
        return True
