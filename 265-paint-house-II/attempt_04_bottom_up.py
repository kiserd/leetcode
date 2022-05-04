class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        prevs = [costs[0][i] for i in range(k)]
        for house in range(1, n):
            new_prev = [costs[house][i] for i in range(k)]
            for color in range(k):
                other_colors = [i for i in range(k) if i != color]
                res = 2001
                for other_color in other_colors:
                    res = min(res, prevs[other_color])
                new_prev[color] += res
            prevs = new_prev
        return min(prevs)
