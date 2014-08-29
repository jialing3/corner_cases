class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):

        def add_one(i, digits):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                if i == 0: # don't forget the leading zero
                    digits = [0] + digits
                    i += 1
                digits[i] = 0
                return add_one(i - 1, digits)

        return add_one(len(digits) - 1, digits)

        
