class Solution:
    def firstMissingPositive(self, nums) -> int:
        # work through array, placing elements within range and assigning
        # trash elements a dummy value of 0
        search = 0
        # iterate through nums
        while search < len(nums):
            # assign convenient name to current num
            num = nums[search]
            # handle case where num is already placed
            if num == search + 1:
                search += 1
            # handle case where num is within range
            elif 0 < num and num <= len(nums):
                # handle case of subsequent occurence of num
                if nums[num - 1] == num:
                    nums[search] = 0
                    search += 1
                # handle case of first occurence of num
                else:
                    nums[num - 1], nums[search] = nums[search], nums[num - 1]
            else:
                nums[search] = 0
                search += 1
        # iterate through list in search of first missing positive
        for i, num in enumerate(nums):
            if num == 0:
                return i + 1
        return len(nums) + 1
