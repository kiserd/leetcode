class Solution:
    def permute(self, nums):
        # define recursive function
        def rec(arr):
            # handle base case
            if not arr:
                return [[]]
            # handle recursive exploration
            res = []
            for i, num in enumerate(arr):
                for perm in rec(arr[:i] + arr[i+1:]):
                    res.append([num] + perm)
            return res
        return rec(nums)
