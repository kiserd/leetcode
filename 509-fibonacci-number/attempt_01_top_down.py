class Solution:
    def fib(self, n: int) -> int:
        # handle edge case
        if n < 2: return n
        # define recursive function
        def dp(i):
            # handle recursive exploration
            if memo[i] is None:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        # define memo array with implicit base cases
        memo = [None] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        return dp(n)