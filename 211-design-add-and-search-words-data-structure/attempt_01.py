class TrieNode:

    def __init__(self, word=None, is_word=False):
        self.word = word
        self.is_word = is_word
        self.nexts = {}


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        # build subtree for word being added
        curr = self.head
        for char in word:
            if char not in curr.nexts:
                curr.nexts[char] = TrieNode()
            curr = curr.nexts[char]
        # populate fields at the leaf of word's subtree
        curr.is_word = True
        curr.word = word

    def search(self, word: str) -> bool:
        curr = self.head

        def rec(node, idx):
            # handle base case
            if idx == len(word):
                if node.is_word:
                    return True
                else:
                    return False
            # handle recursive exploration
            if word[idx] == '.':
                for key in node.nexts:
                    if node.nexts[key] and rec(node.nexts[key], idx + 1):
                        return True
                return False
            else:
                if not node.nexts.get(word[idx], False):
                    return False
                return rec(node.nexts[word[idx]], idx + 1)

        return rec(self.head, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
