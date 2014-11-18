class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if not needle: # weird edge-case
            return 0
        position = 0
        len_haystack = len(haystack)
        len_needle = len(needle) # needle can be composed of multiple characters
        while position + len_needle <= len_haystack:
            if haystack[position : position + len_needle] == needle:
                return position
            position += 1
        return -1
        
