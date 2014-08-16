class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) <= 1:
            return A
        zero = 0
        two = len(A) - 1
        i = 0
        while i <= two:
            if A[i] == 2:
                A[i], A[two] = A[two], A[i]
                two -= 1
            if A[i] == 0:
                A[i], A[zero] = A[zero], A[i]
                zero += 1
                i += 1
                continue
            if A[i] == 1:
                i += 1
        
