class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_red = 0
        next_blue = len(nums) - 1
        search = 0
        while search <= next_blue:
            # handle case of 0
            if nums[search] == 0:
                nums[next_red], nums[search] = nums[search], nums[next_red]
                search += 1
                next_red += 1
            # handle case of 2
            elif nums[search] == 2:
                nums[next_blue], nums[search] = nums[search], nums[next_blue]
                next_blue -= 1
            # handle case of 1
            else:
                search += 1
     

# note that if the search index discovers a 2, it will swap the 2 with the
# element in  the next_blue index, but does not increment the search index.
# This is to handle the possibility of a 0 that needs processed.

# in contrast, if a 0 is encountered, it is processed and the search index is
# incremented. We can safely increment the search index, because our program
# ensures us that a 1 resides in the next_red index.
#   -- can't be a 2, that would have been placed at the end of the array
#   -- can't be a 0, that would have been placed before next_red