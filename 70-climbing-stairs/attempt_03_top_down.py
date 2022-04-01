class Solution:
    def climbStairs(self, n: int) -> int:
        # define recursive function
        def dp(i):
            if i == 0 or i == 1:
                return i + 1
            if not memo[i]:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        # build memo array
        memo = [None] * n
        return dp(n - 1)
