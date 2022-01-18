# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        # handle base case
        if not root:
            return 0
        # handle recursive exploration
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        
        