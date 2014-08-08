class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        number_of_duplicates = 0
        for ind in range(1, n):
            if A[ind] == A[ind - 1]:
                number_of_duplicates += 1
            elif number_of_duplicates > 0:
                A[ind - number_of_duplicates] = A[ind]
        return n - number_of_duplicates
