import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        # sort meeting intervals by start_i
        intervals.sort(key=lambda elt: elt[0])
        # try using min heap to track meeting end times
        heap = []
        heapq.heapify(heap)
        min_rooms = 0
        # loop through intervals
        for interval in intervals:
            st, ed = interval
            # pop meetings that end before current meeting starts
            while len(heap) > 0 and heap[0] <= st:
                heapq.heappop(heap)
            # push current meeting onto min-heap
            heapq.heappush(heap, ed)
            # check whether we needed a higher # of rooms to accomadate
            min_rooms = max(min_rooms, len(heap))
        return min_rooms

