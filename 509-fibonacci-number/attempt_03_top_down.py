class Solution:
    def fib(self, n: int):
        # define recursive function
        def dp(i):
            # handle base case
            if i == 0 or i == 1:
                return i
            # handle recursive case
            if not memo[i]:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        # build memo array
        memo = [None] * (n + 1)
        return dp(n)
