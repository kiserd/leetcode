from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            # handle potential 'hit'
            if nums[mid] == target:
                return mid
            # handle bin search processing
            # handle range that does NOT span end of orig arr
            if nums[lo] <= nums[mid] <= nums[hi]:
                # proceed with vanilla bin search
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # handle range that DOES span end of orig arr
            else:
                # mid is on 'back half' of original array
                if nums[mid] > nums[hi]:
                    if target > nums[mid] or target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                # mid is on 'begin half' of original array
                else:
                    if nums[mid] < target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        return -1
