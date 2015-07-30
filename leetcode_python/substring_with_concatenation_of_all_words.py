class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        num_words = len(words)
        word_len = len(words[0])
        word_dict = {}
        for w in words:
            word_dict[w] = word_dict.get(w, 1) + 1

        output = []
        for i in range(len(s) + 1 - word_len * num_words):
            counter = {}
            j = 0
            while j < num_words:
                w = s[i + j * word_len:i + j * word_len + word_len]
                if w not in word_dict:
                    break
                else:
                    counter[w] = counter.get(w, 1) + 1
                if counter[w] > word_dict[w]:
                    break
                j += 1
            if j == num_words:
                output.append(i)
        return output
