class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            new_additions = []
            for sub in res:
                new_additions.append(sub + [num])
            res += new_additions
        return res