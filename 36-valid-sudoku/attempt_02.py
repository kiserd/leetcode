class Solution:
    def isValidSudoku(self, board) -> bool:
        # create helper sets representing various groupings
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        sqs = [set() for _ in range(len(board))]
        # iterate through cells of board
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    val = board[i][j]
                    sq = (i // 3) * 3 + (j // 3)
                    if val in rows[i]:
                        return False
                    if val in cols[j]:
                        return False
                    if val in sqs[sq]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    sqs[sq].add(val)
        return True
