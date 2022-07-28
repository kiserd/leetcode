class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # init memo
        memo = {}
        # define recursive helper function

        def dp(i, j):
            # handle base case(s)
            if i < 0 or j < 0:
                return 0
            if i == 1 and j == 1:
                return 1
            # handle recursive exploration
            if not memo.get((i, j), False):
                memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
            return memo[(i, j)]
        return dp(m, n)
