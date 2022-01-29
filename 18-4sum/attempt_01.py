class Solution:
    def fourSum(self, nums, target: int):
        # handle edge case
        if len(nums) < 4:
            return [[]]
        # sort array in O(n logn)
        nums.sort()
        
        
