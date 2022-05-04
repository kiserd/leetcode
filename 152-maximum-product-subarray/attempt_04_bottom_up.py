class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # handle edge case
        if len(nums) == 1:
            return nums[0]
        # define memo array
        memo = [[None] * 2 for _ in range(len(nums) + 1)]
        # define "out of bounds" products
        memo[len(nums)][0] = 0
        memo[len(nums)][1] = 0
        # work bottom-up from end of array to front
        res = -10
        for idx in range(len(nums) - 1, -1, -1):
            # handle case of zero
            if nums[idx] == 0:
                memo[idx][0] = memo[idx][1] = 0
            # handle positive number
            elif nums[idx] > 0:
                memo[idx][1] = max(nums[idx], nums[idx] * memo[idx + 1][1])
                memo[idx][0] = nums[idx] * memo[idx + 1][0]
            else:
                memo[idx][1] = max(0, nums[idx] * memo[idx + 1][0])
                memo[idx][0] = min(nums[idx], nums[idx] * memo[idx + 1][1])
            res = max(res, memo[idx][1])
        return res
