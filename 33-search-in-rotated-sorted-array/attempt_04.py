class Solution:
    def search(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            # attempt to return before heavy-lifting hits
            if nums[mid] == target:
                return mid
            # handle case where [lo, hi] does NOT span beginning
            # of the original array
            if nums[lo] <= nums[mid] <= nums[hi]:
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # handle case where [lo, hi] spans beginning of the
            # original array
            else:
                if nums[mid] > nums[hi]:
                    if nums[lo] <= target < nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    if nums[mid] < target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        return -1
