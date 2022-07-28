# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # define recursive helper function
        def helper(node, p, q):
            # handle case where current node is a target
            if node == p or node == q:
                return node
            # handle case of first split
            if p.val < node.val < q.val:
                return node
            if p.val > node.val > q.val:
                return node
            # handle recursive exploration
            if node.val < p.val:
                return helper(node.right, p, q)
            else:
                return helper(node.left, p, q)
        return helper(root, p, q)
