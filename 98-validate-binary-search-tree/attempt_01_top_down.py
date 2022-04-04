# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root) -> bool:
        # define recursive function
        def helper(parent, lo=-math.inf, hi=math.inf):
            # handle base case
            if not parent:
                return True
            # determine current node validity
            if parent.val <= lo or parent.val >= hi:
                return False
            # handle recursive case
            return helper(parent.left, lo, parent.val) and helper(parent.right, parent.val, hi)
        # call helper and return to calling function
        return helper(root)
