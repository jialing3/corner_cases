class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        profit = 0
        
        smaller_than_future = (prices[0] < prices[1])
        buy_price = prices[0] if smaller_than_future else None

        for ind in range(1, len(prices) - 1):
            smaller_than_past = not smaller_than_future
            smaller_than_future = (prices[ind] < prices[ind + 1])
            if not smaller_than_past and not smaller_than_future:
                sell_price = prices[ind]
                profit += (sell_price - buy_price)
                buy_price = None
            elif smaller_than_past and smaller_than_future:
                buy_price = prices[ind]

        ind = len(prices) - 1
        smaller_than_past = not smaller_than_future
        if not smaller_than_past:
            sell_price = prices[ind]
            profit += (sell_price - buy_price)

        return profit
