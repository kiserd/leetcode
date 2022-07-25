class Solution:
    def subsetsWithDup(self, nums):
        # populate map of frequencies
        freqs = {}
        uniques = set()
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
            uniques.add(num)
        uniques = list(uniques) 
        # define recursive helper function
        def helper(i):
            # handle base case
            if i == len(uniques):
                return [[]]
            # handle recursive exploration
            res = []
            for combo in helper(i + 1):
                res.append(combo)
                for ct in range(1, freqs.get(uniques[i], 0) + 1):
                    new_combo = ([uniques[i]] * ct) + combo
                    res.append(new_combo)
            return res
        return helper(0)