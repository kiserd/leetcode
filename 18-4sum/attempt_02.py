class Solution:
    def fourSum(self, nums, target: int):
        # begin by sorting the array to improve efficiency
        nums.sort()

        # define k-sum function
        def ksum(idx, target, k):
            # handle unsuccessful base case
            if target <= 0 and nums[idx] > 0:
                return []
            # handle successful base case
            if k == 2:
                return twosum(idx, target)
            # handle recursive exploration
            res = []
            i = idx
            while i <= len(nums) - k:
                if i == idx or nums[i] != nums[i - 1]:
                    for quad in ksum(i + 1, target - nums[i], k - 1):
                        res.append([nums[i]] + quad)
                i += 1
            return res

        # define 2-sum function
        def twosum(idx, tgt):
            # utilize two pointer approach
            lo = idx
            hi = len(nums) - 1
            res = []
            while lo < hi:
                if nums[lo] + nums[hi] == tgt:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # protect against duplicate quadruples
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif nums[lo] + nums[hi] < tgt:
                    lo += 1
                else:
                    hi -= 1
            # no solution found, return empty list
            return res

        return ksum(0, target, 4)
