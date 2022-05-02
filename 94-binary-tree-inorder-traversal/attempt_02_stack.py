# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        # process using stack
        res = []
        stack = [(root, True)]
        while stack:
            curr, process = stack.pop()
            if not process:
                res.append(curr)
            else:
                if curr:
                    stack.append((curr.right, True))
                    stack.append((curr.val, False))
                    stack.append((curr.left, True))
        return res
