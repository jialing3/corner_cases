class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        step = A[0]
        for i in range(1, len(A)):
            if step > 0 :
                step -= 1
                step = max(step, A[i])
            else:
                return False
        return True
