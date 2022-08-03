import math


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        # sort array for efficient processing
        nums.sort()
        # process similar to regular 3-sum
        res = math.inf
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if abs(target - res) > abs(target - curr):
                    res = curr
                # update pointers
                if curr > target:
                    k -= 1
                else:
                    j += 1
            i += 1
        return res
