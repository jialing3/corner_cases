conversion = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_letter_order = dict((letter, ind) for ind, letter in enumerate('IVXLCDM'))
minimal_num_of_letter_needed_for_each_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 2,
                                               '5': 1, '6': 2, '7': 3, '8': 4, '9': 2}

def check_order(long_form):
    for ind1, char1 in enumerate(long_form[:-1]):
        char2 = long_form[ind1 + 1]
        if roman_letter_order[char1] < roman_letter_order[char2]:
            if char1 + char2 not in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
                return False
    return True

def parse(long_form):
    __sum__ = 0
    for ind1, char1 in enumerate(long_form[:-1]):
        char2 = long_form[ind1 + 1]
        if roman_letter_order[char1] >= roman_letter_order[char2]:
            __sum__ += conversion[char1]
        else:
            if char1 + char2 in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
                __sum__ -= conversion[char1]
    __sum__ += conversion[long_form[-1]]
    return __sum__

def get_long_form_lst():
    lst = []
    with open('p089_roman.txt') as f:
        for row in f.readlines():
            lst.append(row.strip())
    return lst

long_form_lst = get_long_form_lst()
total_length_saved = 0
patterns_to_replace_0 = ['VIIII', 'LXXXX', 'DCCCC']
patterns_to_replace_1 = ['IIII', 'XXXX', 'CCCC']
for long_form in long_form_lst:
    if check_order(long_form) is True:
        short_form_length = 0
        parsed = str(parse(long_form))
        for ind, digit in enumerate(reversed(parsed)):
            if ind == 3: # no short form for the digit of M
                short_form_length += int(digit)
                #print(int(digit))
            else:
                short_form_length += minimal_num_of_letter_needed_for_each_digit[digit]
                #print(minimal_num_of_letter_needed_for_each_digit[digit])
        length_saved = len(long_form) - short_form_length
        total_length_saved += length_saved

        length_saved_2 = 0
        for pattern0, pattern1 in zip(patterns_to_replace_0, patterns_to_replace_1):
            if pattern0 in long_form:
                length_saved_2 += 3
            elif pattern1 in long_form:
                length_saved_2 += 2

        if length_saved != length_saved_2:
            print(long_form, parse(long_form), length_saved, length_saved_2)
    else:
        print(long_form)


print(total_length_saved)
