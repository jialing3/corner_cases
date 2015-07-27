class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        output = []
        table = {}
        for ind in range(len(s) - 9):
            if s[ind:ind + 10] not in table:
                table[s[ind:ind + 10]] = 1
            else:
                table[s[ind:ind + 10]] += 1
                if table[s[ind:ind + 10]] == 2: # only add once
                    output.append(s[ind:ind + 10])
        return output
