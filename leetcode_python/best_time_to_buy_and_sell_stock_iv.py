# local_max is for sales that ended on the i-th day

class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if len(prices) == 0:
            return 0
        if k >= len(prices) / 2:
            return self.sweep(prices)
        global_max = [0 for _ in range(k + 1)]
        local_max = [0 for _ in range(k + 1)]
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            last_global = global_max[:]
            last_local = local_max[:]
            for j in range(1, k + 1):
                local_max[j] = max(last_local[j] + diff,
                                      last_global[j - 1] + max(diff, 0))
                global_max[j] = max(last_global[j],
                                       local_max[j])
        return global_max[k]

    def sweep(self, prices):
        output = 0
        for i, p in enumerate(prices[1:]):
            if p > prices[i]:
                output += p - prices[i]
        return output
