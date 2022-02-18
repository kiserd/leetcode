# essentially duplicated my prior code without looking at it
class Solution:
    def exist(self, board, word: str):
        # define recursive function
        def search(row, col, i):
            # handle unsuccessful base case
            if board[row][col] != word[i]:
                return False
            # handle successful base case
            if i == len(word) - 1:
                return True
            # handle recursive exploration
            temp = board[row][col]
            board[row][col] = None
            adjs = [
                [max(0, row - 1), col],
                [min(len(board) - 1, row + 1), col],
                [row, max(0, col - 1)],
                [row, min(len(board[0]) - 1, col + 1)]
            ]
            for x, y in adjs:
                if search(x, y, i + 1):
                    return True
            board[row][col] = temp
            return False
        
        # find potential starting cells
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, 0): return True
        return False