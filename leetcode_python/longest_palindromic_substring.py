class Solution:
    # @return a string
    def longestPalindrome(self, s):
        def get_common_prefix(a, b):
            if len(a) > len(b):
                a, b = b, a
            count = 0
            for ind in range(len(a)):
                if b[ind] == a[ind]:
                    count = ind + 1
                else:
                    break
            return ''.join(a[:count])


        def reverse_str(s):
            return ''.join(reversed(s))


        if s == '':
            return s
        if list(reversed(s)) == list(s):
            return s
        if len(set(s)) == 1:
            return s


        #s_padded = ['#'] * (len(s) * 2 + 1) # handle even and odd the same way
        #for ind in range(len(s)):
        #    s_padded[ind * 2 + 1] = s[ind]


        #max_length = 0
        #max_string = ''
        #for center_ind in range(len(s_padded)):
        #    common_prefix = get_common_prefix(s_padded[(center_ind + 1):], reverse_str(s_padded[:center_ind]))
        #    if len(common_prefix) > max_length:
        #        max_length = len(common_prefix)
        #        max_string = reverse_str(common_prefix) + s_padded[center_ind] + common_prefix


        # return ''.join([x for x in max_string if x != '#'])

        max_length = 0
        max_string = ''
        for center_ind in range(len(s)):
            common_prefix_odd = get_common_prefix(s[(center_ind + 1):], reverse_str(s[:center_ind]))
            common_prefix_even = get_common_prefix(s[(center_ind):], reverse_str(s[:center_ind]))
            if len(common_prefix_odd) * 2 + 1 > len(common_prefix_even) * 2:
                common_prefix = reverse_str(common_prefix_odd) + s[center_ind] + common_prefix_odd
            else:
                common_prefix = reverse_str(common_prefix_even) + common_prefix_even
            if len(common_prefix) > max_length:
                max_length = len(common_prefix)
                max_string = common_prefix


        return max_string
