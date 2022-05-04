class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # build memo array
        memo = [[None] * n for _ in range(m)]
        # define recursive function
        def dp(i, j):
            # handle base cases
            if i == m - 1 or j == n - 1:
                memo[i][j] = 1
                return 1
            # handle recursive exploration
            if memo[i][j] is None:
                memo[i][j] = dp(i + 1, j) + dp(i, j + 1)
            return memo[i][j]
        return dp(0, 0)
