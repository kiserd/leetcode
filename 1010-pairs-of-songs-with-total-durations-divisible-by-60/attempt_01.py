class Solution:
    def numPairsDivisibleBy60(self, time):
        helper = {}
        res = 0
        for num in time:
            r = num % 60
            if r in helper:
                res += helper[r]
            match = (60 - r) % 60
            helper[match] = helper.get(match, 0) + 1
        return res