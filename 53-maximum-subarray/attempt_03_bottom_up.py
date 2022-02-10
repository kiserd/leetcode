# Kadane
class Solution:
    def maxSubArray(self, nums) -> int:
        outer_max = -10001
        prev = -1
        for i in range(len(nums)):
            prev = max(prev + nums[i], nums[i])
            outer_max = max(outer_max, prev)
        return outer_max
