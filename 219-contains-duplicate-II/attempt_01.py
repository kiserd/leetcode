class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        helper = {}
        for idx, num in enumerate(nums):
            if num in helper and helper[num] >= idx:
                return True
            else:
                helper[num] = idx + k
        return False
