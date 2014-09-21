# linear solution

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        len_s = len(s)
        len_p = len(p)
        ind_p = 0
        ind_s = 0
        ind_s_at_star = 0
        ind_star = None
        while ind_s < len_s:
            if ind_p < len_p and (p[ind_p] == '?' or p[ind_p] == s[ind_s]): # match
                ind_s += 1
                ind_p += 1
            elif ind_p < len_p and p[ind_p] == '*': # no match, '*' in p, increment ind_p
                ind_star = ind_p
                ind_p +=1
                ind_s_at_star = ind_s
            elif ind_star is not None: # no match, increment ind_s
                ind_p = ind_star + 1
                ind_s_at_star += 1
                ind_s = ind_s_at_star
            else: # definitely mismatch
                return False
        while ind_p < len_p and p[ind_p] == '*': # s is over, increment ind_p till '*' is exhausted
            ind_p += 1
        return ind_p == len_p # return False if anything including '?' is left
