class Solution:
    def canJump(self, nums) -> bool:
        # define recursive function
        def dp(i):
            # print('i: ', i)
            # print('memo: ', memo)
            # handle case where memoized result is available
            if memo[i] is not None:
                return memo[i]
            if nums[i] == 0:
                memo[i] = False
                return False
            # handle recursive case
            upper_bound = min(len(nums) - i - 1, nums[i]) + 1
            for j in range(1, upper_bound, 1):
                res = dp(i + j)
                if res:
                    memo[i] = True
                    return True
            # handle case where recursive exploration failed to hit final index
            memo[i] = False
            return False

        # build memo and define base case implicitly
        memo = [None] * len(nums)
        memo[len(nums) - 1] = True
        # call recursive function from first index
        return dp(0)