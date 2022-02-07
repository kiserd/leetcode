# first naive attempt without peeking at any solution hints
class Solution:
    def mincostTickets(self, days, costs) -> int:
        # define recursive function
        def dp(i):
            # handle base case(s)
            if i == len(days):
                return 0
            # handle recursive exploration
            if not memo[i]:
                thirty = None
                seven = None
                j = 1
                while i + j < len(days) and j < 30 and (thirty is None or seven is None):
                    if seven is None and days[i + j] >= days[i] + 7:
                        seven = costs[1] + dp(i + j)
                    if thirty is None and days[i + j] >= days[i] + 30:
                        thirty = costs[2] + dp(i + j)
                    j += 1
                if not thirty:
                    thirty = costs[2]
                if not seven:
                    seven = costs[1]
                single = costs[0] + dp(i + 1)
                memo[i] = min(single, seven, thirty)
            return memo[i]

        # build memo array
        memo = [None] * len(days)
        memo[len(days) - 1] = min(costs)
        # kick off function
        return dp(0)

            