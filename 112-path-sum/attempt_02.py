# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        # handle edge case
        if not root:
            return False
        # define recursive helper function
        def helper(node, target):
            # handle base case(s)
            # handle base case of empty node pointed to by non-leaf
            if not node:
                return False
            # handle base case of leaf
            if not node.left and not node.right:
                return target == node.val
            # handle recursive exploration
            target -= node.val
            return helper(node.left, target) or helper(node.right, target)
        # kick off helper function
        return helper(root, targetSum)