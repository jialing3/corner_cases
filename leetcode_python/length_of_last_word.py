class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = ' ' + s + ' '   # padding makes sure there are switches if there is char
        # '   aaa   '         6, 3  => char2space - space2char
        # '   '               0, 0
        switch_char_to_space = 0
        switch_space_to_char = 0
        for i in range(1, len(s)):
            if s[i - 1] != ' ' and s[i] == ' ':
                switch_char_to_space = i
            elif s[i - 1] == ' ' and s[i] != ' ':
                switch_space_to_char = i
        return switch_char_to_space - switch_space_to_char
