class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        # initialize helper variables
        max_sub = nums[0]
        max_pos = max(0, nums[0])
        min_neg = min(0, nums[0])
        # build memo from bottom up
        for i in range(1, len(nums)):
            if nums[i] != 0:
                temp = max_pos
                max_pos = max(temp * nums[i], min_neg * nums[i], nums[i])
                min_neg = min(min_neg * nums[i], temp * nums[i], nums[i])
            else:
                max_pos = 0
                min_neg = 0
            max_sub = max(max_sub, max_pos)
        return max_sub


# adjusting attempt 1, because only ever use prior values with lookup at end
# need to come back and review this