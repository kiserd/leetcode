# Author: Donald Logan Kiser
# Date: 08/11/2020
# Description: attempt at LeetCode problem 1 in O(n) based on
#              solution hints posted on LeetCode website

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index in range(len(nums)):
            if nums[index] in map:
                return [map[nums[index]], index]
            else:
                map[target - nums[index]] = index