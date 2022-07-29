from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [None] * len(nums)

        def dp(i):
            # handle base case
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[:2])
            # handle recursive exploration
            if memo[i] is None:
                memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))
            return memo[i]
        return dp(len(nums) - 1)
