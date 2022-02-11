# returning to problem to solve via intuition
class Solution:
    def maxProfit(self, prices) -> int:
        min_left = 10000
        res = 0
        for price in prices:
            res = max(res, price - min_left)
            min_left = min(min_left, price)
        return res

