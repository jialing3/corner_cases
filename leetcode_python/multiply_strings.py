class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'


        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        result = []
        overflow = 0

        for i in range(len(num1) + len(num2) - 1):
            accumulator = overflow
            for j in range(i + 1):
                if j < len(num1) and 0 <= i - j < len(num2): # key
                    n1, n2 = num1[j], num2[i - j]
                    accumulator += int(n1) * int(n2)
            overflow, accumulator = divmod(accumulator, 10)
            result.append(accumulator)

        if overflow != 0: # no leading 0
            result.append(overflow)

        return ''.join(reversed(map(lambda x: str(x), result)))
