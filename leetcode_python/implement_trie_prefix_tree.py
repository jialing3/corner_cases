class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.trie = {}


class Trie:

    def __init__(self):
        #self.root = TrieNode()
        self.trie = {}

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        tmp_trie = self.trie
        for letter in word:
            if letter not in tmp_trie:
                tmp_trie[letter] = {}
            tmp_trie = tmp_trie[letter]
        tmp_trie['_end_'] = '_end_'


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        tmp_trie = self.trie
        for letter in word:
            if letter not in tmp_trie:
                return False
            else:
                tmp_trie = tmp_trie[letter]
        return '_end_' in tmp_trie


    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        tmp_trie = self.trie
        for letter in prefix:
            if letter not in tmp_trie:
                return False
            else:
                tmp_trie = tmp_trie[letter]
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
