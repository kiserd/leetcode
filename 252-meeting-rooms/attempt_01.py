from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda val: val[0])
        prev_end = -1
        for st, ed in intervals:
            if st < prev_end:
                return False
            prev_end = ed
        return True
