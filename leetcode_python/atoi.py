'''
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''

class Solution:
    # @return an integer
    def atoi(self, str__):
        stack = []
        sign = '+'
        for c in str__:
            if len(stack) == 0: # empty stack
                c = c.strip() # inside if
                if c == '':
                    pass
                elif c in '+-0123456789':
                    stack.append(c)
                else:
                    return 0
            else: # non-empty stack
                if c in '0123456789':
                    stack.append(c)
                else:
                    break # break
        # output
        if len(stack) > 0 and stack[0] in '+-': # first check for empty stack
            sign = stack.pop(0)
        if len(stack) == 0: # input = '+-2'
            return 0
        elif len(stack) < len('2147483648'):
            return int(sign + ''.join(stack))
        elif len(stack) > len('2147483648'):
            return 2147483647 if sign == '+' else -2147483648
        elif ''.join(stack) <= '2147483647': # 7 and 8, list and str
            return int(sign + ''.join(stack))
        else:
            return 2147483647 if sign == '+' else -2147483648
