# DP
# a table keeps a count m, indicating s3[:m] can match to s1[:i] and s2[:j]
# m = j for all i == 0
# m = i for all j == 0


class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False


        if len(s1) > len(s2):
            s1, s2 = s2, s1

        current_row = [0 for _ in range(len(s2) + 1)]

        for i in range(0, len(s1) + 1):
            last_row = current_row[:]
            current_row = [0 for _ in range(len(s2) + 1)]
            for j in range(0, len(s2) + 1):
                if (i > 0 and s3[i + j - 1] == s1[i - 1] and last_row[j] == i - 1 + j) or (j > 0 and s3[i + j - 1] == s2[j - 1] and current_row[j - 1] == i + j - 1): # key to have i > 0 and j > 0
                    current_row[j] = i + j

        return current_row[len(s2)] == len(s1) + len(s2)         
