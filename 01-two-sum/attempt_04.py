class Solution:
    def twoSum(self, nums, target: int):
        helper = {}
        for idx, num in enumerate(nums):
            if target - num in helper:
                return [helper[target - num], idx]
            else:
                helper[num] = idx
