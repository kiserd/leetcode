class Solution:
    def rob(self, nums):
        # handle edge case
        if len(nums) < 3:
            return max(nums)
        # build memo array
        dp = [None] * len(nums)
        dp[len(nums) - 1] = nums[len(nums) - 1]
        dp[len(nums) - 2] = max(nums[len(nums) - 2:])
        # build memo array back to front
        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]

# dp[i] = max amount to be robbed from subarray of ith house to end
# doesn't necessarily mean we choose to rob the ith house, we lose our
# understanding of whether we choose the ith house, because it doesn't matter

# [2, 1, 1, 2]
#          [2]
#       [2, 2]
#    [3, 2, 2]
# here, we choose between 3 and 2 + 2
# [4, 3, 2, 2]