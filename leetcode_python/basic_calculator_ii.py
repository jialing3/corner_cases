class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        nums = set(map(lambda x: str(x), range(10)))
        stack = []
        for x in s:
            if x == ' ':
                continue
            elif x in nums:
                if (len(stack) > 0 and any([_ not in nums for _ in stack[-1]])) or len(stack) == 0: # key
                    stack.append(x)
                else:
                    stack[-1] = stack[-1] + x
            else:
                stack.append(x)
        # stack = re.split('(\D)', s.replace(' ', ''))

        stack_2 = []
        for x in stack:
            if x in set(['+', '-', '*', '/']):
                stack_2.append(x)
            else:
                x = int(x) # key
                if len(stack_2) == 0: # key
                    stack_2.append(x)
                elif stack_2[-1] in set(['*', '/']):
                    operator = stack_2.pop()
                    if operator == '*':
                        stack_2[-1] *= x
                    else:
                        stack_2[-1] /= x
                else:
                    stack_2.append(x)

        current = None
        for ind, x in enumerate(stack_2):
            if x in set(['+', '-']):
                continue
            else:
                if current is None: # 0 is False
                    current = x
                else:
                    if stack_2[ind - 1] == '+':
                        current += x
                    else:
                        current -= x

        return current
