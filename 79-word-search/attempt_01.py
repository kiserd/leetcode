class Solution:
    def exist(self, board, word: str) -> bool:
        # define a couple helper variables
        m = len(board)
        n = len(board[0])
        # define recursive function
        def helper(s, row, col):
            # handle successful base case
            if len(s) == 0:
                return True
            # handle recursive exploration
            temp = board[row][col]
            board[row][col] = None
            adjs = {
                (max(0, row - 1), col),
                (min(m - 1, row + 1), col),
                (row, max(0, col - 1)),
                (row, min(n - 1, col + 1))
            }
            for i, j in adjs:
                if board[i][j] == s[0]:
                    if helper(s[1:], i, j):
                        return True
            # all adjacent cells tested, indicate failure
            board[row][col] = temp
            return False
        # run helper on each eligible starting point
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(word[1:], i, j):
                        return True
        return False
