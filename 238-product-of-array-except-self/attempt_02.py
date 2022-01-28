# could easily reduce to O(1) space by using res as our
# prec staging array

class Solution:
    def productExceptSelf(self, nums):
        res = [None] * len(nums)
        prod = 1
        # work front to back getting preceding products
        for i, num in enumerate(nums):
            res[i] = prod
            prod *= num
        # work back to front getting succeeding products
        # and populating our return vessel
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res