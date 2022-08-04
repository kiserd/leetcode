from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # build helper data structs
        cts = {}
        uniques = set()
        for num in nums:
            cts[num] = cts.get(num, 0) + 1
            uniques.add(num)

        # define recursive backtracking function
        def back(uniques):
            # handle base case
            if not uniques:
                return [[]]
            # handle recursive exploration
            res = []
            num = list(uniques)[0]
            uniques.remove(num)
            for ct in range(cts[num] + 1):
                for subset in back(uniques):
                    res.append(([num] * ct) + subset)
            uniques.add(num)
            return res
        return back(uniques)
