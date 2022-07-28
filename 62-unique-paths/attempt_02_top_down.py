class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # define recursive function
        def dp(i, j):
            # handle base case
            if memo[i][j] is not None:
                return memo[i][j]
            # handle recursive exploration
            memo[i][j] = dp(i - 1, j) + dp(i, j - 1)
            return memo[i][j]
        # build memo array and define base cases implicitly
        memo = [[None] * (n + 1) for i in range(m + 1)]
        for i in range(n + 1):
            memo[0][i] = 0
        for i in range(m + 1):
            memo[i][0] = 0
        memo[1][1] = 1
        # call recursive function from bottom-right corner
        return dp(m, n)
