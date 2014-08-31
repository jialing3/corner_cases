class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):

        def get_common_prefix(a, b):
            if len(a) > len(b):
                a, b = b, a
            common = []
            for ind, letter in enumerate(a):
                if letter == b[ind]:
                    common.append(letter)
                else:
                    break
            return ''.join(common)

        if len(strs) == 0:
            return ''
        common = strs[0]
        for new_str in strs[1:]:
            common = get_common_prefix(common, new_str)
        return common
