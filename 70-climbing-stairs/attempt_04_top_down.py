class Solution:
    def climbStairs(self, n: int) -> int:
        # build memo array
        memo = [None] * (n + 1)

        # define recursive function
        def dp(i):
            # handle base case
            if i < 3:
                return i
            # handle recursive exploration
            if not memo[i]:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        return dp(n)
