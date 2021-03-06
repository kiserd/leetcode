class Solution:
    def fourSum(self, nums, target: int):
        # handle edge case
        if len(nums) < 4: return []
        # sort array in O(n logn)
        nums.sort()
        # call kSum()
        mySet = self.kSum(nums, target, 4)
        res = []
        for elt in mySet:
            res.append(list(elt))
        return res

    def kSum(self, nums, target, k):
        # handle base case
        if k == 2:
            return self.twoSum(nums, target)
        # handle recursive exploration
        i = 0
        res = set()
        while i <= len(nums) - k:
            # we don't want to repeat the "outer" num
            if i == 0 or nums[i] != nums[i - 1]:
                for elt in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.add((nums[i], ) + elt)
            i += 1
        return res

    def twoSum(self, numbers, target: int):
        # adjust twoSum() slightly to retrieve multiple distinct answers
        st = 0
        ed = len(numbers) - 1
        res = set()
        while st < ed:
            num = numbers[st] + numbers[ed]
            if num == target:
                res.add((numbers[st], numbers[ed]))
                st += 1
            elif num < target:
                st += 1
            else:
                ed -= 1
        return res