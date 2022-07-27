class Solution:
    def subarraySum(self, nums, k: int):
        res = 0
        left_sums = {}
        total = 0
        for num in nums:
            # first update left_sums mapping for prior elt
            left_sums[total] = left_sums.get(total, 0) + 1
            # update total for current elt
            total += num
            # calculate lookup value and increment res
            res += left_sums.get(total - k, 0)
        return res
