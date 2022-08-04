from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_elts = []
            for subset in res:
                new_elts.append(subset + [num])
            res += new_elts
        return res
