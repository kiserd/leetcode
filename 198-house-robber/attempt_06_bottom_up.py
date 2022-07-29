from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # handle edge case
        if len(nums) < 3:
            return max(nums)
        # only need to keep track of two vars
        two_back = nums[0]
        one_back = max(nums[:2])
        for idx in range(2, len(nums)):
            two_back, one_back = one_back, max(nums[idx] + two_back, one_back)
        return one_back
