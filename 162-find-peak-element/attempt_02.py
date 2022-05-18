import math


class Solution:
    def findPeakElement(self, nums) -> int:
        nums = [-math.inf] + nums + [-math.inf]
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            if nums[mid + 1] > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1
