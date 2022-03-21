class Solution:
    def merge(self, intervals):
        # sort intervals by start_i
        intervals.sort(key=lambda x: x[0])
        # process sorted array
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # handle case where merge is needed
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            # handle case where new interval should begin
            else:
                res.append(intervals[i])
        return res
