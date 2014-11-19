# saw this in an interview :-)
# BFS

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        output = []
        current_level = [[]]
        output.extend(current_level)
        cnt = 0
        while cnt <= len(S):
            next_level = []
            for subset in current_level:
                remaining = S if not subset else filter(lambda x: x > subset[-1], S)
                next_level.extend([subset + [x] for x in remaining]) # TypeError: can only concatenate list (not "int") to list
            current_level = next_level
            output.extend(current_level)
            cnt += 1
        return output
        
