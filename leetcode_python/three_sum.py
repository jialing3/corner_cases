class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):

        def merge_sort(lst):
            if len(lst) <= 1: #key base case
                return lst
            n = len(lst) / 2
            left = merge_sort(lst[:n])
            right = merge_sort(lst[n:])
            return merge(left, right)

        def merge(A, B):
            i, j = 0, 0
            C = []
            while (i < len(A) and j < len(B)):
                if A[i] < B[j]:
                    C.append(A[i])
                    i += 1
                else:
                    C.append(B[j])
                    j += 1
            if i < len(A):
                C.extend(A[i:])
            if j < len(B):
                C.extend(B[j:])
            return C

        num = merge_sort(num)

        solutions = set()
        for i, a in enumerate(num):
            j, k = 0, len(num) - 1
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue
                if num[j] + num[k] + a == 0:
                    solutions.add(tuple(sorted((a, num[j], num[k]))))
                    j += 1
                    k -= 1
                elif num[j] + num[k] + a > 0:
                    k -= 1
                else:
                    j += 1

        return [list(row) for row in solutions]
