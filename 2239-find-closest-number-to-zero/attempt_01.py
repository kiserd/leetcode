class Solution:
    def findClosestNumber(self, nums) -> int:
        curr = 10**6
        res = None
        for num in nums:
            if abs(num) < curr:
                res, curr = num, abs(num)
            elif abs(num) == curr:
                res = max(res, num)
        return res
