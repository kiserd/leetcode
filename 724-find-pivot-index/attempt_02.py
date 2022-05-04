class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # get sum of array
        total = sum(nums)
        # iterate through, testing for pivot hit
        left = 0
        right = total
        for idx in range(len(nums)):
            if idx != 0:
                left += nums[idx - 1]
            right -= nums[idx]
            if left == right:
                return idx
        return -1
