class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            elif len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    num3 = num1 + num2
                elif token == '-':
                    num3 = num1 - num2
                elif token == '*':
                    num3 = num1 * num2
                else:
                    num3 = int(1. * num1 / num2)
                stack.append(num3)
        return stack[-1]
