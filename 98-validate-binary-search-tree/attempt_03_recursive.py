# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        # define recursive helper function
        def rec(node, lo=2**31, hi=-(2**31) - 1):
            # handle "successful" base case
            if not node:
                return True
            # handle unsuccessful base case
            if node.val <= hi or node.val >= lo:
                return False
            # handle recursive exploration
            return rec(node.left, node.val, hi) and rec(node.right, lo, node.val)
        return rec(root)
