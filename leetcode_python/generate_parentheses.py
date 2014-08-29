class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        def get_next_arrangements(arrangement, n):
            left = arrangement.count('(')
            right = arrangement.count(')')
            if left > n:
                return []
            else:
                if left == right:
                    return [arrangement + ['(']]
                elif left < right:
                    return []
                elif n == left:
                    return [arrangement + [')']]
                else:
                    return [arrangement + ['('], arrangement + [')']]


        current = [['(']]

        for level in range(1, n * 2):
            past = current
            current = []
            for arrangement in past:
                current.extend(get_next_arrangements(arrangement, n))


        return [''.join(solution) for solution in current]
