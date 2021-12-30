# bottom up
# Kadane's Algorithm
# Explanation: We simply keep track of the current maximum selling opportunity
# to the "right" of the element being currently processed. During that time,
# we continue updating our best buy-sell window. If we find a new max selling
# opportunity, we can update max_to_right. Any elements to the left of our
# "new" max_to_right would obviously benefit further from being sold at the
# new max. I believe an optimal substructure proof would be pretty easy to
# execute, here.

class Solution:
    def maxProfit(self, prices) -> int:
        # setup problem according to Kadane's Algorithm exploration
        best = 0
        max_to_right = 0
        # process array from end-to-beginning
        for i in range(len(prices) - 1, -1, -1):
            # handle case where our max less buying opportunity is negative
            if prices[i] > max_to_right:
                max_to_right = prices[i]
            # handle case where our max less buying opportunity is positive
            elif max_to_right - prices[i] > best:
                best = max_to_right - prices[i]
        return best
