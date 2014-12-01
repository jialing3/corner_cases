# input:	1, -1

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor < 0 and dividend > 0:
            divisor = -divisor
            sign = -1
        elif divisor > 0 and dividend < 0:
            dividend = -dividend
            sign = -1
        elif divisor < 0 and dividend < 0:
            dividend = -dividend
            divisor = -divisor
            sign = 1
        else:
            sign = 1

        output = 0
        while dividend >= divisor:
            multiplier = 0
            divisor_multiplied = divisor
            while dividend >= divisor_multiplied:
                output += 1 << multiplier
                dividend -= divisor_multiplied
                divisor_multiplied <<= 1 # times 2
                multiplier += 1

        if sign == -1:
            output = -output
        return output
