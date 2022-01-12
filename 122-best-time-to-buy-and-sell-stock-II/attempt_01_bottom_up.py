class Solution:
    def maxProfit(self, prices) -> int:
        # build memo array, and set base cases
        dp = [[None] * len(prices) for i in range(2)]
        dp[0][0], dp[1][0] = 0, -prices[0]
        # build memo array bottom up, from back of array to front
        for j in range(1, len(prices), 1):
            for i in range(2):
                # handle case where holding at end of jth decision
                if i == 1:
                    dp[i][j] = max(dp[0][j - 1] - prices[j], dp[i][j - 1])
                # handle case where not holding at end of jth decision
                else:
                    dp[i][j] = max(dp[1][j - 1] + prices[j], dp[i][j - 1])
        return dp[0][len(prices) - 1]




# on any given day, you have the options to:
# (1) buy stock, if you aren't already holding a share
# (2) sell stock, if you aren't already holding a share
# (3) do nothing, regardless of 'holding' state

# dp[i][j] where i in [0, 1] and j in [0, len(s))
# represents the max profit for prices up to j, given a holding state of i