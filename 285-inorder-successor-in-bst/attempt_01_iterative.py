# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        stack = []
        while root != p:
            stack.append(root)
            if p.val > root.val:
                root = root.right
            else:
                root = root.left
        # get right subtree of p
        if p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr
        while stack:
            curr = stack.pop()
            if curr.val > p.val:
                return curr
        return None
