class Solution:
    def rob(self, nums):
        # handle edge case
        if len(nums) < 3:
            return max(nums)
        # initialize working variables
        next_next = nums[len(nums) - 1]
        next = max(nums[len(nums) - 2:])
        # work backward to first house
        for i in range(len(nums) - 3, -1, -1):
            curr = max(nums[i] + next_next, next)
            next_next = next
            next = curr
        return next

# we can remove the base case handling
# class Solution:
#     def rob(self, nums):
#         # initialize working variables
#         next_next = 0
#         next = nums[len(nums) - 1]
#         # work backward to first house
#         for i in range(len(nums) - 2, -1, -1):
#             curr = max(nums[i] + next_next, next)
#             next_next = next
#             next = curr
#         return next
        