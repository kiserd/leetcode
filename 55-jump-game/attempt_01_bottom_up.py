class Solution:
    def canJump(self, nums) -> bool:
        # build out memo array
        dp = [None] * len(nums)
        dp[len(nums) - 1] = True
        for i in range(len(nums) - 2, -1, -1):
            # print('i: ', i)
            # print('nums[i]: ', nums[i])
            j = min(len(nums) - i - 1, nums[i])
            possible = False
            while j > 0 and not possible:
                # print('j: ', j)
                # print('dp[i + j]: ', dp[i + j])
                if dp[i + j]:
                    possible = True
                j -= 1
            dp[i] = possible
        print('dp: ', dp)
        return dp[0]




# i + j < len(nums)
#     j < len(nums) - i