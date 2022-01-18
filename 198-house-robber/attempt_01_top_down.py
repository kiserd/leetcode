class Solution:
    def rob(self, nums):
        # define recursive helper function
        def dp(i):
            # return memo, if result exists
            if memo[i] is not None:
                return memo[i]
            # recursively explore options
            memo[i] = max(nums[i - 1] + dp(i - 2), dp(i - 1))
            return memo[i]

        # build memo array, define base cases implicitly
        memo = [None] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        return dp(len(nums))
        