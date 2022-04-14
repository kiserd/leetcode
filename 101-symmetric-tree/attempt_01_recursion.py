# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        # define recursive pre-order function
        def dfs_pre(node):
            # handle base case
            if not node:
                return [None]
            # handle recursive case
            return [node.val] + dfs_pre(node.left) + dfs_pre(node.right)

        # define recursive post-order function
        def dfs_post(node):
            # handle base case
            if not node:
                return [None]
            # handle recursive case
            return [node.val] + dfs_post(node.right) + dfs_post(node.left)

        return dfs_pre(root.left) == dfs_post(root.right)
