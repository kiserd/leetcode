from copy import copy

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def add_val(row, col, val, update_board=True):
            """ adds val to board @ (row, col) """
            # calculate square index
            sq = (row // 3) * 3 + (col // 3)
            # add val to tracking sets
            rows[row].add(val)
            cols[col].add(val)
            sqs[sq].add(val)
            # add val to board
            if update_board:
                board[row][col] = val

        def is_valid(row, col, val):
            """ indicates whether val is valid @ (row, col) """
            sq = (row // 3) * 3 + (col // 3)
            if val in rows[row]:
                return False
            if val in cols[col]:
                return False
            if val in sqs[sq]:
                return False
            # all tests passed, indicate placement is valid
            return True

        def remove_val(row, col, val):
            """ removes val @ (row, col) """
            # calculate square index
            sq = (row // 3) * 3 + (col // 3)
            # add val to tracking sets
            rows[row].remove(val)
            cols[col].remove(val)
            sqs[sq].remove(val)
            # add val to board
            board[row][col] = '.'

        def backtrack(to_visit):
            """ works through possible sudoku solutions """
            # work is done when to_visit is empty
            if not to_visit:
                return True
            # pop a cell from to_visit to focus on
            row, col = to_visit.pop()
            for val in '123456789':
                if is_valid(row, col, val):
                    add_val(row, col, val)
                    # this is what held me up for a day: needed copy
                    if backtrack(copy(to_visit)):
                        return True
                    else:
                        remove_val(row, col, val)
            # handle case of no number valid in current cell
            return False

        # define some helper variables
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        sqs = [set() for _ in range(n)]
        to_visit = []
        # initialize board tracking sets
        for i in range(n):
            for j in range(n):
                # handle case of empty cell
                if board[i][j] == '.':
                    to_visit.append((i, j))
                # handle case of populated cell
                else:
                    add_val(i, j, board[i][j], update_board=False)
        # call function
        backtrack(copy(to_visit))
