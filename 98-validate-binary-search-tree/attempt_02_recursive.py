# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root) -> bool:
        # define recursive helper function
        def rec(node):
            # handle base case
            if not node:
                return True, None, None
            # handle recursive exploration
            l_valid, l_lo, l_hi = rec(node.left)
            r_valid, r_lo, r_hi = rec(node.right)
            # if either subtree invalid, tree is invalid
            if not l_valid or not r_valid:
                return False, None, None
            # handle case of valid subtrees
            # first handle valid subtrees but invalid tree
            if l_hi is not None and l_hi >= node.val:
                return False, None, None
            if r_lo is not None and r_lo <= node.val:
                return False, None, None
            # handle valid tree and bubble up range
            lo = l_lo
            if lo is None:
                lo = node.val
            hi = r_hi
            if hi is None:
                hi = node.val
            return True, lo, hi
        # kick off function and return result
        return rec(root)[0]
