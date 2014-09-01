# The symmetry of P[i] around palindrome centers allow us to not recompute some P[i]'s.

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        def pad(s):
            s_padded = ['#'] * (len(s) * 2 + 1) # handle even and odd the same way
            for ind in range(len(s)):
                s_padded[ind * 2 + 1] = s[ind]
            return '^' + ''.join(s_padded) + '$'


        s = pad(s)
        center = 0 # center of palindrome
        right = 0 # right edge of palindrome
        P = [0] * len(s) # P[i] = the max offset length of palindrome around poisition i, 0 to be the shortest

        for i in range(1, len(s) - 1):
            i_mirror = 2 * center - i

            if right > i:
                P[i] = min(right - i, P[i_mirror])
            # otherwise no palindrome to the left, and so left at 0 before expansion below

            while s[i + 1 + P[i]] == s[i - 1 - P[i]]:
                P[i] += 1
            # expanding right, taking a total of O(N) steps for the entire loop

            if i + P[i] > right: # palindrome at i expand beyond right, need to define new center and right edge
                center = i
                right = i + P[i]

        max_length, center = max((p, i) for i, p in enumerate(P))
        max_palindrome = s[center - max_length : center + max_length + 1]
        return ''.join([x for x in max_palindrome if x != '#'])
