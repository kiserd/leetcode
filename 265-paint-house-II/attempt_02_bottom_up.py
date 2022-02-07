class Solution:
    def minCostII(self, costs) -> int:
        # track cost to paint previous house a given color
        prev = costs[0]
        for hs in range(1, len(costs)):
            # track min cost to paint colors to left and
            # right of given color
            min_l = [None] * len(prev)
            min_l[0] = 2000
            min_r = [None] * len(prev)
            min_r[len(min_r) - 1] = 2000
            for i in range(1, len(prev)):
                min_l[i] = min(min_l[i - 1], prev[i - 1])
            for i in range(len(prev) - 2, -1, -1):
                min_r[i] = min(min_r[i + 1], prev[i + 1])
            # calculate new prev values based on min left and right
            for i in range(len(prev)):
                prev[i] = min(min_l[i], min_r[i]) + costs[hs][i]
        # return min prev value for last house
        return min(prev)
