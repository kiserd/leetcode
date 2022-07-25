class Solution:
    def subarraySum(self, nums, k: int):
        left_sums = {0: 1}
        curr = 0
        res = 0
        for num in nums:
            curr += num
            res += left_sums.get(curr - k, 0)
            left_sums[curr] = left_sums.get(curr, 0) + 1
        return res

