class MyHashMap:

    def __init__(self):
        self.keymod = 2069
        self.buckets = [None] * self.keymod

    def put(self, key: int, value: int) -> None:
        if self.buckets[key % self.keymod]:
            for idx in range(len(self.buckets[key % self.keymod])):
                k, v = self.buckets[key % self.keymod][idx]
                if k == key:
                    self.buckets[key % self.keymod][idx] = (key, value)
                    return None
            self.buckets[key % self.keymod].append((key, value))
            return None
        self.buckets[key % self.keymod] = [(key, value)]

    def get(self, key: int) -> int:
        if self.buckets[key % self.keymod]:
            for k, v in self.buckets[key % self.keymod]:
                if k == key:
                    return v
        return -1

    def remove(self, key: int) -> None:
        if self.buckets[key % self.keymod]:
            for k, v in self.buckets[key % self.keymod]:
                if k == key:
                    self.buckets[key % self.keymod].remove((k, v))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
