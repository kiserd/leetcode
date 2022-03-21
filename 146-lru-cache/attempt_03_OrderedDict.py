from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        # handle case of key NOT existing in cache
        if key not in self.cache:
            return -1
        # handle case of key existing in cache
        res = self.cache[key]
        self.put(key, res)
        return res
        

    def put(self, key: int, value: int) -> None:
        # handle case of cache containing key
        if key in self.cache:
            del self.cache[key]
        # handle case cache NOT containing key
        else:
            # handle case where cache size has not reached capacity
            if self.size < self.capacity:
                self.size += 1
            # handle case where cache is already at capacity
            else:
                self.cache.popitem(last=False)
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)