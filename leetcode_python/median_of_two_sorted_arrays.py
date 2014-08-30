class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        # k is 1 based
        def get_kth(A, B, k):
            if len(A) > len(B):
                A, B = B, A # make sure A is shorter than B is
            if len(A) == 0:
                return B[k - 1]
            if k == 1:
                return min(A[0], B[0])
            part_a = min(k / 2, len(A))
            part_b = k - part_a
            return get_kth(A[part_a:], B, k - part_a) if A[part_a - 1] <= B[part_b - 1] else get_kth(A, B[part_b:], k - part_b)
            # keep tossing away numbers that are definitely smaller than the kth number

        if (len(A) + len(B)) % 2 == 1:
            return get_kth(A, B, (len(A) + len(B)) / 2 + 1)
        else:
            return .5 * (get_kth(A, B, (len(A) + len(B)) / 2 + 1) + get_kth(A, B, (len(A) + len(B)) / 2))
