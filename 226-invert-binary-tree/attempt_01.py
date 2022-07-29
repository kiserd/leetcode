from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # define recursive helper function
        def helper(node):
            # handle base case
            if not node:
                return None
            # handle recursive exploration
            node.left, node.right = helper(node.right), helper(node.left)
            return node
        return helper(root)
