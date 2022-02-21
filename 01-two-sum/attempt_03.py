class Solution:
    def twoSum(self, nums, target: int):
        helper = {}
        for i, num in enumerate(nums):
            if helper.get(num, False):
                return [i, helper[num]]
            else:
                helper[target - num] = i