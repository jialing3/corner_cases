class Trie:
    '''
    use Trie to store word counts
    '''
    def __init__(self):
        self.trie = {}


    def put(self, word):
        tmp_trie = self.trie
        for letter in word:
            if letter not in tmp_trie:
                tmp_trie[letter] = {}
            tmp_trie = tmp_trie[letter]
        tmp_trie['cnt'] = tmp_trie.get('cnt', 0) + 1


    def get(self, word):
        tmp_trie = self.trie
        for letter in word:
            if letter not in tmp_trie:
                return 0
            tmp_trie = tmp_trie[letter]
        return tmp_trie.get('cnt', 0)


    def get_top_10_words(self):
        # ...
        return


if __name__ == '__main__':
    wc = Trie()
    for word in 'I heart Python'.split():
        wc.put(word)

    for word in 'Python rocks'.split():
        wc.put(word)

    text = 'Now that you have your high-level design, start thinking about what bottlenecks it has. Perhaps your system needs a load balancer and many machines behind it to handle the user requests. Or maybe the data is so huge that you need to distribute your database on multiple machines. What are some of the downsides that occur from doing that? Is the database too slow and does it need some in-memory caching?'
    for word in text.split():
        wc.put(word)

    print(wc.get_top_10_words())
