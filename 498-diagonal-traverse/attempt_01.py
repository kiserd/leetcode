class Solution:
    def findDiagonalOrder(self, mat):
        # define some convenient helper variables
        m = len(mat)
        n = len(mat[0])
        # get "starting" cells
        starts = []
        for i in range(m):
            starts.append((i, 0))
        for j in range(1, n):
            starts.append((m - 1, j))
        # process array from starts
        res = []
        idx = 0
        left = True
        while idx < len(starts):
            left = not left
            row, col = starts[idx]
            idx += 1
            inner = []
            while -1 < row < m and -1 < col < n:
                inner.append(mat[row][col])
                row -= 1
                col += 1
            if left:
                for i in range(len(inner) - 1, -1, -1):
                    res.append(inner[i])
            else:
                for elt in inner:
                    res.append(elt)
        return res
