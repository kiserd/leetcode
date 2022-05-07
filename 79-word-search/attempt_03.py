class Solution:
    def exist(self, board, word: str) -> bool:
        # define set of cells to be visited
        m = len(board)
        n = len(board[0])
        # define recursive helper function
        def search(idx, row, col):
            # handle base case
            if idx == len(word) - 1:
                return True
            # handle recursive exploration
            for new_row, new_col in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                if new_row > -1 and new_row < m and new_col > -1 and new_col < n:
                    temp = board[row][col]
                    board[row][col] = None
                    if board[new_row][new_col] == word[idx + 1]:
                        if search(idx + 1, new_row, new_col):
                            return True
                    board[row][col] = temp
            return False
        # run backtracking algorithm on all potential "starts"
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and search(0, i, j):
                    return True
        return False
