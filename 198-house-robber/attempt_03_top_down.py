class Solution:
    def rob(self, nums):
        # define recursive function
        def dp(i):
            if memo[i] is None:
                memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return memo[i]

        # build memo array with implicit base cases
        n = len(nums)
        memo = [None] * n
        memo[n - 1] = nums[n - 1]
        return dp(1)