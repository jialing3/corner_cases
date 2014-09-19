#DFS

class Solution:

    def walk(self, path, remaining, paths):
        if not remaining: # base-case
            paths.append(path)
        else:
            for i in range(len(remaining)):
                self.walk(path + [remaining[i]], remaining[:i] + remaining[i + 1:], paths)
        return paths

    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        paths = []
        self.walk([], num, paths)
        return paths

        
