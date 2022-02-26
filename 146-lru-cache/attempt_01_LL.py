class LRUNode:

    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = LRUNode(None, None)
        self.tail = LRUNode(None, None, prev=self.head)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        # handle case of key miss
        if key not in self.cache:
            return -1
        # handle case of key hit
        res = self.cache[key][0]
        self.put(key, res)
        return res


    def put(self, key: int, value: int) -> None:
        # handle case where key exists in cache
        if key in self.cache:
            # remove node
            node = self.cache[key][1]
            node.next.prev = node.prev
            node.prev.next = node.next
        # handle case where key does not exist in cache
        else:
            # handle case where cache is at capacity
            if self.size == self.capacity:
                del self.cache[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            else:
                self.size += 1
        # insert new LRUNode and update cache
        new_node = LRUNode(key, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.cache[key] = [value, new_node]

    # def print_ll(self):
    #     curr = self.head
    #     s = ''
    #     while curr != None:
    #         s += (str(curr.key) + '->')
    #         curr = curr.next
    #     print(s[:-2])

    # def print_ll_rev(self):
    #     curr = self.tail
    #     s = ''
    #     while curr != None:
    #         s += (str(curr.key) + '->')
    #         curr = curr.prev
    #     print(s[:-2])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)