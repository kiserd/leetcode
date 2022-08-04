from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # define recursive function
        def back(arr):
            # handle base case
            if not arr:
                return [[]]
            # handle recursive exploration
            res = []
            num = arr.pop()
            for subset in back(arr):
                res.append(subset)
                res.append([num] + subset)
            arr.append(num)
            return res
        return back(nums)
