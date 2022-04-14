# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        # define recursive function
        def mirror(l, r):
            # handle base cases
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            # handle recursion
            return mirror(l.left, r.right) and mirror(l.right, r.left)
        if root:
            return mirror(root.left, root.right)
        return True
