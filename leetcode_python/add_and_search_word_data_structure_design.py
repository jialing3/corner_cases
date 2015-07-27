class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.trie = {}

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        tmp = self.trie
        for letter in word:
            if letter not in tmp:
                tmp[letter] = {}
            tmp = tmp[letter]
        tmp['_end_'] = '_end_'
        return

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.search_in_trie(word, self.trie)


    def search_in_trie(self, word, trie):
        if word == '':
            return '_end_' in trie and trie['_end_'] == '_end_'
        elif word[0] == '.':
            return any([self.search_in_trie(word[1:], subtrie) for letter, subtrie in trie.items() if letter != '_end_'])
        else:
            return word[0] in trie and self.search_in_trie(word[1:], trie[word[0]])

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
