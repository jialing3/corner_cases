class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        buy_price = max(prices) + 1
        profit = 0
        profit_lst = [0] * len(prices)
        for i in range(len(prices)):
            if i < len(prices) - 1 and prices[i] < prices[i + 1]:
                buy_price = min(buy_price, prices[i])
            elif i > 0 and prices[i] > prices[i - 1]:
                profit = max(profit, prices[i] - buy_price)
            profit_lst[i] += profit # max profit made up till the i-th position
        sell_price = min(prices) - 1
        profit = 0
        for i in reversed(range(len(prices))):
            if i > 0 and prices[i] > prices[i - 1]:
                sell_price = max(sell_price, prices[i])
            elif i < len(prices) - 1 and prices[i] < prices[i + 1]:
                profit = max(profit, sell_price - prices[i])
            profit_lst[i] += profit # max profit made from the i-th position
        return max(profit_lst)
