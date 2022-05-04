class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -10001
        prev = 0
        for num in nums:
            if prev + num < num:
                prev = num
            else:
                prev += num
            res = max(res, prev)
        return res
