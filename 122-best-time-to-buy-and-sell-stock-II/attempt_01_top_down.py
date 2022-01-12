class Solution:
    def maxProfit(self, prices) -> int:
        # define recursive function
        def dp(i, holding):
            # if memoized result exists, return it
            if memo[i][holding] is not None:
                return memo[i][holding]
            # handle recursive exploration
            if holding:
                memo[i][holding] = max(dp(i - 1, 1), dp(i - 1, 0) - prices[i])
                # return max(dp(i - 1, 1), dp(i - 1, 0) - prices[i])
            else:
                memo[i][holding] = max(dp(i - 1, 0), dp(i - 1, 1) + prices[i])
                # return max(dp(i - 1, 0), dp(i - 1, 1) + prices[i])
            return memo[i][holding]
        # build memo, define base cases implicitly
        memo = [[None] * 2 for i in range(len(prices))]
        memo[0][0], memo[0][1] = 0, -prices[0]
        return dp(len(prices) - 1, 0)
