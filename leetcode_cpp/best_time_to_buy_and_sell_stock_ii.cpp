class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.size() <= 1) return 0;

        int profit = 0, buy_price, sell_price, i;
        bool smaller_than_future = (prices[0] < prices[1]), smaller_than_past;
        if (smaller_than_future) buy_price = prices[0];

        for (i = 1; i < prices.size() - 1; ++i) {
            smaller_than_past = !smaller_than_future;
            smaller_than_future = (prices[i] < prices[i + 1]);
            if (!smaller_than_past && !smaller_than_future) {
                sell_price = prices[i];
                profit += (sell_price - buy_price);
            }
            else if (smaller_than_past && smaller_than_future) {
                buy_price = prices[i];
            }
        }

        i = prices.size() - 1;
        smaller_than_past = !smaller_than_future;
        if (!smaller_than_past) {
            sell_price = prices[i];
            profit += (sell_price - buy_price);
        }

        return profit;
    }
};
