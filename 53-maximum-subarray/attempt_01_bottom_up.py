# bottom-up
# we still waste O(n) time looping through the array to find max(dp)
# 
# we can reduce space to O(1) by only keeping track of the previous subarray
# total
# 
# Explanation: 
# 
# If the previously explored subarray's total ever becomes
# negative, it is no longer "worth it" to include the contiguous negative
# elements as a means of including the next positive element.
# 
# Suppose the subarray ending at i - 1 has a negative total. Then, if we were
# to add the ith element to this subarray, our new total is less than the ith
# element's value alone.
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