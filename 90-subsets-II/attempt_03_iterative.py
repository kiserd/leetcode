class Solution:
    def subsetsWithDup(self, nums):
        # populate map of frequencies
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        # work through nums, adding to set
        res = [[]]
        for num in freqs:
            new_res = []
            for combo in res:
                for ct in range(1, freqs.get(num) + 1):
                    new_res.append(([num] * ct) + combo)
            res += new_res
        return res
