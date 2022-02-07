from copy import copy
class Solution:
    def minCostII(self, costs) -> int:
        # define recursive function
        def dp(hs, clr):
            # handle base case
            if memo[hs][clr]: return memo[hs][clr]
            # handle recursive exploration
            min_cost = 2001
            for i in range(len(costs[0])):
                if i != clr:
                    min_cost = min(min_cost, costs[hs][clr] + dp(hs - 1, i))
            memo[hs][clr] = min_cost
            return min_cost
        # build memo array
        memo = [[None] * len(costs[0]) for _ in range(len(costs))]
        memo[0] = copy(costs[0])
        # kick off recursive function for final house color options
        for i in range(len(costs[0])):
            dp(len(costs) - 1, i)
        return min(memo[len(memo) - 1])
