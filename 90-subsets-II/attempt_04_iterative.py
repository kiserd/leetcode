from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # init counts
        cts = {}
        for num in nums:
            cts[num] = cts.get(num, 0) + 1
        # progress through by number, adding to set
        res = [[]]
        for num in cts:
            new_elts = []
            for ct in range(1, cts[num] + 1):
                for subset in res:
                    new_elts.append(subset + ([num] * ct))
            res += new_elts
        return res
