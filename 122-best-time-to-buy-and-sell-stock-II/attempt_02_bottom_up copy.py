# quick and dirty, make sure I can solve from intuition
# all we really need to know is the optimal state for any iteration's
# 'holding stock' and 'not holding stock' cash balance
from math import inf
class Solution:
    def maxProfit(self, prices) -> int:
        h = -inf
        n = 0
        for price in prices:
            h, n = max(h, n - price), max(n, h + price)
        return n