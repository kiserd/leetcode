# top-down
# not sure how to do in a 1-D array
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins) -> int:
        # define recursive function
        @lru_cache(None)
        def dp(i, j):
            # base case: 1 way to make change for 0 with any coins available
            if i == 0:
                return 1
            # base case: no coins available, amount != 0
            if j < 0:
                return 0
            # handle recursive exploration
            # if most recently made available coin is less than amount, return
            # recursive exploration into amount less this coin (with that coin'
            # still available). Add that to recursive exploration into amount
            # without that coin available
            if coins[j] <= i:
                return dp(i - coins[j]) + dp(i, j - 1)
            # if we can't use most recently made available coin, just return
            # recursive result of same amount of change without that coin
            # available
            else:
                return dp(i, j - 1)
        # call for all coins available and the total amount
        return dp(amount, len(coins))