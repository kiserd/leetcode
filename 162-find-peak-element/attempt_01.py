import math
class Solution:
    def findPeakElement(self, nums) -> int:
        # handle edge case
        if len(nums) == 1:
            return 0
        # define recursive function
        def search(nums, low, high):
            # construct helper vars
            mid = low + (high - low) // 2
            mid_elt = nums[mid]
            left_nbr = -(math.inf)
            right_nbr = -(math.inf)
            if mid - 1 > -1:
                left_nbr = nums[mid - 1]
            if mid + 1 < len(nums):
                right_nbr = nums[mid + 1]
            # handle base case
            if left_nbr < mid_elt and mid_elt > right_nbr:
                return mid
            # handle recursive exploration
            if mid_elt < right_nbr:
                return search(nums, mid + 1, high)
            else:
                return search(nums, low, mid - 1)
            
        return search(nums, 0, len(nums) - 1)

            



# naive attempt at a variation of binary search
#   - assuming binary search because they want O(log n) time

# nums[i] != nums[i + 1] guarantees there is a peak