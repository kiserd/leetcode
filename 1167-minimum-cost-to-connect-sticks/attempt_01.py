import heapq
class Solution:
    def connectSticks(self, sticks) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            inner_cost = heapq.heappop(sticks)
            inner_cost += heapq.heappop(sticks)
            cost += inner_cost
            heapq.heappush(sticks, inner_cost)
        return cost

