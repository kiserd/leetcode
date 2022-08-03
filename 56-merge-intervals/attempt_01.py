class Solution:
    def merge(self, intervals):
        # sort elements by start_i and prep working vars
        intervals.sort(key=lambda elt: elt[0])
        n = len(intervals)
        res = []
        i = 0
        # loop through intervals from beginning to end
        while i < n:
            # get starting interval values
            l, r = intervals[i]
            # iterate through potential intervals to merge with
            j = i + 1
            while j < n and intervals[j][0] <= r:
                r = max(r, intervals[j][1])
                j += 1
            # append to result and get new beginning index
            res.append([l, r])
            i = j
        return res
