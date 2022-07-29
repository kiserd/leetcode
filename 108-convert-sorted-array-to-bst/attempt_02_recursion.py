# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        # define recursive helper function
        def helper(st, ed):
            # handle base case
            if st > ed:
                return None
            # handle recursive exploration
            mid = (st + ed) // 2
            left = helper(st, mid - 1)
            right = helper(mid + 1, ed)
            return TreeNode(nums[mid], left, right)
        return helper(0, len(nums) - 1)
