# gets occasional TLE, but is also accepted
class Solution:
    def maximumScore(self, nums, multipliers) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            # the multipliers idx can't be less than the left idx (i)
            for k in range(m - 1, i - 1, -1):
                use_i = nums[i] * multipliers[k] + dp[i + 1][k + 1]
                avoid_i = nums[n - 1 - k + i] * multipliers[k] + dp[i][k + 1]
                dp[i][k] = max(use_i, avoid_i)
        return dp[0][0]