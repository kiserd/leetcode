class Solution:
    def threeSum(self, nums):
        # handle edge case
        if len(nums) < 3: return []
        # sort array in O(n logn)
        nums.sort()
        # use first number to get our twoSum target
        i = 0
        res = []
        while i < len(nums) and nums[i] <= 0:
            # if we repeat "outer" number, we could get duplicates
            if i == 0 or nums[i] != nums[i - 1]:
                for elt in self.twoSum(nums[i + 1:], -nums[i]):
                    res.append([nums[i]] + list(elt))
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