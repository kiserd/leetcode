class Solution:
    def climbStairs(self, n: int) -> int:
        # define recursive function
        def dp(i):
            if memo[i] is None:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        # build memo array with implicit base cases
        memo = [None] * (n + 1)
        memo[1] = 1
        memo[2] = 2
        return dp(n)