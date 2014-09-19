# DFS

class Solution:

    def is_distance_one(self, s1, s2):
        for i in range(len(s1)):
            if s1[:i] + s1[i + 1:] == s2[:i] + s2[i + 1:]:
                return True
        else:
            return False

    def walk(self, path, remaining, end, paths, min_len):
        if len(path) > min_len:
            return paths
        elif path[-1] == end:
            paths.append(path)
            min_len = min(min_len, len(path))
        else:
            for i in range(len(remaining)):
                if self.is_distance_one(path[-1], remaining[i]):
                    self.walk(path + [remaining[i]], remaining[:i] + remaining[i + 1:], end, paths, min_len)
        return paths

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dictionary): # dict is reserved and should not be used as parameter name
        dictionary = list(dictionary - set([end]) - set([start]))
        dictionary = [end] + dictionary # always check end first
        paths = self.walk([start], dictionary, end, [], len(dictionary))
        if not paths:
            return []
        min_len = min(len(path) for path in paths)
        return [path for path in paths if len(path) == min_len]
