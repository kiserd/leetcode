from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        delta = 1000000
        idx = 0
        while idx < len(nums) - 2:
            # prevent against processing dups
            # somehow this causes a TLE
            # if not idx or nums[idx] != nums[idx - 1]:
            lo = idx + 1
            hi = len(nums) - 1
            tgt = target - nums[idx]
            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if abs(tgt - curr_sum) < abs(delta):
                    delta = tgt - curr_sum
                if nums[lo] + nums[hi] > tgt:
                    hi -= 1
                    # bypass dups
                    while hi > lo and nums[hi] == nums[hi + 1]:
                        hi -= 1
                else:
                    lo += 1
                    # bypass dups
                    while hi > lo and nums[lo] == nums[lo - 1]:
                        lo += 1
            # increment idx
            idx += 1
        return target - delta
