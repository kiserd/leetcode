from collections import deque


class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        # handle edge case
        if k == 0:
            return 0
        # attempt problem using a queue
        res = 0
        q = deque()
        prod = 1
        for num in nums:
            prod *= num
            q.append(num)
            while q and prod >= k:
                prod = prod // q.popleft()
            res += len(q)
        return res
