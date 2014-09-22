# An ordered dictionary remembers its insertion order.
# When new keys are added, the keys are appended to the end.

# Another key to solving this problem is to correctly understand
# "least recently used". To use, is to get and to set. Least recent
# has to do with freshness of the operations, not count.

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity


    # @return an integer
    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
        else:
            value = -1
        return value


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
        if len(self.cache) == self.capacity:
            for key_to_toss in self.cache.iterkeys():
                del self.cache[key_to_toss]
                break
        self.cache[key] = value
