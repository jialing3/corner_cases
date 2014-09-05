# corner case, one word in any line other than the last line.


class Solution:
    def get_spaces(self, number_of_spaces, number_of_words):
        if number_of_words == 1:
            return [' ' * number_of_spaces]
        extra_spaces = number_of_spaces % (number_of_words - 1)
        common_spaces = number_of_spaces / (number_of_words - 1)
        return [' ' * (common_spaces + 1)] * extra_spaces + [' ' * common_spaces] * (number_of_words - 1 - extra_spaces)


    def merge(self, current_line, spaces):
        if len(current_line) == 0:
            return ['']
        if len(current_line) == 1:
            return current_line[0] + spaces[0]
        return ''.join([current_line[ind] + spaces[ind] for ind in range(len(spaces))]) + current_line[-1]


    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if L == 0:
            return ['']
        if words == ['']:
            return [' ' * L]
        answer = []
        i = 0
        while i < len(words):
            current_line = []
            length_left_in_current_line = L
            while i < len(words) and length_left_in_current_line >= len(words[i]):
                word = words[i]
                current_line.append(word)
                length_left_in_current_line -= len(word) + 1
                i += 1
            number_of_spaces = L - sum(len(x) for x in current_line)
            number_of_words = len(current_line)
            spaces = self.get_spaces(number_of_spaces, number_of_words)
            answer.append(self.merge(current_line, spaces))
        last_line = answer.pop()
        words_in_last_line = last_line.split()
        if len(words_in_last_line) > 1:
            last_line = ' '.join(words_in_last_line)
        last_line = last_line + ' ' * (L - len(last_line))
        answer.append(last_line)
        return answer
