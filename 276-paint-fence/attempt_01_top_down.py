# top-down
from functools import lru_cache
class Solution:
    def numWays(self, n: int, k: int) -> int:
        # define recursive function
        @lru_cache(None)
        def dp(i):
            # handle base cases
            if i == 0:
                return k
            if i == 1:
                return k * k
            # handle recursive exploration
            different_color = (k - 1) * dp(i - 1)
            same_color = 1 * (k - 1) * dp(i - 2)
            return same_color + different_color
        # call from final post and return to calling function
        return dp(n - 1)
