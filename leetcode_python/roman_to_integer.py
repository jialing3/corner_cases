class Solution:
    # @return an integer

    roman_to_num = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

    def romanToInt(self, s):
        total = 0
        prior = self.roman_to_num[s[0]]
        for letter in s[1:]:
            current = self.roman_to_num[letter]
            if prior < current:
                prior = current - prior
            else:
                total += prior
                prior = current
        total += prior
        return total


        
