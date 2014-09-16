class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        A = [None] * n + A[:m]
        i, j = n, 0
        cnt = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                A[cnt] = A[i]
                i += 1
            else:
                A[cnt] = B[j]
                j += 1
            cnt += 1
        if j < len(B):
            A[m + j:] = B[j:]
        return A
