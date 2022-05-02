# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        # process using stack
        s = [root]
        res = []
        while s:
            curr = s.pop()
            if curr:
                res.append(curr.val)
                s.append(curr.right)
                s.append(curr.left)
        return res
