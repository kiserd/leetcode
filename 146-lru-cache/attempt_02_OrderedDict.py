from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # handle case of key miss
        if key not in self.cache:
            return -1
        # handle case of key hit
        res = self.cache[key]
        self.put(key, res)
        return res

    def put(self, key: int, value: int) -> None:
        # handle case where key is present in cache
        if key in self.cache:
            del self.cache[key]
        # handle case where key is NOT present in cache
        else:
            if self.size == self.cap:
                self.cache.popitem(last=False)
            else:
                self.size += 1
        # add new key value pair to cache
        self.cache[key] = value
