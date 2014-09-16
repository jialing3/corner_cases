class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        number = A[0]
        for current in A[1:]:
            number ^= current
        return number
