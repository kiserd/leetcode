import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        # use heap to store end times of 'started' meetings
        h = []
        res = 0
        for st, ed in intervals:
            while h and h[0] <= st:
                heapq.heappop(h)
            heapq.heappush(h, ed)
            res = max(res, len(h))
        return res
