class Solution {
public:
    int singleNumber(int A[], int n) {
        int ones = 0, twos = 0, not_threes;
        for (int i = 0; i < n; ++i) {
            twos |= ones & A[i];
            ones ^= A[i];
            not_threes = ~(ones & twos);
            ones &= not_threes;
            twos &= not_threes;
        }
        return ones;
    }
};
