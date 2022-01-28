class Solution:
    def productExceptSelf(self, nums):
        prec = [1] * len(nums)
        res = [None] * len(nums)
        prod = 1
        # work front to back getting preceding products
        for i, num in enumerate(nums):
            prec[i] = prod
            prod *= num
        # work back to front getting succeeding products
        # and populating our return vessel
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = prod * prec[i]
            prod *= nums[i]
        return res