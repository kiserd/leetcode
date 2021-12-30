# bottom up
# Kadane's Algorithm
# Giving things a try from the other direction

class Solution:
    def maxProfit(self, prices) -> int:
        # setup problem according to Kadane's Algorithm exploration
        best = 0
        min_to_left = 10001
        # process array from end-to-beginning
        for price in prices:
            # handle case where our max less buying opportunity is negative
            if price < min_to_left:
                min_to_left = price
            # handle case where our max less buying opportunity is positive
            elif price - min_to_left > best:
                best = price - min_to_left
        return best
