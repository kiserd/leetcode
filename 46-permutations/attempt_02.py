class Solution:
    def permute(self, nums):
        # define recursive helper function
        def rec(arr):
            # handle base case
            if not arr:
                return [[]]
            # handle recursive case
            res = []
            for idx, elt in enumerate(arr):
                for perm in rec(arr[:idx] + arr[idx + 1:]):
                    res.append([elt] + perm)
            return res
        return rec(nums)
