class Solution:
    def rob(self, nums):
        rob = 0
        dont = 0
        for i in range(len(nums)):
            rob, dont = nums[i] + dont, max(rob, dont)
        return max(rob, dont)
