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
            if not node.left and not node.right:
                return target == node.val
            # handle recursive exploration
            target -= node.val
            left_explore = False
            right_explore = False
            if node.left:
                left_explore = helper(node.left, target)
            if node.right:
                right_explore = helper(node.right, target)
            return left_explore or right_explore
        # kick off helper function
        return helper(root, targetSum)