class Solution:
    def permute(self, nums):
        # handle base case
        if len(nums) == 1:
            return [[nums[0]]]
        # handle recursive exploration
        outer_arr = []
        for i in range(len(nums)):
            for arr in self.permute(nums[:i] + nums[i + 1:]):
                outer_arr.append([nums[i]] + arr)
        return outer_arr
