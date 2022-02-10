class Solution:
    def getMaxLen(self, nums) -> int:
        neg = 0
        pos = 0
        max_len = 0
        for num in nums:
            if num < 0:
                if neg > 0:
                    neg, pos = pos + 1, neg + 1
                else:
                    neg, pos = pos + 1, 0
            elif num > 0:
                pos += 1
                if neg > 0:
                    neg += 1
                else:
                    neg = 0
            else:
                pos = neg = 0
            max_len = max(max_len, pos)
        return max_len
