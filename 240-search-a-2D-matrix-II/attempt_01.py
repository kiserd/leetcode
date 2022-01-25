class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # define a couple helper variables
        m = len(matrix)
        n = len(matrix[0])
        # work from bottom-left to target or out of bounds
        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False