# had good instincts on this one, but sloppy understanding of how to best
# implement

# initially attempted tracking actual max number, but wasn't connecting the
# dots on how to best keep track of the associated index (for when that elt
# fell out of the sliding window)

# return later and implement from intuition

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        # utilize queue in tracking max
        q = deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res = [nums[q[0]]]
        for i in range(k, len(nums)):
            if q[0] == i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res
