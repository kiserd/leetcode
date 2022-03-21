class Trie:
    def __init__(self, strs):
        self.head = self.Tnode(None)
        # build trie

class TNode:
    def __init__(self, elt: str, complete=False):
        self.complete = complete
        self.elt = elt
        self.next = {}
        

class Solution:
    def suggestedProducts(self, products, searchWord: str):
        pass