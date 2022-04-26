class Solution:
    def combinationSum(self, candidates, target: int):
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
            count = 0
            while count * candidates[i] <= t:
                combos = rec(i + 1, t - count * candidates[i])
                for combo in combos:
                    res.append(([candidates[i]] * count) + combo)
                count += 1
            return res
        return rec(0, target)
