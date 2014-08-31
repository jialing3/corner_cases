# greedy algorithm
# space O(min(m, n)), with m = len(word1), n = len(word2)
# time O(max(m, n))

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        # need a matrix to store the distance
        # M[i][j] = distance between word1{:i} and word2[:j]
        # but the iteration only requires us to keep track of the previous row
        current_row = range(len(word1) + 1)
        for i in range(1, len(word2) + 1):
            last_row = current_row[:] # copy
            current_row[0] = i
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    current_row[j] = last_row[j - 1]
                else:
                    current_row[j] = 1 + min(last_row[j - 1], last_row[j], current_row[j - 1])
        return current_row[-1]
