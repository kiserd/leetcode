from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # start by calculating sum to right of each elt
        total = 0
        right_sums = []
        for idx in range(len(nums) - 1, -1, -1):
            right_sums = [total] + right_sums
            total += nums[idx]
        # process array from left to right in search of pivot
        left_sum = 0
        for idx, num in enumerate(nums):
            if left_sum == right_sums[idx]:
                return idx
            left_sum += num
        return -1
