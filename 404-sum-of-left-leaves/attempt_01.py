# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # call and return result of recursive formula
        return self.search(root, False)
    
    def search(self, root, left) -> int:
        # handle base case of root is None
        if root is None:
            return 0
        # handle case of leaf
        if left and root.left is None and root.right is None:
            return root.val
        # handle recursive exploration of children
        return self.search(root.left, True) + self.search(root.right, False)
