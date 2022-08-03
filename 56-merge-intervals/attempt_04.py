from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the input based on start time
        intervals.sort(key=lambda val: val[0])
        # process input using two-ptr approach
        res = []
        bg, ed = intervals[0]
        for curr in intervals:
            if ed >= curr[0]:
                ed = max(ed, curr[1])
            else:
                res.append([bg, ed])
                bg, ed = curr
        # handle case where we still need to add "current" interval
        if not res or res[-1][1] != ed:
            res.append([bg, ed])
        return res
