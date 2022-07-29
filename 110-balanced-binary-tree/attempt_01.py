from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # define recursive helper function
        def helper(node):
            # handle base case
            if not node:
                return True, 0
            # handle recursive exploration
            left_bal, left_h = helper(node.left)
            right_bal, right_h = helper(node.right)
            # handle case where either subtree is not balanced
            if not left_bal or not right_bal:
                return False, 0
            # handle case where both subtree balanced
            if abs(left_h - right_h) > 1:
                return False, 0
            return True, max(left_h, right_h) + 1
        # kick off helper function
        return helper(root)[0]
