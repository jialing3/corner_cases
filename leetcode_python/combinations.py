class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        return self.combine_recursive(k, range(1, n + 1))


    def combine_recursive(self, k, n_list):
        if k == 1:
            return [[x] for x in n_list]
        else:
            return [lst + [x] for lst in self.combine_recursive(k - 1, n_list) for x in n_list if x > max(lst)]
