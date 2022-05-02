# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        # define recursive helper function
        def rec(node):
            # handle base case
            if not node:
                return []
            # handle recursive exploration
            return [node.val] + rec(node.left) + rec(node.right)
        return rec(root)
