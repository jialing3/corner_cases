class Solution:
    def walk(self, path, remaining, paths):
        if len(remaining) == 0:
            paths.add(tuple(path))
        else:
            seen = set() # not adding redundant paths
            for i in range(len(remaining)):
                if remaining[i] not in seen:
                    seen.add(remaining[i])
                    self.walk(path + [remaining[i]], remaining[:i] + remaining[i + 1:], paths)


    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        paths = set()
        self.walk([], num, paths)
        return [list(path) for path in paths]
