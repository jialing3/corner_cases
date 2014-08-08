class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        cnt = 0
        for i in range(len(A)):
            if cnt > 0:
                A[i - cnt] = A[i]
            if A[i] == elem:
                cnt += 1

        return len(A) - cnt
