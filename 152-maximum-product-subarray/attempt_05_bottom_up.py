from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # handle edge case
        if len(nums) == 1:
            return nums[0]
        # init memo arrays
        mx = [0] * (len(nums) + 1)
        mn = [0] * (len(nums) + 1)
        # iterate through array, updating memos
        for idx, num in enumerate(nums):
            mx[idx + 1] = max(num, mx[idx] * num, mn[idx] * num)
            mn[idx + 1] = min(num, mx[idx] * num, mn[idx] * num)
        return max(mx)
