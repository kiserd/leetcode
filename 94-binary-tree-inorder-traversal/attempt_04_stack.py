# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        # process using stack
        s = [root]
        visited = set()
        res = []
        while s:
            curr = s.pop()
            if curr:
                if curr in visited:
                    res.append(curr.val)
                else:
                    visited.add(curr)
                    s.append(curr.right)
                    s.append(curr)
                    s.append(curr.left)
        return res
