# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        stack = [root]
        res = []
        visited = []
        while len(stack) != 0:
            n = stack.pop()
            if n in visited:
                res.append(n.val)
            if n.right is not None:
                stack.append(n.right)
            stack.append(n)
            if n.left is not None:
                stack.append(n.left)
            visited.append(n)
        return res





# need an iterative approach

# when we reach a node n, we need to 