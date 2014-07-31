class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        def binary_search(A, target):
            mid = len(A) / 2
            if A[mid] == target:
                return mid
            elif len(A) == 1:
                return 1 if A[mid] < target else 0
            elif A[mid] > target:
                return binary_search(A[:mid], target)
            else:
                return mid + binary_search(A[mid:], target)

        return binary_search(A, target)
