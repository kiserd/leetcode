from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # define memo array
        memo = [None] * len(cost)
        # define base cases implicitly in memo
        memo[0], memo[1] = cost[0], cost[1]

        # define recursive function
        def dp(i):
            # handle recursive exploration
            if memo[i] is None:
                memo[i] = min(dp(i - 1), dp(i - 2)) + cost[i]
            return memo[i]
        dp(len(cost) - 1)
        return min(memo[-1], memo[-2])
