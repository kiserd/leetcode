from functools import lru_cache
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        # define recursive function
        @lru_cache(None)
        def dp(i, holding):
            # handle base case
            if i == len(prices) - 1:
                if holding:
                    return prices[len(prices) - 1] - fee
                else:
                    return 0
            # handle recursive exploration
            dono = dp(i + 1, holding)
            do = None
            if holding:
                do = prices[i] - fee + dp(i + 1, False)
            else:
                do = -prices[i] + dp(i + 1, True)
            return max(do, dono)
        return dp(0, False)
                