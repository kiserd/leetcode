# using fun trick from solution article
class Solution:
    def minCostII(self, costs) -> int:
        # track cost to paint previous house a given color
        for hs in range(1, len(costs)):
            # only need to track the min and second min
            # overwrite costs to save space
            min_i = min_c = scd_c = None
            for i, num in enumerate(costs[hs - 1]):
                if min_c is None or num < min_c:
                    scd_c = min_c
                    min_c, min_i = num, i
                elif scd_c is None or num < scd_c:
                    scd_c = num
            # update all but the same column with the min_c
            for i in range(len(costs[hs])):
                if i != min_i:
                    costs[hs][i] += min_c
                else:
                    costs[hs][i] += scd_c
        # return min of last row of costs
        return min(costs[len(costs) - 1])
