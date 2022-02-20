class Solution:
    def getModifiedArray(self, length: int, updates):
        res = [0] * length
        for st, ed, inc in updates:
            res[st] += inc
            if ed < length - 1:
                res[ed + 1] -= inc
        # process array
        for i in range(1, length):
            res[i] += res[i - 1]
        return res