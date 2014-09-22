class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.store = {} # {key: [value, times_called_by_get]}
        self.capacity = capacity
        self.key_order = {}


    # @return an integer
    def get(self, key):
        if key in self.store:
            self.store[key][1] += 1
            if len(self.key_order) > 0:
                new_cnt = self.store[key][1]
                if new_cnt not in self.key_order:
                    self.key_order[new_cnt] = []
                self.key_order[new_cnt].append(key)
                self.key_order[new_cnt - 1].remove(key)
            return self.store[key][0]
        else:
            return -1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.store:
            self.store[key][0] = value
            return
        if len(self.store) >= self.capacity:
            if len(self.key_order) == 0:
                for k, v in self.store.items():
                    if v[1] not in self.key_order:
                        self.key_store[v[1]] = []
                    self.key_store[v[1]].append(k)
            cnt = 0
            while cnt not in self.key_order or len(self.key_order[cnt]) == 0:
                cnt += 1
            key_to_discard = self.key_order[cnt].pop()
            self.store.pop(key_to_discard)
        self.store[key] = [value, 0]
        if 0 not in self.key_order:
            self.key_order[0] = []
        self.key_order[0].append(key)
        return
