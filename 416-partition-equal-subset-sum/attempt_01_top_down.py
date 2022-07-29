# getting a TLE, but things seem to be behaving appropriately
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = 0
        for num in nums:
            total += num
        # handle potential to return early
        if total % 2 == 1:
            return False

        def dp(i, amt):
            # handle base case(s)
            if amt == 0:
                return True
            if amt < 0:
                return False
            if i < 0:
                return False
            # handle recursive exploration
            if (i, amt) not in memo:
                include = False
                if amt >= nums[i]:
                    include = dp(i - 1, amt - nums[i])
                exclude = dp(i - 1, amt)
                memo[(i, amt)] = include or exclude
            return memo[(i, amt)]
        return dp(len(nums) - 1, total // 2)
