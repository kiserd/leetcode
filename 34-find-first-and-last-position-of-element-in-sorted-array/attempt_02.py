class Solution:
    def searchRange(self, nums, target):
        # handle edge case
        if not nums:
            return [-1, -1]
        lo = 0
        hi = len(nums) - 1
        hi_bound = hi
        # first search for starting position
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi_bound = min(hi_bound, mid)
                hi = mid - 1
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        # handle case of target not found
        if nums[hi] != target:
            return [-1, -1]
        # find ending position
        res = [hi]
        lo, hi = res[0], hi_bound
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        res.append(lo)
        return res
