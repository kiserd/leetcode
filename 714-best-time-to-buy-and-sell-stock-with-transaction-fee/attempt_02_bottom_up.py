# still need to improve space complexity a bit
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        # build memo array
        memo = [[None] * len(prices) for _ in range(2)]
        memo[0][0] = 0
        memo[1][0] = -prices[0] - fee
        # build memo array from bottom up
        for i in range(1, len(prices)):
            # not holding at the end of ith day
            memo[0][i] = max(memo[0][i - 1], memo[1][i - 1] + prices[i])
            # holding at the end of ith day
            memo[1][i] = max(memo[1][i - 1], memo[0][i - 1] - prices[i] - fee)
        # never the best move to end the period still holding stock
        return memo[0][len(prices) - 1]