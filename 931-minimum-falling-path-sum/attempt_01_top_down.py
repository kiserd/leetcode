import math
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        # handle edge case
        if len(matrix) == 1: return matrix[0][0]
        # define recursive function
        def dp(i, j):
            # handle base case
            if i == len(matrix) - 1:
                return matrix[i][j]
            # handle recursive exploration
            if memo[i][j] is None:
                min_path = math.inf
                for col in self.getCols(j, len(matrix)):
                    min_path = min(min_path, dp(i + 1, col))
                memo[i][j] = min_path + matrix[i][j]
            return memo[i][j]
        # define memo array
        memo = [[None] * len(matrix) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            dp(0, i)
        return min(memo[0])


    def getCols(self, j, n):
        if j == 0:
            return [j, j + 1]
        if j == n - 1:
            return [j - 1, j]
        return [j - 1, j, j + 1]