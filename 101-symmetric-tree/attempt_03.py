# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        # define recursive helper function
        def rec(left, right):
            # handle base case
            if not left and right or left and not right:
                return False
            if not left and not right:
                return True
            if left.val != right.val:
                return False
            # handle recursive exploration
            if left.val == right.val:
                return rec(left.left, right.right) and rec(left.right, right.left)
        # kick off function and return result
        return rec(root.left, root.right)
