class Solution:
    # @return an integer
    def reverse(self, x):
        x = list(str(x))
        initial_pos = 1 if x[0] == '-' else 0
        for i in range(initial_pos, (len(x) + initial_pos) / 2):
            x[i], x[-1 - i + initial_pos] = x[-1 - i + initial_pos], x[i]
        return int(''.join(x))
