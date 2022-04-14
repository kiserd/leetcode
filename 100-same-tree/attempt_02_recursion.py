# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        # define recursive function
        def same(l, r):
            # handle base cases
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            # handle recursive case
            return same(l.left, r.left) and same(l.right, r.right)
        # kick off function
        return same(p, q)
