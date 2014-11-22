class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest_substring = []
        current_substring = []
        chars_in_substring = set()
        for c in s:
            if c not in chars_in_substring:
                chars_in_substring.add(c)
                current_substring.append(c)
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
            else: # c in chars_in_substring
                ind_c = current_substring.index(c)
                current_substring = current_substring[ind_c + 1:]
                current_substring.append(c)
                chars_in_substring = set(current_substring)
        return len(longest_substring)

        
