class Solution:
    def subsetsWithDup(self, nums):
        # populate map of frequencies
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        # define recursive helper function
        def helper(i):
            # handle base case
            if i == 11:
                return [[]]
            # handle recursive exploration
            res = []
            for combo in helper(i + 1):
                res.append(combo)
                for ct in range(1, freqs.get(i, 0) + 1):
                    new_combo = ([i] * ct) + combo
                    res.append(new_combo)
            return res
        # kick off helper function
        return helper(-10)


