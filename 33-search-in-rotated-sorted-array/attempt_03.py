class Solution:
    def search(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            # calculate our mid index
            mid = lo + (hi - lo) // 2
            # see if our mid is a target hit
            if nums[mid] == target:
                return mid
            # handle case where [lo, hi] does not span the beg of orig arr
            # here we proceed with vanilla binary search
            if nums[lo] <= nums[mid] <= nums[hi]:
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # handle case where [lo, hi] DOES span beg of orig arr
            elif nums[hi] <= nums[lo] <= nums[mid]:
                if target > nums[mid] or target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif nums[mid] <= nums[hi] <= nums[lo]:
                if target >= nums[lo] or target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1