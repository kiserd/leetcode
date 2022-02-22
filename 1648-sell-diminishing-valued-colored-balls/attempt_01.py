# feels like my use of heapq should improve things, but it does not seem to do
# so
import heapq
import copy
class Solution:
    def maxProfit(self, inventory, orders: int) -> int:
        # setup heap, might not use this
        h = []
        heapq.heapify(h)
        # get total number of balls
        max_freq = 0
        for num in inventory:
            max_freq = max(max_freq, num)
            heapq.heappush(h, -num)
        # use binary search to determine k
        lo = 0
        hi = max_freq
        while hi - lo > 1:
            mi = lo + (hi - lo) // 2
            balls_sold = 0
            temp_h = copy.copy(h)
            while temp_h and -temp_h[0] > mi:
                curr = -heapq.heappop(temp_h)
                balls_sold += curr - mi
            if balls_sold == orders:
                lo = hi = mi
            elif balls_sold > orders:
                lo = mi
            else:
                hi = mi
        k = hi
        # process heap values down to k while possible
        res = 0
        while -h[0] > k:
            curr = -heapq.heappop(h)
            res += self.fact_sum(curr, k)
            heapq.heappush(h, -k)
            orders -= (curr - k)
        # reduce max heap value by 1 until orders are filled
        res += (orders * k)
        return res % (10**9 + 7)

    def fact_sum(self, n, k):
        return (n - k) * (n + (k + 1)) // 2

