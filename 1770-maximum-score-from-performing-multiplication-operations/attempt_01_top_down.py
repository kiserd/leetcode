# this one got real tricky with avoiding the TLE / MLE due to the cache not
# being cleared
from functools import lru_cache
class Solution:
    def maximumScore(self, nums, multipliers) -> int:
        # define recursive function
        @lru_cache(2000)
        def dp(i, k):
            # handle base case
            if k == len(multipliers): return 0
            # handle recursive exploration
            use_i = nums[i] * multipliers[k] + dp(i + 1, k + 1)
            avoid_i = nums[len(nums) - 1 - (k - i)] * multipliers[k] + dp(i, k + 1)
            return max(use_i, avoid_i)
        # kick off function
        res = dp(0, 0)
        # clear the cache between test cases to avoid TLE
        dp.cache_clear()
        return res