from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # start by calculating total
        right_sum = 0
        for num in nums:
            right_sum += num
        # process array from left to right in search of pivot
        left_sum = 0
        for idx, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return idx
            left_sum += num
        return -1
