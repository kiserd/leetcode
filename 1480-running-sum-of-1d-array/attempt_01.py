from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        for idx, num in enumerate(nums):
            curr += num
            nums[idx] = curr
        return nums
