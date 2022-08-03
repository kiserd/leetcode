class Solution:
    def insert(self, intervals, newInterval):
        # handle edge case
        if len(intervals) == 0:
            return [newInterval]
        n = len(intervals)
        res = []
        # begin by intervals "prior to" newInterval
        idx = 0
        while idx < n and newInterval[0] > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1
        # handle edge case
        if len(res) == n:
            res.append(newInterval)
            return res
        # merge overlapping intervals
        st = min(intervals[idx][0], newInterval[0])
        ed = newInterval[1]
        while idx < n and ed >= intervals[idx][0]:
            ed = max(ed, intervals[idx][1])
            idx += 1
        res.append([st, ed])
        # re-increment idx and add remaining intervals
        while idx < n:
            res.append(intervals[idx])
            idx += 1
        return res
