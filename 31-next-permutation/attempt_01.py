class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # top represents the end of the increasing component of the array
        # working from the back of array to front
        tgt_low = len(nums) - 2
        # work backward through array looking for first decreasing elt
        while tgt_low > -1 and nums[tgt_low] >= nums[tgt_low + 1]:
            tgt_low -= 1
        # work from end of array in search of smallest element that is greater
        # than element at tgt_low
        if tgt_low > -1:
            tgt_high = len(nums) - 1
            # found = False
            while nums[tgt_high] <= nums[tgt_low]:
                tgt_high -= 1
            # swap target with idx
            nums[tgt_low], nums[tgt_high] = nums[tgt_high], nums[tgt_low]
            # sort elements following tgt_low
            self.reverse(nums, tgt_low + 1, len(nums) - 1)
        # handle case where no top found
        else:
            nums.reverse()
    
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -=1