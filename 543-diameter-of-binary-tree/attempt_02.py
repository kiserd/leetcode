from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # use global variable to help with subtree problem
        max_path = 0

        # define recursive helper function
        def helper(node):
            nonlocal max_path
            # handle base case
            if not node:
                return 0
            # handle recursive helper function
            left = helper(node.left)
            right = helper(node.right)
            # handle case where longest path has current node as 'root'
            max_path = max(max_path, left + right)
            return max(left, right) + 1
        helper(root)
        return max_path
