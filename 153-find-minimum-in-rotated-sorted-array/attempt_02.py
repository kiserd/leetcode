# adding a slight tweak to remove the need to update min_elt from attempt_01
class Solution:
    def findMin(self, nums):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # attempt to return early if mid is beginning of orig array
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            # realized we can return early in this scenario as well
            if nums[lo] <= nums[mid] <= nums[hi]:
                return min(nums[lo], nums[hi])
            elif nums[hi] <= nums[lo] <= nums[mid]:
                lo = mid + 1
            elif nums[mid] <= nums[hi] <= nums[lo]:
                hi = mid - 1
        return nums[mid]


# big breakthrough in this attempt w/ rotated sorted array was understanding
# that there are really only three scenarios:

# (1) the subarray does NOT span the element where the beginning of the array
#     was rotated to. Here, we can continue with vanilla binary search
#     ** on second glance, realized we can return early here, because the min
#     element MUST be either lo or hi

# (2) the subarray DOES span the element where the beginning of the array was
#     rotated to AND both the lo and mid element are to the left of that
#     element:
#              nums[hi] <= nums[low] <= nums[mid]

# (3) the subarray DOES span the element where the beginning of the array was
#     rotated to AND both the mid and hi element are either equal to the
#     element or to the right of it:
#              nums[mid] <= nums[hi] <= nums[low]
