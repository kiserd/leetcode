from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_right = 0
        res = 0
        for idx in range(len(prices) - 1, -1, -1):
            res = max(res, max_right - prices[idx])
            max_right = max(max_right, prices[idx])
        return res
