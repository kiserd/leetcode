class Solution:
    def removeDuplicates(self, nums) -> int:
        # handle edge case
        if len(nums) == 1:
            return 1
        # use two pointers
        avail = 1
        search = 1
        while search < len(nums):
            if nums[search] != nums[search - 1]:
                nums[avail] = nums[search]
                avail += 1
            search += 1
        return avail
