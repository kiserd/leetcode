class Solution:
    def findMin(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[lo] < nums[mid] < nums[hi]:
                return nums[lo]
            if nums[lo] > nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
