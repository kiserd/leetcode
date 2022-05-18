import math

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # define recursive helper function
        def dp(lo, hi):
            # handle base case
            if lo >= hi:
                return 0
            # handle recursive exploration
            if memo[lo][hi] is None:
                res = math.inf
                for guess in range(lo, hi + 1):
                    # recursively search cases where our guess
                    # is higher/lower than potential num
                    higher = dp(guess + 1, hi)
                    lower = dp(lo, guess - 1)
                    # get worst case scenario from number being
                    # lower/higher than each possible guess
                    worst_case = guess + max(lower, higher)
                    # if we found a new min worst case, update res
                    res = min(res, worst_case)
                memo[lo][hi] = res
            return memo[lo][hi]
        memo = [[None] * (n + 1) for _ in range(n + 1)]
        return dp(1, n)
