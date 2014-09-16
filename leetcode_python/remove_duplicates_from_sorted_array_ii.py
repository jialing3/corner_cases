class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 3:
            return len(A)
        number_of_duplicates = 0
        current = A[0]
        cnt = 1
        for ind in range(1, len(A)):
            if A[ind] == current:
                cnt += 1
            else:
                cnt = 1
            if cnt > 2:
                number_of_duplicates += 1
            current = A[ind]
            A[ind - number_of_duplicates] = A[ind]
        return len(A) - number_of_duplicates
