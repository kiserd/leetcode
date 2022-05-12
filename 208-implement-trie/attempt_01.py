class TrieNode:

    def __init__(self, word=None):
        self.word = word
        self.nexts = [None] * 26


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            next_node = curr.nexts[ord(char) % ord('a')]
            if not next_node:
                curr.nexts[ord(char) % ord('a')] = TrieNode()
            curr = curr.nexts[ord(char) % ord('a')]
        curr.word = word

    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            next_node = curr.nexts[ord(char) % ord('a')]
            if not next_node:
                return False
            curr = curr.nexts[ord(char) % ord('a')]
        if curr.word == word:
            return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            next_node = curr.nexts[ord(char) % ord('a')]
            if not next_node:
                return False
            curr = curr.nexts[ord(char) % ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
