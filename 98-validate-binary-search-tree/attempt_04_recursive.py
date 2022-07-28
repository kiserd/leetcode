# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        # define recursive helper function
        def helper(node, lo=((-2)**31)-1, hi=(2**31)):
            # handle base case(s)
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            # handle recursive exploration
            left = helper(node.left, lo, node.val)
            right = helper(node.right, node.val, hi)
            return left and right
        return helper(root)
