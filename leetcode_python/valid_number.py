# finite state solution

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        INVALID, SPACE, SIGN, DIGIT, DOT, EXPONENT = range(6)
        transition_table = [[-1,  0,  3,  1,  2, -1], # 0 no entry or have only entered spaces
                            [-1,  8, -1,  1,  4,  5], # 1 have only entered numbers and possibly a sign
                            [-1, -1, -1,  4, -1, -1], # 2 no numbers entered yet, have just entered a dot and possibly a sign
                            [-1, -1, -1,  1,  2, -1], # 3 have only entered a sign
                            [-1,  8, -1,  4, -1,  5], # 4 have entered numbers and a dot
                            [-1, -1,  6,  7, -1, -1], # 5 have entered 'e' or 'E'
                            [-1, -1, -1,  7, -1, -1], # 6 have entered a sign after 'e' or 'E'
                            [-1,  8, -1,  7, -1, -1], # 7 have entered numbers (and possibly a sign) after 'e' or 'E'
                            [-1,  8, -1, -1, -1, -1], # 8 previously valid, now entering spaces
                            ]
        current_state = 0
        for c in s:
            if c == ' ':
                input = SPACE
            elif c in ('+', '-'):
                input = SIGN
            elif c in ('0123456789'):
                input = DIGIT
            elif c == '.':
                input = DOT
            elif c in ('e', 'E'):
                input = EXPONENT
            else:
                input = INVALID
            current_state = transition_table[current_state][input]
            if current_state == -1:
                return False
        return current_state in (1, 4, 7, 8)
