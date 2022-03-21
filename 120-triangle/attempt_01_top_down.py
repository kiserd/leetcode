from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle) -> int:
        # define recursive function
        @lru_cache(None)
        def dp(i, j):
            # handle base case
            if i == len(triangle) - 1:
                return triangle[i][j]
            return min(dp(i + 1, j), dp(i + 1, j + 1)) + triangle[i][j]
        # build memo array and kick off function
        return dp(0, 0)