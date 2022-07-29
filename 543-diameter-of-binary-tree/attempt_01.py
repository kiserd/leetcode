from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # utilize global variable to track max starting from a
        # different "root" down the tree
        global_max = 0

        # define recursive helper function
        def helper(node):
            nonlocal global_max
            # handle base case
            if not node:
                return 0
            # handle recursive exploration
            left = helper(node.left)
            right = helper(node.right)
            global_max = max(global_max, left + right)
            return max(left, right) + 1
        helper(root)
        return global_max
