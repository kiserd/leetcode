class Solution:
    def minCost(self, costs) -> int:
        prevs = [costs[0][i] for i in range(3)]
        for house in range(1, len(costs)):
            new_prev = [costs[house][i] for i in range(3)]
            for color in range(3):
                other_colors = [i for i in range(3) if i != color]
                res = 2001
                for other_color in other_colors:
                    res = min(res, prevs[other_color])
                new_prev[color] += res
            prevs = new_prev
        print(prevs)
        return min(prevs)
