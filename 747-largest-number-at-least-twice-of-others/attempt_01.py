class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        fst = -1
        fst_idx = -1
        scd = 0
        for idx, num in enumerate(nums):
            if num > fst:
                fst, scd = num, fst
                fst_idx = idx
            elif num > scd:
                scd = num
        if fst >= 2 * scd:
            return fst_idx
        return -1
