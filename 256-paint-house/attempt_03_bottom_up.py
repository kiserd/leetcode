# give sliding window a try
class Solution:
    def minCost(self, costs) -> int:
        # initialize working variables
        red = costs[0][0]
        ylw = costs[0][1]
        grn = costs[0][2]
        # build memo array from bottom up
        for i in range(1, len(costs)):
            temp_red = red
            temp_ylw = ylw
            red = min(temp_ylw, grn) + costs[i][0]
            ylw = min(temp_red, grn) + costs[i][1]
            grn = min(temp_red, temp_ylw) + costs[i][2]
        return min(red, ylw, grn)
