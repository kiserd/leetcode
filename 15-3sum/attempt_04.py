class Solution:
    def threeSum(self, nums):
        # first sort nums to help with time later
        nums.sort()
        # work through potential first elements
        res = []
        n = len(nums)
        i = 0
        while i < n - 2 and nums[i] < 1:
            if i ==0 or nums[i] != nums[i - 1]:
                for s, t, v in self.twoSum(nums[i + 1:], nums[i]):
                    res.append([s, t, v])
            i += 1
        return res

    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        res = set()
        while i < j and nums[j] > -1:
            if -target == nums[i] + nums[j]:
                res.add((target, nums[i], nums[j]))
                i += 1
                j -= 1
            elif -target < nums[i] + nums[j]:
                j -= 1
            else:
                i += 1
        return res
