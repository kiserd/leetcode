class Solution:
    def maxProfit(self, prices) -> int:
        hold = -10001
        not_hold = 0
        for price in prices:
            hold, not_hold = max(hold, not_hold - price), max(not_hold, hold + price)
        return not_hold
