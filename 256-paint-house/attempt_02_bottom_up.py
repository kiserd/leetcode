# giving bottom-up a try
import math
class Solution:
    def minCost(self, costs) -> int:
        # define memo array
        dp = [[None] * 3 for _ in range(len(costs))]
        dp[0] = costs[0]
        # build memo array from bottom up
        arr = [0, 1, 2]
        for i in range(1, len(costs)):
            for j in range(3):
                min_cost = math.inf
                for idx in arr:
                    if idx != j:
                        min_cost = min(min_cost, dp[i - 1][idx])
                dp[i][j] = min_cost + costs[i][j]
        return min(dp[len(dp) - 1])
