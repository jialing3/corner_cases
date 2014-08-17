class Solution:
    # @return a string
    int_to_roman = {}
    int_to_roman[1000] = 'M'
    int_to_roman[500] = 'D'
    int_to_roman[100] = 'C'
    int_to_roman[50] = 'L'
    int_to_roman[10] = 'X'
    int_to_roman[5] = 'V'
    int_to_roman[1] = 'I'
    int_to_roman[0] = '' # boundary case

    def getKeyValueOfBiggestKey(self, number):
        for key, value in sorted(self.int_to_roman.items(), reverse=True):
            if key <= number:
                return key, value
        return None

    def getFourOrNine(self, number):
        ordered_keys = sorted(self.int_to_roman.keys(), reverse=True)
        str_to_return = ''
        counter = 0
        for ind, key in enumerate(ordered_keys):
            if ind == 0:
                continue
            else:
                if key < number:
                    number = 10 ** (len(str(number)) - 1)
                    str_to_return = self.int_to_roman[ordered_keys[ind - 1]] + str_to_return
                    counter += 1
                    if counter == 2:
                        return str_to_return
        return None

    def intToRoman(self, num):
        roman = ''
        for i in range(1, 5):
            current_digit = ''
            i = 10 ** i
            current = num % i
            first_digit = current / (i / 10)
            if first_digit == 0:
                pass
            elif first_digit in set([1, 2, 3, 5, 6, 7, 8]):
                while current >= i / 10:
                    to_subtract, digit_to_add = self.getKeyValueOfBiggestKey(current)
                    current -= to_subtract
                    current_digit = current_digit + digit_to_add
                roman = current_digit + roman
            else: # 4, 9
                current_digit = self.getFourOrNine(current)
                roman = current_digit + roman
        return roman
                
