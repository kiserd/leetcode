class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # initialize a couple helper arrays
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
        # build prefix/suffix sum arrays
        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
            right_sum[len(nums) - i - 1] = right_sum[len(nums) - i] + nums[len(nums) - i]
        # find first hit according to problem spec
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
