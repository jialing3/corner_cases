class Solution {
public:
    int maxSubArray(int A[], int n) {
        int max_ending_here = A[0], max_so_far = A[0];
        for (int i = 1; i < n; ++i) {
            max_ending_here = max(max_ending_here + A[i], A[i]);
            max_so_far = max(max_so_far, max_ending_here);
        }
        return max_so_far;
    }
};
