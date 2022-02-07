import math
class Solution:
    def minCost(self, costs) -> int:
        # define recursive function
        def dp(i, j):
            # handle base case
            if memo[i][j]:
                return memo[i][j]
            # handle recursive exploration
            elts = [0, 1, 2]
            elts.pop(j)
            res = math.inf
            for elt in elts:
                res = min(res, dp(i - 1, elt) + costs[i][j])
            memo[i][j] = res
            return res
        # define memo array and kick off function
        memo = [[None] * 3 for _ in range(len(costs))]
        memo[0] = costs[0]
        dp(len(memo) - 1, 0)
        dp(len(memo) - 1, 1)
        dp(len(memo) - 1, 2)
        return min(memo[len(memo) - 1])
