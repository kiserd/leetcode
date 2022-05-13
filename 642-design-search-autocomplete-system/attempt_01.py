import heapq


class TrieNode:

    def __init__(self, is_sentence=False, times=0):
        self.is_sentence = is_sentence
        self.sentence = None
        self.times = 0
        self.nexts = {}


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # build tree object
        self.current_search = ''
        self.t = TrieNode()
        for idx, sentence in enumerate(sentences):
            self.add_sentence(sentence, times[idx], True)

    def add_sentence(self, sentence, times=1, multi_add=False):
        curr = self.t
        for char in sentence:
            if not curr.nexts.get(char, False):
                curr.nexts[char] = TrieNode()
            curr = curr.nexts[char]
        # add information to leaf node representing sentence
        curr.is_sentence = True
        curr.sentence = sentence
        if multi_add:
            curr.times = times
        else:
            curr.times += 1

    def input(self, c: str) -> List[str]:
        # handle case of trailing special char
        if c[-1] == '#':
            self.add_sentence(self.current_search)
            self.current_search = ''
            return []
        # add character to current_search property
        self.current_search += c
        # get root of prefix subtree
        root = self.t
        for char in self.current_search:
            if not root.nexts.get(char, False):
                return []
            root = root.nexts.get(char)
        # get all viable sentences via DFS (stack)
        s = [root]
        h = []
        while s:
            curr = s.pop()
            if curr.is_sentence:
                heapq.heappush(h, (-1 * curr.times, curr.sentence))
            for key in curr.nexts:
                s.append(curr.nexts[key])
        # get three "hottest" hits from heap and return to user
        res = []
        count = 0
        while h and count < 3:
            res.append(heapq.heappop(h)[1])
            count += 1
        return res

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
