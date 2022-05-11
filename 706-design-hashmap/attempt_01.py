# attempt using LL manifests in TLE for Python
# see attempt 2

class ListNode:

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.keymod = 2069
        self.buckets = [None] * self.keymod

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[key % self.keymod]
        if self.buckets[key % self.keymod]:
            curr = self.buckets[key % self.keymod]
            while True:
                if curr.key == key:
                    curr.value = value
                    return None
                if not curr.next or curr.next.key > key:
                    curr.next = ListNode(key, value, curr.next)
                    return None
                else:
                    curr = curr.next
        else:
            self.buckets[key % self.keymod] = ListNode(key, value)

    def get(self, key: int) -> int:
        bucket = self.buckets[key % self.keymod]
        if bucket:
            curr = bucket
            while True:
                if curr.key == key:
                    return curr.value
                if not curr.next or curr.next.key > key:
                    return -1
                else:
                    curr == curr.next
        else:
            return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.keymod]
        if bucket:
            prev = bucket
            curr = prev.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return None
                if not curr.next or curr.next.key > key:
                    return None
                else:
                    prev = curr
                    curr == curr.next
            # branch reached if prev was only node
            if prev.key == key:
                self.buckets[key % self.keymod] = None
                return None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
