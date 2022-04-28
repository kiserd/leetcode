class Solution:
    def threeSumSmaller(self, nums, target: int) -> int:
        # sort array and process in similar fashion to regular 3sum
        nums.sort()
        # attempt to return early
        if sum(nums[:3]) >= target:
            return 0
        i = 0
        valid_combos = set()
        res = 0
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                k = len(nums) - 1
                while nums[i] + nums[j] + nums[k] >= target and j < k:
                    k -= 1
                res += (k - j)
                j += 1
            i += 1
        return res
