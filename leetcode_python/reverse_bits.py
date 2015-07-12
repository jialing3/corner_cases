# (1 << 31) - 1
# 32-bit unsigned integer

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        digit = 31
        binary = []
        while digit >= 0:
            zero_or_one = n >> digit
            binary.append(zero_or_one)
            if zero_or_one == 1:
                n -= 1 << digit
            digit -= 1

        n = 0
        for digit, zero_or_one in enumerate(binary):
            if zero_or_one == 1:
                n += 1 << digit
        return n
