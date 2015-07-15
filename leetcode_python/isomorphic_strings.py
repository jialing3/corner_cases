# not two letters can map to the same letter

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            s_letter, t_letter = s[i], t[i]
            if s_letter not in s_to_t:
                s_to_t[s_letter] = t_letter
            elif s_to_t[s_letter] != t_letter:
                return False
            if t_letter not in t_to_s:
                t_to_s[t_letter] = s_letter
            elif t_to_s[t_letter] != s_letter:
                return False
        return True
