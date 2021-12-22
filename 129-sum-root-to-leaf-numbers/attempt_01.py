# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        return self.helper(root, 0)


    def helper(self, root, sum):
        # # handle base case of root == None
        # if root is None:
        # handle base case of leaf
        if root.left is None and root.right is None:
            return (sum * 10) + root.val
        # handle recursive exploration
        left_total = 0
        right_total = 0
        if root.left is not None:
            left_total = self.helper(root.left, (sum * 10) + root.val)
        if root.right is not None:
            right_total = self.helper(root.right, (sum * 10) + root.val)
        return left_total + right_total
                