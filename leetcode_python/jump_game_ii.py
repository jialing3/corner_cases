class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        steps = [None] * len(A)
        steps[0] = 0
        for i in range(len(A)):
            if i > 0 and A[i - 1] >= A[i] + 1: # reach of the current position is smaller than the previous position
                continue
            if A[i] == 0: # current position doesn't reach anywhere
                continue
            for j in range(1, min(A[i] + 1, len(A) - i)):
                if steps[i + j] is None:
                    steps[i + j] = steps[i] + 1
        return steps[-1]
        
