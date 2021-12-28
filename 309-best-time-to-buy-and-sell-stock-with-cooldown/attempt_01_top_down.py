# top-down
from functools import lru_cache
class Solution:
    def maxProfit(self, prices) -> int:
        # define recursive function
        @lru_cache(None)
        def dp(i, has_stock):
            # handle base case of after final day
            if i >= len(prices):
                return 0
            # recursively explore opportunity to do nothing
            do_nothing = dp(i + 1, has_stock)
            change = 0
            # handle case where user is currently holding stock
            if has_stock:
                change = max(change, prices[i] + dp(i + 2, not has_stock))
            else:
                change = max(change, -prices[i] + dp(i + 1, not has_stock))
            # return maximum of doing nothing and transacting
            return max(do_nothing, change)
        # kick off recursive exploration and return result
        return dp(0, False)