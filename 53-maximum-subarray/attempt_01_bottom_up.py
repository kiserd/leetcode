class Solution:
    def maxSubArray(self, nums) -> int:
        # build out memo array, set base case implicitly
        dp = [None] * len(nums)
        dp[0] = nums[0]
        # build memo from base case - up
        for i in range(1, len(nums)):
            # handle case where current subarray total is negative / zero
            if dp[i - 1] <= 0:
                dp[i] = nums[i]
            # handle case where current subarray total is positive
            else: 
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)