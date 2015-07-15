class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        paths = [[]]
        while True:
            new_paths = []
            for path in paths:
                sum_path = sum(path)
                if sum_path == target:
                    new_paths.append(path)
                    continue
                max_path = max(path) if path else 0
                candidates_copy = candidates[:]
                for _ in path: #
                    candidates_copy.remove(_)
                candidates_copy = list(set(candidates_copy)) #
                for num in candidates_copy:
                    if num >= max_path and num <= target - sum_path:
                        new_paths.append(path + [num])
            if new_paths == [[]]:
                return []
            elif paths == new_paths:
                break
            else:
                paths = new_paths
        return paths
