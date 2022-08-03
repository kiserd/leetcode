# didn't really improve anything here, tried to make things more readable


class Solution:
    def insert(self, intervals, newInterval):
        # handle edge case
        if not intervals:
            return [newInterval]
        res = []
        bg, ed = newInterval
        inserted = False
        beg_found = False
        for val in intervals:
            if not inserted:
                if bg > val[1]:
                    res.append(val)
                else:
                    if not beg_found and ed < val[0]:
                        res.append([bg, ed])
                        res.append(val)
                        inserted = True
                    elif not beg_found:
                        bg = min(bg, val[0])
                        ed = max(ed, val[1])
                        beg_found = True
                    elif ed >= val[0]:
                        ed = max(ed, val[1])
                    elif ed < val[0]:
                        res.append([bg, ed])
                        res.append(val)
                        inserted = True
            else:
                res.append(val)
        if not inserted:
            res.append([bg, ed])
        return res
