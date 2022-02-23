class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # count total zeros in the sequence
        zeros = 0
        for char in s:
            if char == '0':
                zeros += 1
        # track cost to make the current char the first '1'
        min_flips = 100001
        zeros_enc = 0
        ones_enc = 0
        for char in s:
            flips = ones_enc + zeros - zeros_enc
            if char == '0':
                zeros_enc += 1
                flips += 1
            else:
                ones_enc += 1
            min_flips = min(min_flips, flips)
        return min(min_flips, ones_enc)
        