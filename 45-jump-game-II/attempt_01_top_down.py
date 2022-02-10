class Solution:
    def jump(self, nums) -> int:
        # define recursive function
        def dp(i):
            # handle successful base case
            if i == len(nums) - 1: return 0
            # handle recursive exploration
            if not memo[i]:
                min_jumps = 10001
                for j in range(min(len(nums) - 1, i + nums[i]), i, -1):
                    min_jumps = min(min_jumps, 1 + dp(j))
                memo[i] = min_jumps
            return memo[i]
        # build memo array and kick off function
        memo = [None] * len(nums)
        return dp(0)
            