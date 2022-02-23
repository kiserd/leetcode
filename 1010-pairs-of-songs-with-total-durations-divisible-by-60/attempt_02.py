class Solution:
    def numPairsDivisibleBy60(self, time):
        counts = [0] * 60
        res = 0
        for num in time:
            r = num % 60
            res += counts[r]
            match = (60 - r) % 60
            counts[match] += 1
        return res