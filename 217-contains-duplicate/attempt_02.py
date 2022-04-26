class Solution:
    def containsDuplicate(self, nums) -> bool:
        helper = {}
        for num in nums:
            if helper.get(num, False):
                return True
            else:
                helper[num] = 1
        return False
