class Solution:
    def solveNQueens(self, n: int):
        # define function to determine attack vectors
        def get_vectors(row, col):
            """ returns list of 'attackable' cells for queen @ (row, col) """
            # get column-wise attackable cells
            res = [(i, col) for i in range(row + 1, n)]
            # get diagonal-wise attackable cells
            res += [(row + offset, col + offset) for offset in range(n) if row + offset < n and col + offset < n]
            res += [(row + offset, col - offset) for offset in range(n) if row + offset < n and col - offset > -1]
            # turn res into set and remove (row, col)
            res = set(res)
            return res

        # define function to place queen
        def place_queen(row, col):
            """ places queen @ (row, col) """
            # add cell to queens set
            queens.add((row, col))
            # remove attackable cells from eligible set
            attackable_cells = get_vectors(row, col)
            for i, j in attackable_cells:
                if (i, j) in eligible:
                    eligible.remove((i, j))
            # add queen placement to attackable set
            for i, j in attackable_cells:
                attackable[(i, j)].add((row, col))

        # define function to remove queen
        def remove_queen(row, col):
            """ removes queen from (row, col) """
            # only process if a queen was previously placed
            if (row, col) in queens:
                queens.remove((row, col))
                # update attackable dict and move cells to eligible (if applicable)
                for i, j in get_vectors(row, col):
                    attackable[(i, j)].remove((row, col))
                    if not attackable[(i, j)]:
                        eligible.add((i, j))

        # define function to build board
        def build_board(qs):
            """ builds board according to problems spec """
            board = [['.'] * n for _ in range(n)]
            for row, col in qs:
                board[row][col] = 'Q'
                board[row] = ''.join(board[row])
            return board

        # define backtracking function
        def backtrack(row):
            for col in range(n):
                if (row, col) in eligible:
                    place_queen(row, col)
                    if len(queens) == n:
                        sols.append(build_board(queens))
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        # establish some helper variables
        eligible = set([(i, j) for i in range(n) for j in range(n)])
        queens = set()
        attackable = {(i, j): set() for i in range(n) for j in range(n)}
        sols = []
        # call recursive backtracking function
        backtrack(0)
        return sols