class Solution:
    def twoSumLessThanK(self, nums, k: int) -> int:
        # sort the array to make binary search possible
        nums.sort()
        # iterate through potential "left" numbers (i)
        res = -1
        i = 0
        while i < len(nums) - 1 and nums[i] + nums[i + 1] < k:
            # use binary search to find max "right" number (j)
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                # key here is adding the one to take the high mid-point
                # that way, we can continue closing lo in on our max
                # element that satisfies the condition i.e. lo = mid
                # instead of lo = mid + 1
                mid = lo + ((hi - lo + 1) // 2)
                if nums[i] + nums[mid] < k:
                    lo = mid
                else:
                    hi = mid - 1
            # still need to make sure a valid lo index was found
            if nums[i] + nums[lo] < k:
                res = max(res, nums[i] + nums[lo])
            i += 1
        return res
