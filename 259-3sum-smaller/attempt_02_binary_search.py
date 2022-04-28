class Solution:
    def threeSumSmaller(self, nums, target: int) -> int:
        # sort array and process in similar fashion to regular 3sum
        nums.sort()
        # attempt to return early
        if sum(nums[:3]) >= target:
            return 0
        # loop through potential "first" elements
        i = 0
        res = 0
        for i in range(len(nums) - 2):
            # loop through potential "second" elements
            for j in range(i + 1, len(nums) - 1):
                # utilize binary search in determining valid "third" elements
                lo = j + 1
                hi = len(nums) - 1
                while lo < hi:
                    mid = lo + ((hi - lo + 1) // 2)
                    if nums[i] + nums[j] + nums[mid] < target:
                        lo = mid
                    else:
                        hi = mid - 1
                if nums[i] + nums[j] + nums[lo] < target:
                    res += (lo - j)
        return res
