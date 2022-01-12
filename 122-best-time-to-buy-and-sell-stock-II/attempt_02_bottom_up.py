# use sliding window instead of full memo array
class Solution:
    def maxProfit(self, prices) -> int:
        # only keep track of previous maximums
        holding = -prices[0]
        not_holding = 0
        # build memo array bottom up, from back of array to front
        for i in range(1, len(prices), 1):
            # handle case where holding at end of ith decision
            new_holding = max(holding, not_holding - prices[i])
            # handle case where not holding at end of jth decision
            new_not_holding = max(holding + prices[i], not_holding)
            # set variables for next round
            holding, not_holding = new_holding, new_not_holding
        return not_holding
