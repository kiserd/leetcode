class TrieNode:

    def __init__(self, word=None):
        self.word = word
        self.nexts = {}


class Solution:
    def findWords(self, board, words) -> List[str]:
        # build trie
        t = self.build_trie(words)

        # define recursive search function
        def rec(node, row, col):
            # temporarily clear char from board
            temp = board[row][col]
            board[row][col] = None
            # handle base case
            if not node.nexts:
                board[row][col] = temp
                if node.word:
                    res.add(node.word)
            # handle recursive exploration
            else:
                if node.word:
                    res.add(node.word)
                # define viable adjacent cells
                adjs = self.get_adjs(row, col, len(board), len(board[0]))
                # explore each adjacency
                for i, j in adjs:
                    if board[i][j] in node.nexts:
                        rec(node.nexts[board[i][j]], i, j)
                # restore current cell and return hits
                board[row][col] = temp
                return res

        # loop through board, kicking off recursive function
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in t.nexts:
                    rec(t.nexts[board[i][j]], i, j)
        return res

    def build_trie(self, words):
        res = TrieNode()
        for word in words:
            curr = res
            for char in word:
                if char not in curr.nexts:
                    curr.nexts[char] = TrieNode()
                curr = curr.nexts[char]
            curr.word = word
        return res

    def get_adjs(self, row, col, m, n):
        up = (max(0, row - 1), col)
        down = (min(m - 1, row + 1), col)
        left = (row, max(0, col - 1))
        right = (row, min(n - 1, col + 1))
        return set([up, down, left, right]) - set((row, col))
