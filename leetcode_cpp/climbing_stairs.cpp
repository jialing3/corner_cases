class Solution {
public:
    unordered_map <int, int> cached = {
        {0, 1},
        {1, 1}
    };

    int climbStairs(int n) {
        if (cached.count(n) == 0) {
            cached[n] = climbStairs(n - 1) + climbStairs(n - 2);
        }
        return cached[n];
    }
};
