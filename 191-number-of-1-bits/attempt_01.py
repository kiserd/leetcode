class Solution:
    def hammingWeight(self, n):
        res = 0
        while n > 0:
            # if least sig bit is set, increment res
            res += (n % 2)
            # if least sig bit is set, flip the bit
            n -= (n % 2)
            # bit shift number by one place
            n //= 2
        return res