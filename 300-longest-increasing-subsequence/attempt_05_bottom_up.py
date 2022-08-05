from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            j = i - 1
            mx = 1
            while dp[i] is None and j > -1:
                if nums[i] > nums[j]:
                    mx = max(mx, 1 + dp[j])
                j -= 1
            dp[i] = mx
        return max(dp)
