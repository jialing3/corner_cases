# coin problem
# tree traversal
# tree-level search

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        paths = [[]]
        while not all([sum(path) == target for path in paths]):
            new_paths = []
            for path in paths:
                sum_path = sum(path)
                max_num = max(path) if path else 0
                if sum_path == target:
                    new_paths.append(path)
                    continue
                for num in candidates:
                    if num >= max_num and num <= target - sum_path:
                        new_paths.append(path + [num])
            if new_paths == []:
                return []
            paths = new_paths
        return paths
