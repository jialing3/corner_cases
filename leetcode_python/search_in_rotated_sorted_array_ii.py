# when there are duplicates, we can't be sure if the left half is ordered when A[left] == A[mid]
# in that case, we should left += 1
# running time went from O(lg n) to O(n) because that step in worst-case

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right: # left can equal right
            mid = (left + right) / 2
            if A[mid] == target:
                return True
            if A[left] < A[mid]: # left half is ordered
                if A[left] <= target < A[mid]:
                    right  = mid - 1
                else:
                    left = mid + 1
            elif A[mid] < A[left]: # right half is ordered
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False
