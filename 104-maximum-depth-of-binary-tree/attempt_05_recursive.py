# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        # define recursive helper function
        def rec(node):
            # handle base case
            if not node:
                return 0
            # handle recursive exploration
            return 1 + max(rec(node.left), rec(node.right))
        # return function result
        return rec(root)
