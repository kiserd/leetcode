class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        holding = -prices[0] - fee
        no_hold = 0
        # build memo array from bottom up
        for i in range(1, len(prices)):
            # not holding at the end of ith day
            no_hold = max(holding + prices[i], no_hold)
            # holding at the end of ith day
            holding = max(no_hold - prices[i] - fee, holding)
        # never the best move to end the period still holding stock
        return no_hold



# # improving things just a tiny bit by setting base cases differently (above)
# class Solution:
#     def maxProfit(self, prices, fee: int) -> int:
#         holding = -100001
#         no_hold = 0
#         # build memo array from bottom up
#         for i in range(len(prices)):
#             # not holding at the end of ith day
#             no_hold = max(holding + prices[i], no_hold)
#             # holding at the end of ith day
#             holding = max(no_hold - prices[i] - fee, holding)
#         # never the best move to end the period still holding stock
#         return no_hold