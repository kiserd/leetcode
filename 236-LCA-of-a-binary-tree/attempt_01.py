# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ancestor = None

        # define recursive helper function
        def lca(node, p, q):
            nonlocal ancestor
            # handle base case
            if not node:
                return False
            # handle recursive exploration
            # handle case where current node is lca
            left = lca(node.left, p, q)
            right = lca(node.right, p, q)
            if node.val == p.val or node.val == q.val:
                if left or right:
                    ancestor = node
                    return False
                return True
            if right and left:
                ancestor = node
                return False
            return left or right
        lca(root, p, q)
        return ancestor
