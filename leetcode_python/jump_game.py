class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        step = A[0]
        for i in range(1, len(A)):
            if step == 0:
                return False
            else:
                step = max(step - 1, A[i])
        return True
