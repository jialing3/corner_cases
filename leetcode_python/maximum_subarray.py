class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_ending_here = max_so_far = A[0]
        for x in A[1:]:
            max_ending_here = max(max_ending_here + x, x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
