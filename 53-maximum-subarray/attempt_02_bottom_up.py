# bottom-up
# try to save on time and space a bit
class Solution:
    def maxSubArray(self, nums) -> int:
        # instead of memo array, maintain one value
        prev = nums[0]
        # use one variable to track max for full array
        max_sub = prev
        # build memo from base case - up
        for i in range(1, len(nums)):
            # handle case where current subarray total is negative / zero
            if prev <= 0:
                prev = nums[i]
            # handle case where current subarray total is positive
            else: 
                prev = prev + nums[i]
            # handle case where running max subarray needs updated
            if prev > max_sub:
                max_sub = prev
        return max_sub
