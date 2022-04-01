# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        # define recursive function
        def helper(node):
            # handle base case
            if not node:
                return 0
            # handle recursive case
            return 1 + max(helper(node.left), helper(node.right))
        return helper(root)
