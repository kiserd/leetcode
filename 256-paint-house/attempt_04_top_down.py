class Solution:
    def minCost(self, costs) -> int:
        # build memo array with implicit base cases
        n = len(costs)
        memo = [[None] * 3 for _ in range(n)]
        memo[n - 1] = costs[n - 1]
        # define recursive function
        def dp(house, color):
            # base cases implicitly defined in memo
            # handle recursive exploration
            if memo[house][color] is None:
                colors = [i for i in range(3) if i != color]
                res = 2001
                for clr in colors:
                    res = min(res, dp(house + 1, clr))
                memo[house][color] = costs[house][color] + res
            return memo[house][color]
        # kick off recursive function for all start colors
        for clr in range(3):
            dp(0, clr)
        # return min cost of painting first
        for row in memo:
            print(row)
        return min(memo[0])
