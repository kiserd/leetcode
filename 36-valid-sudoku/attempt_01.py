class Solution:
    def isValidSudoku(self, board) -> bool:
        # create some helper variables for constant time lookup
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        sqs = [set() for _ in range(n)]
        # loop through cells, populate tracking sets, check for invalidation
        for row in range(n):
            for col in range(n):
                val = board[row][col]
                if board[row][col] != '.':
                    sq = (row // 3) * 3 + (col // 3)
                    # if val is already present in a group, board is invalid
                    if val in rows[row] or val in cols[col] or val in sqs[sq]:
                        return False
                    # update tracking sets for new val
                    rows[row].add(val)
                    cols[col].add(val)
                    sqs[sq].add(val)
        # all tests passed, indicate board is valid
        return True
