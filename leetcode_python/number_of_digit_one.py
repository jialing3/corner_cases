# n = 136

# power_of_ten = 1
# a = 136, b = 0
# count of right most digit 1 = 14 * 1
# 1, 11, 21, 31, 41, ..., 131

# power_of_ten = 10
# a = 13, b = 6
# count of second digit 1 = 2 * 10
# 11, 12, 13, ..., 19, 111, ...

# power_of_ten = 100
# a = 1, b = 36
# count of additional third digit 1 = 37
# 101, 102, ..., 136

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        count = 0
        power_of_ten = 1
        while power_of_ten <= n:
            a, b = divmod(n, power_of_ten)
            count += (a + 8) // 10 * power_of_ten # whole tens, whole hundreds, ...
            if a % 10 == 1:
                count += b + 1 # remaining after tens. hundreds
            power_of_ten *= 10
        return count
