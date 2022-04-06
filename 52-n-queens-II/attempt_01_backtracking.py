class Solution:
    sols = 0
    def totalNQueens(self, n: int) -> int:
        def backtrack(row=0):
            """ recursively searches problem space for queen arrangements """
            # iterate through columns of current row
            for col in range(n):
                if not under_attack[(row, col)]:
                    place_queen(row, col)
                    if row == n - 1:
                        self.sols += 1
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        def place_queen(row, col):
            """ places a queen @ (row, col) """
            for i, j in get_vectors(row, col):
                under_attack[(i, j)] += 1

        def remove_queen(row, col):
            """ removes queen from (row, col) """
            for i, j in get_vectors(row, col):
                under_attack[(i, j)] -= 1

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

        # define helper variables
        under_attack = {(i, j): 0 for i in range(n) for j in range(n)}
        backtrack()
        return self.sols
