# BFS

class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        current_level = [list(s)] if s else [['']]
        output = []

        while current_level:
            next_level = []
            for uncombined in current_level:
                output.append(uncombined)
                combinable, combined = self.combine(uncombined)
                if combinable:
                    next_level.extend(combined)
            next_level = [_ for _ in next_level if _ not in output] # could speed out
            next_level = [list(y) for y in set(tuple(x) for x in next_level)]
            current_level = next_level
        return output

    def combine(self, s):
        combinable = False
        combined = []
        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i]:
                combinable = True
                combined.append(s[:i - 1] + [s[i - 1] + s[i]] + s[i + 1:])
            #if s[i] == s[i + 1]:
            #    combinable = True
            #    combined.append(s[:i] + [s[i] + s[i + 1]] + s[i + 2:])
            if s[i - 1] == s[i + 1]:
                combinable = True
                combined.append(s[:i - 1] + [s[i - 1] + s[i] + s[i + 1]] + s[i + 2:])
        if len(s) >= 2 and s[-2] == s[-1]:
            combinable = True
            combined.append(s[:-2] + [s[-2] + s[-1]])
        return combinable, combined
                
