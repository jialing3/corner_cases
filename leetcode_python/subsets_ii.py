class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        current_level = [S]
        output = current_level
        while current_level != [[]]:
            next_level = set()
            for subset in current_level:
                for i in range(len(subset)):
                    next_level.add(tuple(subset[:i] + subset[i + 1:]))
            current_level = [list(x) for x in next_level]
            output.extend(current_level)
        return output

        
