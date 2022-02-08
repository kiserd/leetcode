class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            if n < 1: return 0
            else: return 1
        # define recursive function
        def dp(i):
            if memo[i] is None:
                memo[i] = dp(i - 1) + dp(i - 2) + dp(i - 3)
            return memo[i]

        # build memo array and define base cases implicitly
        memo = [None] * (n + 1)
        memo[0] = 0
        memo[1] = memo[2] = 1
        return dp(n)