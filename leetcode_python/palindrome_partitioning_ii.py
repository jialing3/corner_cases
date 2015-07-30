# store is_palindrome[i, j] as an indicator for whether s[i:j + 1] is a palindrome or not
# store cuts[j] for the number of min_cuts in s[:j + 1]

class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        is_palindrome = [[False for _ in range(len(s))] for _ in range(len(s))]
        cuts = list(range(len(s)))
        for j in range(len(s)):
            for i in reversed(range(j + 1)): # make sure that i + 1 is visited before i; j - 1 is visited before j & cuts[i] is determined before cuts[j]
                    if i == j or (s[i] == s[j] and (j - i == 1 or is_palindrome[i + 1][j - 1])):
                        is_palindrome[i][j] = True
                        if i == 0:
                            cuts[j] = 0
                        else:
                            cuts[j] = min(cuts[j], cuts[i - 1] + 1)
        return cuts[len(s) - 1]


            
