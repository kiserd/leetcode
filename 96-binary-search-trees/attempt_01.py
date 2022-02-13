# I was trying to be too clever for my own good, trying to back into a super
# quick math solution. After BRIEFLY looking at the solution, it was clear how
# things should be approached (took a couple min to code up). When you return
# to this, try not to look at this solution too much
class Solution:
    def numTrees(self, n: int) -> int:
        # define recursive function
        def dp(i, j):
            # handle base case
            if j - i < 1:
                return 1
            # handle recursive exploration
            if memo[i][j] is None:
                ways = 0
                for k in range(i, j + 1):
                    ways += (dp(i, k - 1) * dp(k + 1, j))
                memo[i][j] = ways
            return memo[i][j]
        # build memo
        memo = [[None] * n for _ in range(n)]
        return dp(0, n - 1)

