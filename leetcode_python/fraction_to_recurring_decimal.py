# pay attention to edge cases

class Solution:
    def __init__(self):
        self.memo = {}


    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        positive = True
        if numerator < 0:
            numerator *= -1
            positive = not positive
        if denominator < 0:
            denominator *= -1
            positive = not positive

        integer_part = numerator // denominator
        remainder = numerator - denominator * integer_part

        decimal_part = []
        cnt = 0
        while remainder != 0:
            remainder *= 10
            if (remainder, denominator) in self.memo:
                insert_position = self.memo[remainder, denominator][1]
                decimal_part = decimal_part[:insert_position] + ['('] + decimal_part[insert_position:] + [')']
                break
            else:
                self.memo[remainder, denominator] = (remainder // denominator, cnt)
                decimal_part.append(str(self.memo[remainder, denominator][0]))
                remainder -= denominator * self.memo[remainder, denominator][0]
                cnt += 1

        if decimal_part:
            output = str(integer_part) + '.' + ''.join(decimal_part)
        else:
            output = str(integer_part)

        if not positive and output != '0':
            output = '-' + output
        return output
