class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])

        def partial(left, right):
            if left == right:
                return [nums[left]]
            else:
                return [ops[i](x, y)
                        for i in range(left, right)
                        for x in partial(left, i)
                        for y in partial(i + 1, right)]
        return partial(0, len(ops))
