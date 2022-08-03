from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            # handle base case
            if not node:
                return 1
            # handle recursive exploration
            left = helper(node.left)
            right = helper(node.right)
            # handle case of unbalanced subtree in left or right
            if not left or not right:
                return 0
            # handle case of current subtree being unbalanced
            if abs(left - right) > 1:
                return 0
            # balanced so far, return height
            return max(left, right) + 1
        res = helper(root)
        if not res:
            return False
        return True
