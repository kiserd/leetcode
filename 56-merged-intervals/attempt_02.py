class Solution:
    def merge(self, intervals):
        # sort intervals by start_i
        intervals.sort(key=lambda x: x[0])
        # outer loop sets our starting index
        res = []
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            # inner loop finds our ending index
            i += 1
            while i < len(intervals) and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                i += 1
            res.append([start, end])
        return res
