class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):

        def get_next_level(current_permutation):
            return [current_permutation + [i] for i in num if i not in current_permutation]

        current_level = [[n] for n in num]

        for i in range(1, len(num)):
            last_level = current_level
            current_level = []
            for current_permutation in last_level:
                current_level.extend(get_next_level(current_permutation))

        return current_level
