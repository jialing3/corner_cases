class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):

        num.sort()
        solutions = set()

        for i, a in enumerate(num):
            if i > 1 and num[i - 1] == num[i]:
                continue
            j, k = i + 1, len(num) - 1
            while j < k:
                total = num[j] + num[k] + a
                if total == 0:
                    solutions.add((a, num[j], num[k]))
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return [list(row) for row in solutions]

        '''
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
        '''
