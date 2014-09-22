class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.store = {} # {key: [value, times_called_by_get]}
        self.capacity = capacity


    # @return an integer
    def get(self, key):
        if key in self.store:
            self.store[key][1] += 1
            return self.store[key][0]
        else:
            return -1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if len(self.store) >= self.capacity:
            # the following operation is too costly, when capacity is reached
            key_to_discard = min(self.store.items(), key=lambda x: x[1][1])[0] # return the first occurrence if multiple entries exist
            self.store.pop(key_to_discard)
        self.store[key] = [value, 0]
        return None
