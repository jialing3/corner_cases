
with open('p098_words.txt') as f:
    words = f.read().strip().replace('"', '').split(',')

square_nums = [str(i ** 2) for i in range(1, 10 ** 7)]
num_by_length = {}
for num in square_nums:
    length = len(num)
    if length not in num_by_length:
        num_by_length[length] = []
    num_by_length[length].append(num)
square_nums = []

word2num_map = {}
word2largest_num = {}
for word in words:
    word_len = len(word)
    candidate_nums = num_by_length[word_len]
    for num in candidate_nums:
        letter2digit = {}
        digit2letter = {}
        is_mapping_good = True
        for letter, digit in zip(word, num):
            if letter not in letter2digit:
                letter2digit[letter] = digit
            else:
                if letter2digit[letter] == digit:
                    pass # inter-consistent
                else:
                    is_mapping_good = False
                    break # not inter-consistent
            if digit not in digit2letter:
                digit2letter[digit] = letter
            else:
                if digit2letter[digit] == letter:
                    pass # inter-consistent
                else:
                    is_mapping_good = False
                    break # not inter-consistent
        if is_mapping_good:
            #print(num)
            mapping = tuple(sorted(letter2digit.items()))
            if mapping not in word2num_map:
                word2num_map[mapping] = []
            word2num_map[mapping].append(word)
            word2largest_num[word] = max(word2largest_num.get(word, 0), int(num))

pairs = []
from itertools import combinations
for __map__ in word2num_map.keys():
    if len(word2num_map[__map__]) > 1:
        for word_0, word_1 in combinations(word2num_map[__map__], 2):
            if sorted(word_0) == sorted(word_1):
                pairs.append((__map__, word_0, word_1))


# there is ambiguity in the wording of the last bit of the question
print(pairs) # BROAD (('A', '6'), ('B', '1'), ('D', '9'), ('O', '7'), ('R', '8'))
