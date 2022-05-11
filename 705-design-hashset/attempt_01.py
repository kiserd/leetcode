class MyHashSet:

    def __init__(self):
        self.buckets = [None] * 1000

    def add(self, key: int) -> None:
        hashed = self.hashify(key)
        if self.contains(key):
            return None
        if not self.buckets[hashed]:
            self.buckets[hashed] = [key]
        else:
            self.buckets[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = self.hashify(key)
        if self.buckets[hashed]:
            for idx in range(len(self.buckets[hashed])):
                if self.buckets[hashed][idx] == key:
                    self.buckets[hashed].pop(idx)
                    return None

    def contains(self, key: int) -> bool:
        hashed = self.hashify(key)
        if self.buckets[hashed]:
            for idx in range(len(self.buckets[hashed])):
                if self.buckets[hashed][idx] == key:
                    return True
        return False


    def hashify(self, key: int) -> int:
        return key % 1000

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
