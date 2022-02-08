class Solution:
    def rob(self, nums) -> int:
        # handle edge case
        if len(nums) < 4: return max(nums)
        # call rob twice on subsets discluding begin/end
        return max(self.rob(nums[:-1]), self.rob(nums[1:]))

    def rob(self, nums):
        rob = 0
        dont = 0
        for i in range(len(nums)):
            rob, dont = nums[i] + dont, max(rob, dont)
        return max(rob, dont)