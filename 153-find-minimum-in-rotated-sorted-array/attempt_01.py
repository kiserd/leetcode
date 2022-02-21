class Solution:
    def findMin(self, nums):
        low = 0
        hi = len(nums) - 1
        min_elt = 5001
        while low <= hi:
            mid = low + (hi - low) // 2
            min_elt = min(min_elt, nums[mid])
            if nums[low] <= nums[mid] <= nums[hi]:
                hi = mid - 1
            elif nums[hi] <= nums[low] <= nums[mid]:
                low = mid + 1
            elif nums[mid] <= nums[hi] <= nums[low]:
                hi = mid - 1
        return min_elt


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
