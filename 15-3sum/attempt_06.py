class Solution:
    def threeSum(self, nums):
        # start by sorting list
        nums.sort()
        # choose first element to setup two-sum
        idx = 0
        res = []
        while nums[idx] <= 0 and idx < len(nums) - 2:
            # since no duplicates, skip iteration if equal to prev elt
            if idx > 0 and nums[idx] == nums[idx - 1]:
                idx += 1
            else:
                # setup two-sum problem
                target = -nums[idx]
                lo = idx + 1
                hi = len(nums) - 1
                while lo < hi:
                    curr = nums[lo] + nums[hi]
                    if curr == target:
                        res.append([-target, nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while hi > lo and nums[hi] == nums[hi + 1]:
                            hi -= 1
                    elif curr < target:
                        lo += 1
                    else:
                        hi -= 1
                # iterate idx, should be a way to do this 'smarter'
                idx += 1
        return res
