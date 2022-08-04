class Solution:
    def combinationSum(self, candidates, target):
        # define recursive helper function
        def rec(i, t):
            # handle successful base case
            if t == 0:
                return [[]]
            # handle unsuccessful base case
            if i == len(candidates):
                return []
            # handle recursive exploration
            res = []
            ct = 0
            while candidates[i] * ct <= t:
                for combo in rec(i + 1, t - candidates[i] * ct):
                    res.append(([candidates[i]] * ct) + combo)
                ct += 1
            return res
        return rec(0, target)
