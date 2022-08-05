import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        h = []
        res = 0
        for bg, ed in intervals:
            while h and bg >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, ed)
            res = max(res, len(h))
        return res
