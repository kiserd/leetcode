class TrieNode:

    def __init__(self, is_word=False):
        self.is_word = is_word
        self.nexts = [None] * 26


class Trie:

    def __init__(self, dictionary):
        self.head = TrieNode()
        # build trie structure with words in dictionary
        for word in dictionary:
            curr = self.head
            for char in word:
                # handle case of new "branch"
                if not curr.nexts[ord(char) % ord('a')]:
                    curr.nexts[ord(char) % ord('a')] = TrieNode()
                curr = curr.nexts[ord(char) % ord('a')]
            # set is_word flag for leaf
            curr.is_word = True


class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        # initialize our try object
        t = Trie(dictionary)
        # parse sentence into array of words
        arr = sentence.split(' ')
        # process each word in sentence
        for idx, word in enumerate(arr):
            i = 0
            curr = t.head
            active = True
            while i < len(word) and active:
                if curr.is_word:
                    arr[idx] = word[:i]
                    active = False
                elif not curr.nexts[ord(word[i]) % ord('a')]:
                    active = False
                else:
                    curr = curr.nexts[ord(word[i]) % ord('a')]
                i += 1
        res = ''
        for word in arr:
            res += word
            res += ' '
        return res[:-1]
