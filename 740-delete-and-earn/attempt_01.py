# try to clean this up with a sliding window
class Solution:
    def deleteAndEarn(self, nums) -> int:
        # build out helper dict
        helper = {}
        for num in nums:
            helper[num] = helper.get(num, 0) + num
        # build new nums array
        new_nums = sorted([key for key in helper])
        # build out memoization array
        dp = [0] * (len(new_nums) + 1)
        dp[1] = helper[new_nums[0]]
        # build memo array from bottom up
        for i in range(2, len(dp)):
            if new_nums[i - 2] == new_nums[i - 1] - 1:
                dp[i] = max(dp[i - 1], helper[new_nums[i - 1]] + dp[i - 2])
            else:
                dp[i] = dp[i - 1] + helper[new_nums[i - 1]]
        return dp[len(dp) - 1]
