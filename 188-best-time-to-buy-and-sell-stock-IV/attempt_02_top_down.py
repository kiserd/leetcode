# top-down
# try using dp with three variables, since we are handicapping with lru_cache
from functools import lru_cache
class Solution:
    def maxProfit(self, k: int, prices) -> int:
        # define recursive function
        @lru_cache(None)
        def dp(i, j, has_stock):
            # handle base case of no transactions left
            if j == 0:
                return 0
            # handle base case of full transaction can't occur
            if i >= len(prices):
                return 0
            # recursively explore subsequent transaction opportunities
            do_nothing = dp(i + 1, j, has_stock)
            profit = 0
            # explore case when holding stock
            if has_stock:
                profit = max(profit, prices[i] + dp(i + 1, j - 1, False))
            # explore cases when user is not holding stock
            else:
                profit = max(profit, -prices[i] + dp(i + 1, j, True))
            # return maximum of do_nothing and buy/sell to calling function
            return max(do_nothing, profit)
        # kick off recursive exploration
        return dp(0, k, False)