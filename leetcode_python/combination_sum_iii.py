# tree-level search


class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        paths = [[]]
        candidates = range(1, 10)
        target = n
        for i in range(1, k + 1):
            new_paths = []
            for path in paths:
                sum_path = sum(path)
                max_path = max(path) if path else 0
                for num in candidates:
                    if num not in path and num > max_path:
                        if (i == k and num == target - sum_path) or (i < k and num < target - sum_path):
                            new_paths.append(path + [num])
            if new_paths == []:
                return []
            paths = new_paths
        return paths
