class Solution:
    # use a stack

    # @return a string
    def countAndSay_helper(self, n):
        result = []
        stack = []
        for current in n + '_':
            if len(stack) > 0 and stack[-1] != current: # pop
                cnt = 0
                while stack:
                    number = stack.pop()
                    cnt += 1
                result.append(str(cnt))
                result.append(number)
            stack.append(current) # push
        return ''.join(result)

    def countAndSay(self, n):
        start = '1'
        for i in range(1, n):
            start = self.countAndSay_helper(start)
        return start
