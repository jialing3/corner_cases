# "()(()"

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = []
        max_length = 0
        for ind, c in enumerate(s):
            if c == '(':
                stack.append((ind, c))
            elif c == ')':
                if stack and stack[-1][1] == '(':
                    stack.pop()
                    max_length = max(max_length, ind - stack[-1][0] if stack else (ind + 1))
                    # if stack is empty: current length is ind + 1
                    # else: current length is ind - top_ind_on_stack
                else:
                    stack.append((ind, c))
        return max_length
