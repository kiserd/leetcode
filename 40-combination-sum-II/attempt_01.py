class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # build array of counts
        counts = [0] * 51
        for candidate in candidates:
            counts[candidate] += 1
        # define recursive helper function
        def rec(i, t):
            # handle successful base case
            if t == 0:
                return [[]]
            # handle unsuccessful base case
            if i == len(counts) or i > t:
                return []
            # handle recursive exploration
            res = []
            # loop through potential starting index
            for idx in range(i, len(counts)):
                # loop through potential counts for candidate
                count = 1
                while count <= counts[idx] and count * idx <= t:
                    # combine with successful recursive explorations
                    for combo in rec(idx + 1, t - count * idx):
                        res.append(([idx] * count) + combo)
                    count += 1
            return res
        return rec(1, target)
