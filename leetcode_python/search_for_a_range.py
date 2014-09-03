class Solution:

    def get_start_pos(self, A, target):
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                if start == end:
                    return mid
                end = mid
            elif A[mid] < target:
                start = mid + 1
            else: # >
                end = mid - 1
        return -1


    def get_end_pos(self, A, target):
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end + 1) / 2
            if A[mid] == target:
                if start == end:
                    return mid
                start = mid
            elif A[mid] < target:
                start = mid + 1
            else: # >
                end = mid - 1
        return -1


    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return [self.get_start_pos(A, target), self.get_end_pos(A, target)]
