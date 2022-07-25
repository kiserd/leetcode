class Solution:
    def hammingWeight(self, n):
        res = 0
        mask = 2 ** 0
        while mask <= n:
            if n & mask != 0:
                res += 1
            mask *= 2
        return res