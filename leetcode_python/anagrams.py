class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        str_dict = {}
        for str in strs:
            str_key = ''.join(sorted(list(str)))
            if str_key not in str_dict:
                str_dict[str_key] = []
            str_dict[str_key].append(str)

        solutions = []
        for anagrams in str_dict.values():
            if len(anagrams) > 1:
                solutions.extend(anagrams)

        return solutions
