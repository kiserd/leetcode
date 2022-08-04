from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for idx in range(1, len(nums)):
            res ^= nums[idx]
        return res
