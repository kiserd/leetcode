from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_back = cost[0]
        one_back = cost[1]
        for i in range(2, len(cost)):
            two_back, one_back = one_back, min(two_back, one_back) + cost[i]
        return min(two_back, one_back)
