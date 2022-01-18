class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        # initialize memo array
        dp = [[0] * len(nums) for i in range(2)]
        dp[0][0] = max(0, nums[0])
        dp[1][0] = min(0, nums[0])
        # build memo from bottom up
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[0][i] = max(dp[0][i - 1] * nums[i], nums[i])
                dp[1][i] = min(dp[1][i - 1] * nums[i], dp[0][i - 1])
            elif nums[i] < 0:
                dp[0][i] = max(dp[1][i - 1] * nums[i], 0)
                dp[1][i] = min(dp[0][i - 1] * nums[i], nums[i])
            else:
                dp[0][i] = 0
                dp[1][i] = 0
        return max(dp[0])
