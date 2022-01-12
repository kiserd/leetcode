# spent quite a while trying to find cyclic replacement approach
# stumbled on this while scratching things out on paper
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k != 0:
            self.reverse(nums, 0, len(nums) - 1)
            self.reverse(nums, 0, (k - 1) % len(nums))
            self.reverse(nums, k % len(nums), len(nums) - 1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

