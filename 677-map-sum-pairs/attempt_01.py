class TrieNode:

    def __init__(self, word=None, val=0):
        self.word = word
        self.val = val
        self.nexts = [None] * 26


class MapSum:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.head
        for char in key:
            if not curr.nexts[ord(char) % ord('a')]:
                curr.nexts[ord(char) % ord('a')] = TrieNode()
            curr = curr.nexts[ord(char) % ord('a')]
        curr.word = key
        curr.val = val

    def sum(self, prefix: str) -> int:
        # first get the head of our subtree
        curr = self.head
        for char in prefix:
            next_node = curr.nexts[ord(char) % ord('a')]
            if not curr.nexts[ord(char) % ord('a')]:
                return 0
            curr = next_node
        # sum up leaf vals via DFS
        res = 0
        s = [curr]
        while s:
            node = s.pop()
            res += node.val
            for elt in node.nexts:
                if elt:
                    s.append(elt)
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
