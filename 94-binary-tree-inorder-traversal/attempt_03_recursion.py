# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        # define helper function
        def rec(node):
            # handle base case
            if not node:
                return []
            # handle recursive exploration
            return rec(node.left) + [node.val] + rec(node.right)
        return rec(root)
