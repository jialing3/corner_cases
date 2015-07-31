# double poitner

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        t_counts = {}
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1

        i, j = 0, 0
        min_window = None
        s_counts = {}
        while i <= j < len(s):
            c = s[j]
            if c in t_counts:
                s_counts[c] = s_counts.get(c, 0) + 1
            if len(s_counts) == len(t_counts) and all([s_counts[k] >= t_counts[k] for k in t_counts.keys()]): # met criteria
                while i <= j:
                    c_to_remove = s[i]
                    if c_to_remove not in s_counts:
                        i += 1
                    elif s_counts[c_to_remove] > t_counts[c_to_remove]:
                        i += 1 # shift left
                        s_counts[c_to_remove] -= 1
                    else:
                        break
                if (not min_window) or (min_window[1] - min_window[0] > j - i):
                    min_window = (i, j) # inclusive
                i += 1 # shift left
                if c_to_remove in s_counts:
                    s_counts[c_to_remove] -= 1 # key
            j += 1 # shift right

        if min_window is not None:
            return s[min_window[0]:min_window[1] + 1]
        else:
            return ''
            
