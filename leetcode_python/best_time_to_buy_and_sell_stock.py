class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for current_price in prices[1:]:
            current_profit = current_price - min_price
            max_profit = max(max_profit, current_profit)
            min_price = min(min_price, current_price)
        return max_profit
