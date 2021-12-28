# top-down
# pretty awful runtime
from functools import lru_cache
class Solution:
    def maxProfit(self, k: int, prices) -> int:
        # define recursive function
        @lru_cache(None)
        def dp(i, j):
            # handle base case of no transactions left
            if j == 0:
                return 0
            # handle base case of full transaction can't occur
            if i > len(prices) - 2:
                return 0
            # recursively explore subsequent transaction opportunities
            # set max to the do nothing event
            do_nothing = dp(i + 1, j)
            max_profit = 0
            for d in range(i + 1, len(prices), 1):
                # explore case of buying stock today
                p1 = prices[d] - prices[i] + dp(d + 1, j - 1)
                max_profit = max(max_profit, p1)
            return max(max_profit, do_nothing)
    
        # build memo and kick off recursive exploration
        # memo = [[None] * (k + 1) for i in range(len(prices) + 1)]
        # print('starting memo: ', memo)
        return dp(0, k)
