# Author: Donald Logan Kiser
# Date: 08/11/2020
# Project: LeetCode Problem 1 Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for index1 in range(len(nums)):
            if nums[index1] <= target:
                for index2 in range(len(nums)):
                    if index1 == index2:
                        pass
                    elif nums[index1] + nums[index2] == target:
                        return [index1, index2]
                    else:
                        pass
                                    
                
