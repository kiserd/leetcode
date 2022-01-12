# work through cyclic replacement approach
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # mod k to make life easier
        k %= len(nums)
        # only process if k is non-zero
        if k != 0:
            # establish variables for use in loop
            reps = 0
            st = curr = k
            temp_out = nums[0]
            first_rep = True
            # only process number of elements in array
            while reps < len(nums):
                # handle shifting of elements
                temp_in = nums[curr]
                nums[curr] = temp_out
                temp_out = temp_in
                curr = (curr + k) % len(nums)
                reps += 1
                # handle case where full cycle was made
                # be careful that this doesn't hit on first rep of cycle
                if curr == st and not first_rep:
                    st = curr = (curr + 1) % k
                    temp_out = nums[(curr - k) % len(nums)]
                    first_rep = True
                first_rep = False