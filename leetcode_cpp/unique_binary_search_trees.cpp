class Solution {
public:
    int numTrees(int n) {
        if (n <= 1) {
            return 1;
        }
        int sum = 0, sum_left, sum_right;
        for (int i = 1; i <= n; ++i) {
            sum_left = numTrees(i - 1);
            sum_right = numTrees(n - i);
            sum += sum_left * sum_right;
        }
        return sum;
    }
};
